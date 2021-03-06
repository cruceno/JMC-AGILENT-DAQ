# -*- coding: utf-8 -*-

"""
Form implementation generated from reading ui file './JMC_AgilentADQ.ui'.

Created by: PyQt4 UI code generator 4.11.4

WARNING! All changes made in this file will be lost!
"""
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):

        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_jmc_agilent_daq(object):
    """Interfaz grafica generada con pyuic."""

    def setupUi(self, jmc_agilent_daq):
        QtGui.QFontDatabase.addApplicationFont("./fonts/EXO2REGULAR.TTF")
        font = QtGui.QFont('Exo 2')
        jmc_agilent_daq.setObjectName(_fromUtf8("jmc_agilent_daq"))
        jmc_agilent_daq.resize(800, 600)
        jmc_agilent_daq.setWindowIcon(QtGui.QIcon(
            QtGui.QPixmap('./gui/images/logo-symbol-64x64.png')))

        self.centralwidget = QtGui.QWidget(jmc_agilent_daq)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.centralwidget.setStyleSheet(
            'QWidget {background-color:rgb(47,157,195)}')
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.daq_tab = QtGui.QWidget()
        self.daq_tab.setStyleSheet(
            'QWidget {background-color:rgb(255,255,255)}')
        self.daq_tab.setObjectName(_fromUtf8("daq_tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.daq_tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gb_daq_mainplot = QtGui.QGroupBox(self.daq_tab)
        font.setPointSize(20)
        self.gb_daq_mainplot.setFont(font)
        self.gb_daq_mainplot.setObjectName(_fromUtf8("gb_daq_mainplot"))
        self.gridLayout_2.addWidget(self.gb_daq_mainplot, 1, 3, 5, 3)
        self.gb_multimeter_config_lines = QtGui.QGroupBox(self.daq_tab)
        font.setPointSize(14)
        self.gb_multimeter_config_lines.setFont(font)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.gb_multimeter_config_lines.sizePolicy().hasHeightForWidth())
        self.gb_multimeter_config_lines.setSizePolicy(sizePolicy)
        self.gb_multimeter_config_lines.setObjectName(_fromUtf8(
            "gb_multimeter_config_lines"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gb_multimeter_config_lines)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.pb_save_multimeter_config = QtGui.QPushButton(
            self.gb_multimeter_config_lines)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pb_save_multimeter_config.sizePolicy().hasHeightForWidth())
        self.pb_save_multimeter_config.setSizePolicy(sizePolicy)
        font.setPointSize(14)
        self.pb_save_multimeter_config.setFont(font)
        self.pb_save_multimeter_config.setObjectName(
            _fromUtf8("pb_save_multimeter_config"))
        self.gridLayout_3.addWidget(self.pb_save_multimeter_config, 0, 0, 1, 1)
        self.pb_load_multimeter_config = QtGui.QPushButton(
            self.gb_multimeter_config_lines)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pb_load_multimeter_config.sizePolicy().hasHeightForWidth())
        self.pb_load_multimeter_config.setSizePolicy(sizePolicy)
        font.setPointSize(14)
        self.pb_load_multimeter_config.setFont(font)
        self.pb_load_multimeter_config.setObjectName(
            _fromUtf8("pb_load_multimeter_config"))
        self.gridLayout_3.addWidget(self.pb_load_multimeter_config, 0, 1, 1, 1)
        self.pte_config_lines = QtGui.QPlainTextEdit(
            self.gb_multimeter_config_lines)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pte_config_lines.sizePolicy().hasHeightForWidth())
        self.pte_config_lines.setSizePolicy(sizePolicy)
        font.setPointSize(14)
        self.pte_config_lines.setFont(font)
        self.pte_config_lines.setObjectName(_fromUtf8("pte_config_lines"))
        self.pte_config_lines.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.gridLayout_3.addWidget(self.pte_config_lines, 1, 0, 1, 2)
        self.pb_load_multimeter_config.raise_()
        self.pb_save_multimeter_config.raise_()
        self.pte_config_lines.raise_()
        self.pte_config_lines.raise_()
        self.gridLayout_2.addWidget(self.gb_multimeter_config_lines,
                                    3, 0, 1, 3)
        self.lb_select_device = QtGui.QLabel(self.daq_tab)
        font.setPointSize(14)
        self.lb_select_device.setFont(font)
        self.lb_select_device.setObjectName(_fromUtf8("lb_select_device"))
        self.gridLayout_2.addWidget(self.lb_select_device, 0, 0, 1, 2)
        self.lb_output_file = QtGui.QLabel(self.daq_tab)
        font.setPointSize(14)
        self.lb_output_file.setFont(font)
        self.lb_output_file.setObjectName(_fromUtf8("lb_output_file"))
        self.gridLayout_2.addWidget(self.lb_output_file, 0, 3, 1, 1)

        self.le_output_file = QtGui.QLineEdit(self.daq_tab)
        self.le_output_file.setObjectName(_fromUtf8("le_output_file"))
        self.gridLayout_2.addWidget(self.le_output_file, 0, 4, 1, 1)

        self.cbx_input_device = QtGui.QComboBox(self.daq_tab)
        self.cbx_input_device.setMinimumHeight(24)
        self.cbx_input_device.setObjectName(_fromUtf8("cbx_input_device"))
        self.gridLayout_2.addWidget(self.cbx_input_device, 1, 0, 1, 3)

        self.tlb_load_devices = QtGui.QToolButton(self.daq_tab)
        self.tlb_load_devices.setIcon(QtGui.QIcon(QtGui.QPixmap(
            './gui/images/black-update.png')))
        self.tlb_load_devices.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tlb_load_devices.setObjectName(_fromUtf8("tlb_load_devices"))
        self.tlb_load_devices.setFixedSize(32, 32)
        self.gridLayout_2.addWidget(self.tlb_load_devices, 0, 2, 1, 2)

        self.tlb_output_file = QtGui.QToolButton(self.daq_tab)
        self.tlb_output_file.setIcon(QtGui.QIcon(QtGui.QPixmap(
            './gui/images/folder_black.png')))
        self.tlb_output_file.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.tlb_output_file.setFixedSize(32, 32)
        self.tlb_output_file.setObjectName(_fromUtf8("tlb_output_file"))
        self.gridLayout_2.addWidget(self.tlb_output_file, 0, 5, 1, 1)

        self.lb_data_per_second = QtGui.QLabel(self.daq_tab)
        font.setPointSize(14)
        self.lb_data_per_second.setFont(font)
        self.lb_data_per_second.setObjectName(_fromUtf8("lb_data_per_second"))
        self.gridLayout_2.addWidget(self.lb_data_per_second, 2, 0, 1, 1)

        self.sb_data_per_second = QtGui.QSpinBox(self.daq_tab)
        font.setPointSize(14)
        self.sb_data_per_second.setFont(font)
        self.sb_data_per_second.setObjectName(_fromUtf8("sb_data_per_second"))
        self.gridLayout_2.addWidget(self.sb_data_per_second, 2, 2, 1, 1)

        self.lcd_current_value = QtGui.QLCDNumber(self.daq_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lcd_current_value.sizePolicy().hasHeightForWidth())
        self.lcd_current_value.setSizePolicy(sizePolicy)
        self.lcd_current_value.setMinimumSize(QtCore.QSize(0, 70))
        font.setPointSize(12)
        self.lcd_current_value.setFont(font)
        self.lcd_current_value.setFrameShape(QtGui.QFrame.Box)
        self.lcd_current_value.setFrameShadow(QtGui.QFrame.Plain)
        self.lcd_current_value.setLineWidth(1)
        self.lcd_current_value.setMidLineWidth(0)
        self.lcd_current_value.setSmallDecimalPoint(True)
        self.lcd_current_value.setNumDigits(8)
        self.lcd_current_value.setDigitCount(8)
        self.lcd_current_value.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_current_value.setProperty("value", 1.0)
        self.lcd_current_value.setProperty("intValue", 1)
        self.lcd_current_value.setObjectName(_fromUtf8("lcd_current_value"))
        self.gridLayout_2.addWidget(self.lcd_current_value, 4, 0, 1, 3)
        self.pb_start = QtGui.QPushButton(self.daq_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pb_start.sizePolicy().hasHeightForWidth())
        self.pb_start.setSizePolicy(sizePolicy)
        self.pb_start.setMinimumSize(QtCore.QSize(0, 70))
        font.setPointSize(30)
        self.pb_start.setFont(font)
        self.pb_start.setObjectName(_fromUtf8("pb_start"))
        self.gridLayout_2.addWidget(self.pb_start, 5, 0, 1, 3)
        self.tabWidget.addTab(self.daq_tab, _fromUtf8(""))

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        jmc_agilent_daq.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(jmc_agilent_daq)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        jmc_agilent_daq.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(jmc_agilent_daq)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        jmc_agilent_daq.setStatusBar(self.statusbar)

        self.retranslateUi(jmc_agilent_daq)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(jmc_agilent_daq)

    def disable_controls(self):
        self.cbx_input_device.setEnabled(False)
        self.le_output_file.setEnabled(False)
        self.tlb_output_file.setEnabled(False)
        self.pb_save_multimeter_config.setEnabled(False)
        self.pb_load_multimeter_config.setEnabled(False)
        self.pte_config_lines.setEnabled(False)

    def enable_controls(self):
        self.cbx_input_device.setEnabled(True)
        self.le_output_file.setEnabled(True)
        self.tlb_output_file.setEnabled(True)
        self.pb_save_multimeter_config.setEnabled(True)
        self.pb_load_multimeter_config.setEnabled(True)
        self.pte_config_lines.setEnabled(True)

    def retranslateUi(self, jmc_agilent_daq):
        jmc_agilent_daq.setWindowTitle(_translate("jmc_agilent_daq",
                                                  "Agilent DAQ", None))
        self.gb_daq_mainplot.setTitle(_translate("jmc_agilent_daq",
                                                 "Plot", None))
        self.gb_multimeter_config_lines.setTitle(_translate("jmc_agilent_daq",
                                                            "Multimeter Config Lines",
                                                            None))
        self.pb_save_multimeter_config.setText(_translate("jmc_agilent_daq", "Save Config", None))
        self.pb_load_multimeter_config.setText(_translate("jmc_agilent_daq", "Load Config", None))
        self.lb_select_device.setText(_translate("jmc_agilent_daq", "Select Agilent Multimeter", None))
        self.lb_output_file.setText(_translate("jmc_agilent_daq", "Output File", None))
        self.tlb_output_file.setText(_translate("jmc_agilent_daq", "...", None))
        self.lb_data_per_second.setText(_translate("jmc_agilent_daq", "Data per second", None))
        self.pb_start.setText(_translate("jmc_agilent_daq", "Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.daq_tab), _translate("jmc_agilent_daq", "DAQ", None))
