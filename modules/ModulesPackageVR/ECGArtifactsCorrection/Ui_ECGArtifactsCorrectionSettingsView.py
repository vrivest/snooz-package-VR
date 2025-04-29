# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_ECGArtifactsCorrectionSettingsView.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import themes_rc

class Ui_ECGArtifactsCorrectionSettingsView(object):
    def setupUi(self, ECGArtifactsCorrectionSettingsView):
        if not ECGArtifactsCorrectionSettingsView.objectName():
            ECGArtifactsCorrectionSettingsView.setObjectName(u"ECGArtifactsCorrectionSettingsView")
        ECGArtifactsCorrectionSettingsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        ECGArtifactsCorrectionSettingsView.resize(711, 333)
        self.verticalLayout = QVBoxLayout(ECGArtifactsCorrectionSettingsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.eeg_signals_horizontalLayout = QHBoxLayout()
        self.eeg_signals_horizontalLayout.setObjectName(u"eeg_signals_horizontalLayout")
        self.eeg_signals_label = QLabel(ECGArtifactsCorrectionSettingsView)
        self.eeg_signals_label.setObjectName(u"eeg_signals_label")

        self.eeg_signals_horizontalLayout.addWidget(self.eeg_signals_label)

        self.eeg_signals_lineedit = QLineEdit(ECGArtifactsCorrectionSettingsView)
        self.eeg_signals_lineedit.setObjectName(u"eeg_signals_lineedit")

        self.eeg_signals_horizontalLayout.addWidget(self.eeg_signals_lineedit)


        self.verticalLayout.addLayout(self.eeg_signals_horizontalLayout)

        self.ecg_signal_horizontalLayout = QHBoxLayout()
        self.ecg_signal_horizontalLayout.setObjectName(u"ecg_signal_horizontalLayout")
        self.ecg_signal_label = QLabel(ECGArtifactsCorrectionSettingsView)
        self.ecg_signal_label.setObjectName(u"ecg_signal_label")

        self.ecg_signal_horizontalLayout.addWidget(self.ecg_signal_label)

        self.ecg_signal_lineedit = QLineEdit(ECGArtifactsCorrectionSettingsView)
        self.ecg_signal_lineedit.setObjectName(u"ecg_signal_lineedit")

        self.ecg_signal_horizontalLayout.addWidget(self.ecg_signal_lineedit)


        self.verticalLayout.addLayout(self.ecg_signal_horizontalLayout)

        self.filename_horizontalLayout = QHBoxLayout()
        self.filename_horizontalLayout.setObjectName(u"filename_horizontalLayout")
        self.filename_label = QLabel(ECGArtifactsCorrectionSettingsView)
        self.filename_label.setObjectName(u"filename_label")

        self.filename_horizontalLayout.addWidget(self.filename_label)

        self.filename_lineedit = QLineEdit(ECGArtifactsCorrectionSettingsView)
        self.filename_lineedit.setObjectName(u"filename_lineedit")

        self.filename_horizontalLayout.addWidget(self.filename_lineedit)


        self.verticalLayout.addLayout(self.filename_horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ECGArtifactsCorrectionSettingsView)

        QMetaObject.connectSlotsByName(ECGArtifactsCorrectionSettingsView)
    # setupUi

    def retranslateUi(self, ECGArtifactsCorrectionSettingsView):
        ECGArtifactsCorrectionSettingsView.setWindowTitle(QCoreApplication.translate("ECGArtifactsCorrectionSettingsView", u"Form", None))
        self.eeg_signals_label.setText(QCoreApplication.translate("ECGArtifactsCorrectionSettingsView", u"eeg_signals", None))
        self.ecg_signal_label.setText(QCoreApplication.translate("ECGArtifactsCorrectionSettingsView", u"ecg_signal", None))
        self.filename_label.setText(QCoreApplication.translate("ECGArtifactsCorrectionSettingsView", u"filename", None))
    # retranslateUi

