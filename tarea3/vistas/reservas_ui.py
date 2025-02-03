# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservas.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_MostrarReservas(object):
    def setupUi(self, MostrarReservas):
        if not MostrarReservas.objectName():
            MostrarReservas.setObjectName(u"MostrarReservas")
        MostrarReservas.setWindowModality(Qt.WindowModality.WindowModal)
        MostrarReservas.resize(995, 492)
        self.vcCentralWidget = QWidget(MostrarReservas)
        self.vcCentralWidget.setObjectName(u"vcCentralWidget")
        self.verticalLayout = QVBoxLayout(self.vcCentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(self.vcCentralWidget)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vcListWidSalones = QListWidget(self.vcCentralWidget)
        self.vcListWidSalones.setObjectName(u"vcListWidSalones")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcListWidSalones.sizePolicy().hasHeightForWidth())
        self.vcListWidSalones.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(11)
        self.vcListWidSalones.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcListWidSalones)

        self.vcGridReservas = QTableView(self.vcCentralWidget)
        self.vcGridReservas.setObjectName(u"vcGridReservas")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcGridReservas.sizePolicy().hasHeightForWidth())
        self.vcGridReservas.setSizePolicy(sizePolicy1)
        self.vcGridReservas.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcGridReservas)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.vcbtnReservar = QPushButton(self.vcCentralWidget)
        self.vcbtnReservar.setObjectName(u"vcbtnReservar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vcbtnReservar.sizePolicy().hasHeightForWidth())
        self.vcbtnReservar.setSizePolicy(sizePolicy2)
        self.vcbtnReservar.setMinimumSize(QSize(100, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.vcbtnReservar.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnReservar)

        self.vcbtnModificar = QPushButton(self.vcCentralWidget)
        self.vcbtnModificar.setObjectName(u"vcbtnModificar")
        sizePolicy2.setHeightForWidth(self.vcbtnModificar.sizePolicy().hasHeightForWidth())
        self.vcbtnModificar.setSizePolicy(sizePolicy2)
        self.vcbtnModificar.setMinimumSize(QSize(100, 40))
        self.vcbtnModificar.setFont(font2)

        self.horizontalLayout.addWidget(self.vcbtnModificar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MostrarReservas.setCentralWidget(self.vcCentralWidget)

        self.retranslateUi(MostrarReservas)

        QMetaObject.connectSlotsByName(MostrarReservas)
    # setupUi

    def retranslateUi(self, MostrarReservas):
        MostrarReservas.setWindowTitle(QCoreApplication.translate("MostrarReservas", u"Reservas", None))
#if QT_CONFIG(tooltip)
        MostrarReservas.setToolTip(QCoreApplication.translate("MostrarReservas", u"Listado de reservas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("MostrarReservas", u"Reservas", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("MostrarReservas", u"RESERVAS", None))
#if QT_CONFIG(tooltip)
        self.vcListWidSalones.setToolTip(QCoreApplication.translate("MostrarReservas", u"Salones disponibles", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcGridReservas.setToolTip(QCoreApplication.translate("MostrarReservas", u"Listado de reservas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnReservar.setToolTip(QCoreApplication.translate("MostrarReservas", u"Crear nueva reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnReservar.setText(QCoreApplication.translate("MostrarReservas", u"Reservar", None))
#if QT_CONFIG(tooltip)
        self.vcbtnModificar.setToolTip(QCoreApplication.translate("MostrarReservas", u"Modificar reserva seleccionada", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnModificar.setText(QCoreApplication.translate("MostrarReservas", u"Modificar", None))
    # retranslateUi

