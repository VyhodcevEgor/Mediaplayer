from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(484, 371)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.playlistView = QtWidgets.QListView(self.centralWidget)
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)
        self.playlistView.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout.addWidget(self.playlistView)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.currentTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.currentTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.currentTimeLabel.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horizontalLayout_4.addWidget(self.currentTimeLabel)

        self.timeSlider = QtWidgets.QSlider(self.centralWidget)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_4.addWidget(self.timeSlider)

        self.totalTimeLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 0))
        self.totalTimeLabel.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.horizontalLayout_4.addWidget(self.totalTimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.previousButton = QtWidgets.QPushButton(self.centralWidget)
        self.previousButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/previous.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon)
        self.previousButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.previousButton.setObjectName("previousButton")
        self.horizontalLayout_5.addWidget(self.previousButton)

        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/control.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_5.addWidget(self.playButton)

        self.pauseButton = QtWidgets.QPushButton(self.centralWidget)
        self.pauseButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/pause.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_5.addWidget(self.pauseButton)

        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/stop.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon3)
        self.stopButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_5.addWidget(self.stopButton)

        self.nextButton = QtWidgets.QPushButton(self.centralWidget)
        self.nextButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/next.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon4)
        self.nextButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_5.addWidget(self.nextButton)

        self.shuffleButton = QtWidgets.QPushButton(self.centralWidget)
        self.shuffleButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/shuffle.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shuffleButton.setIcon(icon5)
        self.shuffleButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.shuffleButton.setObjectName("shuffleButton")
        self.horizontalLayout_5.addWidget(self.shuffleButton)

        self.viewButton = QtWidgets.QPushButton(self.centralWidget)
        self.viewButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/video.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewButton.setIcon(icon6)
        self.viewButton.setCheckable(True)
        self.viewButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.viewButton.setObjectName("viewButton")
        self.horizontalLayout_5.addWidget(self.viewButton)

        self.sortButton = QtWidgets.QPushButton(self.centralWidget)
        self.sortButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/sort_list.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sortButton.setIcon(icon9)
        self.sortButton.setCheckable(True)
        self.sortButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sortButton.setObjectName("sortButton")
        self.horizontalLayout_5.addWidget(self.sortButton)

        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)

        self.muteButton = QtWidgets.QPushButton(self.centralWidget)
        self.muteButton.setText("")
        self.icon7 = QtGui.QIcon()
        self.icon7.addPixmap(QtGui.QPixmap("images/unmute.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(self.icon7)
        self.muteButton.setCheckable(True)
        self.muteButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.muteButton.setObjectName("muteButton")
        self.horizontalLayout_5.addWidget(self.muteButton)

        self.volumeSlider = QtWidgets.QSlider(self.centralWidget)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setProperty("value", 100)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName("volumeSlider")
        self.volumeSlider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 484, 22))
        self.menuBar.setObjectName("menuBar")

        self.menuFIle = QtWidgets.QMenu(self.menuBar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menuBar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.open_file_action = QtWidgets.QAction(MainWindow)
        self.open_file_action.setObjectName("open_file_action")
        self.menuFIle.addAction(self.open_file_action)
        self.menuBar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Медиапроигрыватель"))
        self.currentTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.totalTimeLabel.setText(_translate("MainWindow", "0:00"))
        self.menuFIle.setTitle(_translate("MainWindow", "Медиа"))
        self.open_file_action.setText(_translate("MainWindow", "Добавить "
                                                               "медиафайлы"))
