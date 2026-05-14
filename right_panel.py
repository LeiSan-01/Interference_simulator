from PyQt5 import QtWidgets, QtCore, QtGui

def setup_right_panel(self, centralwidget):
    """Setup the right side with title and tabs"""
    # Second vertical layout (right)
    self.verticalLayoutWidget_4 = QtWidgets.QWidget(centralwidget)
    self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1030, 50, 841, 925))
    self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")

    self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
    self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
    self.verticalLayout_2.setObjectName("verticalLayout_2")

    # Title
    self.title = QtWidgets.QLabel(self.verticalLayoutWidget_4)
    self.title.setTextFormat(QtCore.Qt.MarkdownText)
    self.title.setScaledContents(False)
    self.title.setIndent(-1)
    self.title.setObjectName("title")
    self.verticalLayout_2.addWidget(self.title)

    # Call the Tab_view config
    setup_tabs(self)

def setup_tabs(self):
    """
    Setup all tabs with their respective content.
    """
    self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget_4)
    self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
    self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
    self.tabWidget.setObjectName("tabWidget")

    # Create all tabs
    
    base_route = QtCore.QDir.current()  # for image import from the images dir we extract the path

    #---EXPERIMENT---
    self.tab = QtWidgets.QWidget()
    self.tab.setObjectName("tab")

    self.image_0 = QtWidgets.QLabel(self.tab)
    self.image_0.setGeometry(QtCore.QRect(50, 40, 741, 491))
    self.image_0.setText("")
    
    route0 = base_route.filePath("images/Patro_de_difraccio.png")
    self.image_0.setPixmap(QtGui.QPixmap(route0))
    self.image_0.setScaledContents(True)
    self.image_0.setObjectName("image_0")

    self.label_0 = QtWidgets.QLabel(self.tab)
    self.label_0.setGeometry(QtCore.QRect(50, 600, 731, 301))
    self.label_0.setObjectName("label_0")
    self.tabWidget.addTab(self.tab, "")

    #---WAVELENGTH---
    self.tab1 = QtWidgets.QWidget()
    self.tab1.setObjectName("tab1")

    self.label_1 = QtWidgets.QLabel(self.tab1)
    self.label_1.setGeometry(QtCore.QRect(50, 600, 731, 301))
    self.label_1.setObjectName("label_1")

    self.image_1 = QtWidgets.QLabel(self.tab1)
    self.image_1.setGeometry(QtCore.QRect(50, 40, 741, 491))
    self.image_1.setText("")
    
    route1 = base_route.filePath("images/wavelength.png")
    self.image_1.setPixmap(QtGui.QPixmap(route1))
    self.image_1.setScaledContents(True)
    self.image_1.setObjectName("image_1")
    self.tabWidget.addTab(self.tab1, "")

    #---SCREEN DISTANCE---
    self.tab2 = QtWidgets.QWidget()
    self.tab2.setObjectName("tab2")

    self.label_2 = QtWidgets.QLabel(self.tab2)
    self.label_2.setGeometry(QtCore.QRect(50, 600, 731, 301))
    self.label_2.setObjectName("label_2")

    self.image_2 = QtWidgets.QLabel(self.tab2)
    self.image_2.setGeometry(QtCore.QRect(50, 40, 741, 491))
    self.image_2.setText("")
    
    route2 = base_route.filePath("images/screendist.png")
    self.image_2.setPixmap(QtGui.QPixmap(route2))
    self.image_2.setScaledContents(True)
    self.image_2.setObjectName("image_2")
    self.tabWidget.addTab(self.tab2, "")

    #---SLIT SEPARATION---
    self.tab3 = QtWidgets.QWidget()
    self.tab3.setObjectName("tab3")

    self.label_3 = QtWidgets.QLabel(self.tab3)
    self.label_3.setGeometry(QtCore.QRect(50, 600, 731, 301))
    self.label_3.setObjectName("label_3")

    self.image_3 = QtWidgets.QLabel(self.tab3)
    self.image_3.setGeometry(QtCore.QRect(50, 40, 741, 491))
    self.image_3.setText("")

    route3 = base_route.filePath("images/slitdist.png")
    self.image_3.setPixmap(QtGui.QPixmap(route3))
    self.image_3.setScaledContents(True)
    self.image_3.setObjectName("image_3")
    self.tabWidget.addTab(self.tab3, "")

    #---SLIT WIDTH---
    self.tab5 = QtWidgets.QWidget()
    self.tab5.setObjectName("tab5")

    self.label_4 = QtWidgets.QLabel(self.tab5)
    self.label_4.setGeometry(QtCore.QRect(50, 600, 731, 301))
    self.label_4.setObjectName("label_4")

    self.image_4 = QtWidgets.QLabel(self.tab5)
    self.image_4.setGeometry(QtCore.QRect(50, 40, 741, 491))
    self.image_4.setText("")
    
    route4 = base_route.filePath("images/slit_width.jpeg")
    self.image_4.setPixmap(QtGui.QPixmap(route4))
    self.image_4.setScaledContents(True)
    self.image_4.setObjectName("image_4")
    self.tabWidget.addTab(self.tab5, "")
    
    self.verticalLayout_2.addWidget(self.tabWidget)