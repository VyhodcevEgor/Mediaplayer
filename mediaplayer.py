from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os

from MainWindow import Ui_MainWindow

tracks = {}
track_count = {}


def hhmmss(ms):
    s = ms // 1000 % 60
    m = ms // 60000 % 60
    h = ms // 3600000 % 24
    return ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))


class ViewerWindow(QMainWindow):
    state = pyqtSignal(bool)
    rewind_signal = pyqtSignal(str)

    def closeEvent(self, e):
        self.state.emit(False)

    def keyPressEvent(self, e):
        print(f" Viewer key: {e.key()}")
        if e.key() == Qt.Key_V:
            self.close()
        if e.key() == Qt.Key_Left:
            self.rewind_signal.emit('backward')
        if e.key() == Qt.Key_Right:
            self.rewind_signal.emit('forward')
        else:
            super(ViewerWindow, self).keyPressEvent(e)

    @pyqtSlot()
    def main_rewind(self, e):
        if e.key() == Qt.Key_Left:
            self.rewind_signal.emit('backward')
        if e.key() == Qt.Key_Right:
            self.rewind_signal.emit('forward')


class PlaylistModel(QStringListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole:
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index):
        return self.playlist.mediaCount()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setFocusPolicy(Qt.StrongFocus)
        self.viewerWindow_state = ViewerWindow()
        self.viewerWindow_state.rewind_signal.connect(lambda sig: print(sig))

        self.player = QMediaPlayer()

        self.player.error.connect(self.erroralert)
        self.player.play()
        self.playlist = QMediaPlaylist()
        self.player.setPlaylist(self.playlist)

        self.viewer = ViewerWindow(self)
        self.viewer.setWindowFlags(
            self.viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(QSize(480, 360))

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)

        self.sort_viewer = ViewerWindow(self)
        self.sort_viewer.setWindowFlags(
            self.sort_viewer.windowFlags() | Qt.WindowStaysOnTopHint)
        self.sort_viewer.setMinimumSize(QSize(480, 360))

        self.sorting_view = QListWidget()
        self.sorting_view.setDragDropMode(QAbstractItemView.InternalMove)
        self.sort_viewer.setCentralWidget(self.sorting_view)

        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)
        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.shuffleButton.pressed.connect(self.shuffle)

        self.viewButton.toggled.connect(self.toggle_viewer)
        self.viewer.state.connect(self.viewButton.setChecked)

        self.sortButton.toggled.connect(self.toggle_sorting)
        self.sort_viewer.state.connect(self.sortButton.setChecked)

        self.muteButton.toggled.connect(self.toggle_mute)
        self.icon8 = QIcon()
        self.icon8.addPixmap(QPixmap("images/mute.png"),
                             QIcon.Normal, QIcon.Off)

        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)

        self.playlist.currentIndexChanged.connect(
            self.playlist_position_changed)
        selection_model = self.playlistView.selectionModel()
        selection_model.selectionChanged.connect(
            self.playlist_selection_changed)

        self.playlistView.setFocusPolicy(Qt.StrongFocus)
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)
        self.timeSlider.valueChanged.connect(self.player.setPosition)

        self.open_file_action.triggered.connect(self.open_files)

        self.setAcceptDrops(True)
        self.show()

    def keyPressEvent(self, e):
        print(e.key())
        if e.key() == Qt.Key_Delete:
            self.delete_from_playlist()
        if e.key() == Qt.Key_Space:
            self.play_pause()
        if e.key() == Qt.Key_Left:
            self.rewind('backward')
        if e.key() == Qt.Key_Right:
            self.rewind('forward')
        if e.key() == Qt.Key_M:
            self.muteButton.click()
        if e.key() == Qt.Key_S:
            self.stopButton.click()
        if e.key() == Qt.Key_R:
            self.shuffle()
        if e.key() == Qt.Key_V:
            self.viewButton.click()
        if e.key() == Qt.Key_Q:
            self.sortButton.click()
        if e.key() == Qt.Key_Up:
            self.change_volume('higher')
        if e.key() == Qt.Key_Down:
            self.change_volume('lower')
        else:
            super(MainWindow, self).keyPressEvent(e)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.acceptProposedAction()

    def dropEvent(self, e):
        for url in e.mimeData().urls():
            self.playlist.addMedia(
                QMediaContent(url)
            )
            tracks[url.fileName()] = url
            track_count[url.fileName()] = \
                track_count.setdefault(url.fileName(), 0) + 1
            self.sorting_view.addItem(url.fileName())

        self.model.layoutChanged.emit()

        if self.player.state() != QMediaPlayer.PlayingState:
            #i = self.playlist.mediaCount() - len(e.mimeData().urls())
            ix = self.model.index(0)
            self.playlistView.setCurrentIndex(ix)
            self.playlist.setCurrentIndex(0)
            self.player.play()

    def open_files(self):
        path_list, _ = QFileDialog.getOpenFileNames(self, "Open file", "",
                                                    "mp3 Audio (*.mp3);;"
                                                    "mp4 Video (*.mp4);;"
                                                    "Movie files (*.mov);;"
                                                    "All files (*.*)")

        if path_list:
            for path in path_list:
                url = QUrl.fromLocalFile(path)
                self.playlist.addMedia(
                    QMediaContent(
                        url
                    )
                )
                tracks[url.fileName()] = url
                track_count[url.fileName()] = \
                    track_count.setdefault(url.fileName(), 0) + 1
                self.sorting_view.addItem(url.fileName())

        self.model.layoutChanged.emit()

    def update_duration(self, duration):
        #print("!", duration)
        #print("?", self.player.duration())

        self.timeSlider.setMaximum(duration)

        if duration >= 0:
            self.totalTimeLabel.setText(hhmmss(duration))

    def update_position(self, position):
        if position >= 0:
            self.currentTimeLabel.setText(hhmmss(position))

        self.timeSlider.blockSignals(True)
        self.timeSlider.setValue(position)
        self.timeSlider.blockSignals(False)

    def playlist_selection_changed(self, ix):
        print("selection changed")
        i = ix.indexes()[0].row()
        self.playlist.setCurrentIndex(i)

    def playlist_position_changed(self, i):
        print("pos changed")
        if i > -1:
            ix = self.model.index(i)
            self.playlistView.setCurrentIndex(ix)

    def delete_from_playlist(self):
        idx = int(self.playlist.currentIndex())
        ix_del = self.model.index(idx)
        if idx - 1 > -1:
            print(self.model.data(ix_del, Qt.DisplayRole))
            track_count[self.model.data(ix_del, Qt.DisplayRole)] = \
                track_count.setdefault(self.model.data(ix_del,
                                                       Qt.DisplayRole), 0) - 1
            print(track_count)
            if track_count[self.model.data(ix_del, Qt.DisplayRole)] == 0:
                _ = tracks.pop(self.model.data(ix_del, Qt.DisplayRole), None)
                self.sorting_view.takeItem(idx)
            ix = self.model.index(idx - 1)
            self.model.beginRemoveRows(ix, 1, 1)
            self.playlist.removeMedia(idx)
            self.model.endRemoveRows()
            self.playlistView.setCurrentIndex(ix)
            self.playlist.setCurrentIndex(idx - 1)

        if idx - 1 == -1:
            if idx + 1 < self.playlist.mediaCount():
                track_count[self.model.data(ix_del, Qt.DisplayRole)] = \
                    track_count.setdefault(self.model.data(ix_del,
                                                           Qt.DisplayRole),
                                           0) - 1
                print(track_count)
                if track_count[self.model.data(ix_del, Qt.DisplayRole)] == 0:
                    _ = tracks.pop(self.model.data(ix_del, Qt.DisplayRole),
                                   None)
                    self.sorting_view.takeItem(idx)
                ix = self.model.index(idx + 1)
                self.playlistView.setCurrentIndex(ix)
                self.playlist.removeMedia(idx)

                self.playlist.setCurrentIndex(idx)
                self.player.play()

            else:
                tracks.clear()
                self.sorting_view.clear()
                self.playlist.clear()
                self.model.beginResetModel()
                self.model.endResetModel()

    def shuffle(self):
        self.model.beginResetModel()
        self.playlist.shuffle()
        self.model.endResetModel()
        ix = self.model.index(0)
        self.playlistView.setCurrentIndex(ix)

    def toggle_viewer(self, state):
        if state:
            self.viewer.show()
        else:
            self.viewer.hide()

    def toggle_sorting(self, state):
        if state:
            self.sort_viewer.show()
        else:
            sorted_list = [self.sorting_view.item(row).text() for row in
                           range(self.sorting_view.count())]
            self.playlist.clear()
            self.model.beginResetModel()
            self.model.endResetModel()
            for track in sorted_list:
                self.playlist.addMedia(
                    QMediaContent(tracks[track])
                )
            ix = self.model.index(0)
            self.playlistView.setCurrentIndex(ix)
            self.playlist.setCurrentIndex(0)
            self.player.play()
            self.sort_viewer.hide()

    def toggle_mute(self, state):
        if state:
            self.player.setMuted(True)
            self.muteButton.setIcon(self.icon8)
        else:
            self.player.setMuted(False)
            self.muteButton.setIcon(self.icon7)

    def play_pause(self):
        if self.player.state() != QMediaPlayer.PlayingState:
            self.player.play()
        else:
            self.player.pause()

    def rewind(self, operation):
        if operation == 'backward':
            pos = self.player.position()
            self.timeSlider.setValue(pos - 5000)
            self.update_position(pos - 5000)

        if operation == 'forward':
            pos = self.player.position()
            self.timeSlider.setValue(pos + 5000)
            self.update_position(pos + 5000)

    def change_volume(self, operation):
        if operation == 'higher':
            pos = self.volumeSlider.value()
            self.volumeSlider.setValue(pos + 5)
            if self.player.isMuted():
                self.toggle_mute(False)

        if operation == 'lower':
            pos = self.volumeSlider.value()
            self.volumeSlider.setValue(pos - 5)
            if self.volumeSlider.value() == 0:
                self.toggle_mute(True)

    def erroralert(self, *args):
        print(args)


if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QApplication([])
    app.setApplicationName("Медиапроигрыватель")
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(28, 9, 228))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(170, 7, 177))
    palette.setColor(QPalette.AlternateBase, QColor(128, 3, 122))
    palette.setColor(QPalette.ToolTipBase, QColor(136, 8, 221))
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(136, 8, 221))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(50, 223, 35))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; "
        "background-color: #2a82da; border: 1px solid white; }")

    window = MainWindow()
    app.exec_()
