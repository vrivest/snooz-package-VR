# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_EcgOnEegFilterResultsView.ui'
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

class Ui_EcgOnEegFilterResultsView(object):
    def setupUi(self, EcgOnEegFilterResultsView):
        if not EcgOnEegFilterResultsView.objectName():
            EcgOnEegFilterResultsView.setObjectName(u"EcgOnEegFilterResultsView")
        EcgOnEegFilterResultsView.setStyleSheet(u"font: 12pt \"Roboto\";")
        EcgOnEegFilterResultsView.resize(483, 360)
        self.verticalLayout = QVBoxLayout(EcgOnEegFilterResultsView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.result_layout = QVBoxLayout()
        self.result_layout.setObjectName(u"result_layout")

        self.verticalLayout.addLayout(self.result_layout)


        self.retranslateUi(EcgOnEegFilterResultsView)

        QMetaObject.connectSlotsByName(EcgOnEegFilterResultsView)
    # setupUi

    def retranslateUi(self, EcgOnEegFilterResultsView):
        EcgOnEegFilterResultsView.setWindowTitle(QCoreApplication.translate("EcgOnEegFilterResultsView", u"Form", None))
    # retranslateUi

