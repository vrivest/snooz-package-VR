# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_SubtractSignalsResultsView.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)
import themes_rc

class Ui_SubtractSignalsResultsView(object):
    def setupUi(self, SubtractSignalsResultsView):
        if not SubtractSignalsResultsView.objectName():
            SubtractSignalsResultsView.setObjectName(u"SubtractSignalsResultsView")
        SubtractSignalsResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        SubtractSignalsResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(SubtractSignalsResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(SubtractSignalsResultsView)

        QMetaObject.connectSlotsByName(SubtractSignalsResultsView)
    # setupUi

    def retranslateUi(self, SubtractSignalsResultsView):
        SubtractSignalsResultsView.setWindowTitle(QCoreApplication.translate("SubtractSignalsResultsView", u"Form", None))
    # retranslateUi

