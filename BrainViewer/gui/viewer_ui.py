# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 900))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self._brain_gp = QtWidgets.QGroupBox(self.centralwidget)
        self._brain_gp.setMinimumSize(QtCore.QSize(0, 0))
        self._brain_gp.setMaximumSize(QtCore.QSize(419, 98))
        self._brain_gp.setCheckable(True)
        self._brain_gp.setObjectName("_brain_gp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self._brain_gp)
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._brain_transparency_lb = QtWidgets.QLabel(self._brain_gp)
        self._brain_transparency_lb.setMinimumSize(QtCore.QSize(75, 25))
        self._brain_transparency_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        self._brain_transparency_lb.setObjectName("_brain_transparency_lb")
        self.horizontalLayout.addWidget(self._brain_transparency_lb)
        self._brain_transparency_slider = QtWidgets.QSlider(self._brain_gp)
        self._brain_transparency_slider.setMinimumSize(QtCore.QSize(250, 25))
        self._brain_transparency_slider.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self._brain_transparency_slider.setFont(font)
        self._brain_transparency_slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._brain_transparency_slider.setAutoFillBackground(False)
        self._brain_transparency_slider.setMaximum(100)
        self._brain_transparency_slider.setSingleStep(10)
        self._brain_transparency_slider.setPageStep(10)
        self._brain_transparency_slider.setProperty("value", 30)
        self._brain_transparency_slider.setSliderPosition(30)
        self._brain_transparency_slider.setOrientation(QtCore.Qt.Horizontal)
        self._brain_transparency_slider.setInvertedAppearance(False)
        self._brain_transparency_slider.setInvertedControls(False)
        self._brain_transparency_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self._brain_transparency_slider.setTickInterval(10)
        self._brain_transparency_slider.setObjectName("_brain_transparency_slider")
        self.horizontalLayout.addWidget(self._brain_transparency_slider)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._brain_hemi_lb = QtWidgets.QLabel(self._brain_gp)
        self._brain_hemi_lb.setMinimumSize(QtCore.QSize(113, 25))
        self._brain_hemi_lb.setMaximumSize(QtCore.QSize(1999999, 25))
        self._brain_hemi_lb.setObjectName("_brain_hemi_lb")
        self.horizontalLayout_2.addWidget(self._brain_hemi_lb)
        self._brain_hemi_cbx = QtWidgets.QComboBox(self._brain_gp)
        self._brain_hemi_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._brain_hemi_cbx.setMaximumSize(QtCore.QSize(1000, 25))
        self._brain_hemi_cbx.setObjectName("_brain_hemi_cbx")
        self._brain_hemi_cbx.addItem("")
        self._brain_hemi_cbx.addItem("")
        self._brain_hemi_cbx.addItem("")
        self.horizontalLayout_2.addWidget(self._brain_hemi_cbx)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self._brain_gp)
        self._rois_gp = QtWidgets.QGroupBox(self.centralwidget)
        self._rois_gp.setMinimumSize(QtCore.QSize(0, 700))
        self._rois_gp.setMaximumSize(QtCore.QSize(419, 16777215))
        self._rois_gp.setCheckable(True)
        self._rois_gp.setObjectName("_rois_gp")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self._rois_gp)
        self.verticalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self._roi_transparency_lb = QtWidgets.QLabel(self._rois_gp)
        self._roi_transparency_lb.setMinimumSize(QtCore.QSize(75, 25))
        self._roi_transparency_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        self._roi_transparency_lb.setObjectName("_roi_transparency_lb")
        self.horizontalLayout_4.addWidget(self._roi_transparency_lb)
        self._roi_transparency_slider = QtWidgets.QSlider(self._rois_gp)
        self._roi_transparency_slider.setMinimumSize(QtCore.QSize(250, 25))
        self._roi_transparency_slider.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self._roi_transparency_slider.setFont(font)
        self._roi_transparency_slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._roi_transparency_slider.setAutoFillBackground(False)
        self._roi_transparency_slider.setMaximum(100)
        self._roi_transparency_slider.setSingleStep(10)
        self._roi_transparency_slider.setPageStep(10)
        self._roi_transparency_slider.setProperty("value", 100)
        self._roi_transparency_slider.setSliderPosition(100)
        self._roi_transparency_slider.setOrientation(QtCore.Qt.Horizontal)
        self._roi_transparency_slider.setInvertedAppearance(False)
        self._roi_transparency_slider.setInvertedControls(False)
        self._roi_transparency_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self._roi_transparency_slider.setTickInterval(10)
        self._roi_transparency_slider.setObjectName("_roi_transparency_slider")
        self.horizontalLayout_4.addWidget(self._roi_transparency_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self._roi_hemi_lb = QtWidgets.QLabel(self._rois_gp)
        self._roi_hemi_lb.setMinimumSize(QtCore.QSize(75, 25))
        self._roi_hemi_lb.setMaximumSize(QtCore.QSize(16777215, 25))
        self._roi_hemi_lb.setObjectName("_roi_hemi_lb")
        self.horizontalLayout_6.addWidget(self._roi_hemi_lb)
        self._roi_hemi_cbx = QtWidgets.QComboBox(self._rois_gp)
        self._roi_hemi_cbx.setMinimumSize(QtCore.QSize(250, 25))
        self._roi_hemi_cbx.setMaximumSize(QtCore.QSize(250, 25))
        self._roi_hemi_cbx.setObjectName("_roi_hemi_cbx")
        self._roi_hemi_cbx.addItem("")
        self._roi_hemi_cbx.addItem("")
        self._roi_hemi_cbx.addItem("")
        self.horizontalLayout_6.addWidget(self._roi_hemi_cbx)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self._roi_stack = QtWidgets.QStackedWidget(self._rois_gp)
        self._roi_stack.setLineWidth(0)
        self._roi_stack.setObjectName("_roi_stack")
        self._lh_page = QtWidgets.QWidget()
        self._lh_page.setObjectName("_lh_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self._lh_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self._lh_info_list = QtWidgets.QListWidget(self._lh_page)
        self._lh_info_list.setMinimumSize(QtCore.QSize(0, 640))
        self._lh_info_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._lh_info_list.setFont(font)
        self._lh_info_list.setAutoFillBackground(True)
        self._lh_info_list.setAlternatingRowColors(False)
        self._lh_info_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self._lh_info_list.setObjectName("_lh_info_list")
        self.verticalLayout_4.addWidget(self._lh_info_list)
        self._roi_stack.addWidget(self._lh_page)
        self._rh_page = QtWidgets.QWidget()
        self._rh_page.setObjectName("_rh_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self._rh_page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self._rh_info_list = QtWidgets.QListWidget(self._rh_page)
        self._rh_info_list.setMinimumSize(QtCore.QSize(0, 640))
        self._rh_info_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._rh_info_list.setFont(font)
        self._rh_info_list.setAutoFillBackground(True)
        self._rh_info_list.setAlternatingRowColors(False)
        self._rh_info_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self._rh_info_list.setObjectName("_rh_info_list")
        self.verticalLayout_5.addWidget(self._rh_info_list)
        self._roi_stack.addWidget(self._rh_page)
        self._other_page = QtWidgets.QWidget()
        self._other_page.setObjectName("_other_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self._other_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self._other_info_list = QtWidgets.QListWidget(self._other_page)
        self._other_info_list.setMinimumSize(QtCore.QSize(0, 640))
        self._other_info_list.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._other_info_list.setFont(font)
        self._other_info_list.setAutoFillBackground(True)
        self._other_info_list.setAlternatingRowColors(False)
        self._other_info_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self._other_info_list.setObjectName("_other_info_list")
        self.verticalLayout_6.addWidget(self._other_info_list)
        self._roi_stack.addWidget(self._other_page)
        self.verticalLayout_2.addWidget(self._roi_stack)
        self.verticalLayout_3.addWidget(self._rois_gp)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self._plotter = Brain(self.centralwidget)
        self._plotter.setMinimumSize(QtCore.QSize(850, 800))
        self._plotter.setObjectName("_plotter")
        self.horizontalLayout_3.addWidget(self._plotter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1300, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self._View_menu = QtWidgets.QMenu(self.menuEdit)
        self._View_menu.setObjectName("_View_menu")
        self._Color_menu = QtWidgets.QMenu(self.menuEdit)
        self._Color_menu.setObjectName("_Color_menu")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../iEEGTool/iEEGTool/icon/screenshot.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionBrain_Color = QtWidgets.QAction(MainWindow)
        self.actionBrain_Color.setObjectName("actionBrain_Color")
        self.actionBackground_Color = QtWidgets.QAction(MainWindow)
        self.actionBackground_Color.setObjectName("actionBackground_Color")
        self._bg_color_action = QtWidgets.QAction(MainWindow)
        self._bg_color_action.setObjectName("_bg_color_action")
        self._brain_color_action = QtWidgets.QAction(MainWindow)
        self._brain_color_action.setObjectName("_brain_color_action")
        self._front_action = QtWidgets.QAction(MainWindow)
        self._front_action.setObjectName("_front_action")
        self._back_action = QtWidgets.QAction(MainWindow)
        self._back_action.setObjectName("_back_action")
        self._left_action = QtWidgets.QAction(MainWindow)
        self._left_action.setObjectName("_left_action")
        self._right_action = QtWidgets.QAction(MainWindow)
        self._right_action.setObjectName("_right_action")
        self._top_action = QtWidgets.QAction(MainWindow)
        self._top_action.setObjectName("_top_action")
        self._bottom_action = QtWidgets.QAction(MainWindow)
        self._bottom_action.setObjectName("_bottom_action")
        self._load_surface_action = QtWidgets.QAction(MainWindow)
        self._load_surface_action.setShortcutVisibleInContextMenu(False)
        self._load_surface_action.setObjectName("_load_surface_action")
        self._load_volume_action = QtWidgets.QAction(MainWindow)
        self._load_volume_action.setObjectName("_load_volume_action")
        self.action_PNG = QtWidgets.QAction(MainWindow)
        self.action_PNG.setObjectName("action_PNG")
        self._export_action = QtWidgets.QAction(MainWindow)
        self._export_action.setObjectName("_export_action")
        self._load_lut_action = QtWidgets.QAction(MainWindow)
        self._load_lut_action.setObjectName("_load_lut_action")
        self._github_action = QtWidgets.QAction(MainWindow)
        self._github_action.setObjectName("_github_action")
        self.menuFile.addAction(self._load_surface_action)
        self.menuFile.addAction(self._load_volume_action)
        self.menuFile.addAction(self._load_lut_action)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self._export_action)
        self._View_menu.addAction(self._front_action)
        self._View_menu.addAction(self._back_action)
        self._View_menu.addAction(self._left_action)
        self._View_menu.addAction(self._right_action)
        self._View_menu.addAction(self._top_action)
        self._View_menu.addAction(self._bottom_action)
        self._Color_menu.addAction(self._bg_color_action)
        self._Color_menu.addAction(self._brain_color_action)
        self.menuEdit.addAction(self._Color_menu.menuAction())
        self.menuEdit.addAction(self._View_menu.menuAction())
        self.menuHelp.addAction(self._github_action)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self._brain_gp.setTitle(_translate("MainWindow", "Brain"))
        self._brain_transparency_lb.setText(_translate("MainWindow", "Transparency"))
        self._brain_hemi_lb.setText(_translate("MainWindow", "Hemisphere"))
        self._brain_hemi_cbx.setItemText(0, _translate("MainWindow", "Both"))
        self._brain_hemi_cbx.setItemText(1, _translate("MainWindow", "Left"))
        self._brain_hemi_cbx.setItemText(2, _translate("MainWindow", "Right"))
        self._rois_gp.setTitle(_translate("MainWindow", "Regions of Interest"))
        self._roi_transparency_lb.setText(_translate("MainWindow", "Transparency"))
        self._roi_hemi_lb.setText(_translate("MainWindow", "Hemisphere"))
        self._roi_hemi_cbx.setItemText(0, _translate("MainWindow", "Left"))
        self._roi_hemi_cbx.setItemText(1, _translate("MainWindow", "Right"))
        self._roi_hemi_cbx.setItemText(2, _translate("MainWindow", "Other"))
        self._lh_info_list.setSortingEnabled(True)
        self._rh_info_list.setSortingEnabled(True)
        self._other_info_list.setSortingEnabled(True)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self._View_menu.setTitle(_translate("MainWindow", "View"))
        self._Color_menu.setTitle(_translate("MainWindow", "Color"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.actionBrain_Color.setText(_translate("MainWindow", "Brain Color"))
        self.actionBackground_Color.setText(_translate("MainWindow", "Background Color"))
        self._bg_color_action.setText(_translate("MainWindow", "Background color"))
        self._brain_color_action.setText(_translate("MainWindow", "Brain color"))
        self._front_action.setText(_translate("MainWindow", "Front"))
        self._back_action.setText(_translate("MainWindow", "Back"))
        self._left_action.setText(_translate("MainWindow", "Left"))
        self._right_action.setText(_translate("MainWindow", "Right"))
        self._top_action.setText(_translate("MainWindow", "Top"))
        self._bottom_action.setText(_translate("MainWindow", "Bottom"))
        self._load_surface_action.setText(_translate("MainWindow", "Load surface"))
        self._load_surface_action.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self._load_volume_action.setText(_translate("MainWindow", "Load volumes"))
        self._load_volume_action.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_PNG.setText(_translate("MainWindow", ".PNG"))
        self._export_action.setText(_translate("MainWindow", "Export"))
        self._load_lut_action.setText(_translate("MainWindow", "Load ColorLut"))
        self._load_lut_action.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self._github_action.setText(_translate("MainWindow", "Github"))
from utils.brain import Brain


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
