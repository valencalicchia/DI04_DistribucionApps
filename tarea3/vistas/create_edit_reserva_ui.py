# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_edit_reserva.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QFormLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Reservar(object):
    def setupUi(self, Reservar):
        if not Reservar.objectName():
            Reservar.setObjectName(u"Reservar")
        Reservar.setWindowModality(Qt.WindowModality.WindowModal)
        Reservar.resize(420, 316)
        Reservar.setMinimumSize(QSize(420, 316))
        self.verticalLayout = QVBoxLayout(Reservar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vCLblTitulo = QLabel(Reservar)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vCLblTitulo.sizePolicy().hasHeightForWidth())
        self.vCLblTitulo.setSizePolicy(sizePolicy)
        self.vCLblTitulo.setMinimumSize(QSize(25, 0))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vCLblTitulo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.vcLblNombre = QLabel(Reservar)
        self.vcLblNombre.setObjectName(u"vcLblNombre")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.vcLblNombre.setFont(font1)
        self.vcLblNombre.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vcLblNombre)

        self.vcTxtNombre = QLineEdit(Reservar)
        self.vcTxtNombre.setObjectName(u"vcTxtNombre")
        font2 = QFont()
        font2.setPointSize(11)
        self.vcTxtNombre.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vcTxtNombre)

        self.vclblTelefono = QLabel(Reservar)
        self.vclblTelefono.setObjectName(u"vclblTelefono")
        self.vclblTelefono.setFont(font1)
        self.vclblTelefono.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vclblTelefono)

        self.vcTxtTelefono = QLineEdit(Reservar)
        self.vcTxtTelefono.setObjectName(u"vcTxtTelefono")
        self.vcTxtTelefono.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.vcTxtTelefono)

        self.vclblFecha = QLabel(Reservar)
        self.vclblFecha.setObjectName(u"vclblFecha")
        self.vclblFecha.setFont(font1)
        self.vclblFecha.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.vclblFecha)

        self.vcdateEdit = QDateEdit(Reservar)
        self.vcdateEdit.setObjectName(u"vcdateEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.vcdateEdit)

        self.vcLblTipoRes = QLabel(Reservar)
        self.vcLblTipoRes.setObjectName(u"vcLblTipoRes")
        self.vcLblTipoRes.setFont(font1)
        self.vcLblTipoRes.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.vcLblTipoRes)

        self.vccboBoxTipoRes = QComboBox(Reservar)
        self.vccboBoxTipoRes.setObjectName(u"vccboBoxTipoRes")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.vccboBoxTipoRes)

        self.vcLblTipoCocina = QLabel(Reservar)
        self.vcLblTipoCocina.setObjectName(u"vcLblTipoCocina")
        self.vcLblTipoCocina.setFont(font1)
        self.vcLblTipoCocina.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.vcLblTipoCocina)

        self.vccboBoxTipoCocina = QComboBox(Reservar)
        self.vccboBoxTipoCocina.setObjectName(u"vccboBoxTipoCocina")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.vccboBoxTipoCocina)

        self.vcLblNAsist = QLabel(Reservar)
        self.vcLblNAsist.setObjectName(u"vcLblNAsist")
        self.vcLblNAsist.setFont(font1)
        self.vcLblNAsist.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.vcLblNAsist)

        self.vcLayOutCongreso = QHBoxLayout()
        self.vcLayOutCongreso.setSpacing(6)
        self.vcLayOutCongreso.setObjectName(u"vcLayOutCongreso")
        self.vcLayOutCongreso.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.vcchkBoxHabitaciones = QCheckBox(Reservar)
        self.vcchkBoxHabitaciones.setObjectName(u"vcchkBoxHabitaciones")
        self.vcchkBoxHabitaciones.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcchkBoxHabitaciones.sizePolicy().hasHeightForWidth())
        self.vcchkBoxHabitaciones.setSizePolicy(sizePolicy1)
        self.vcchkBoxHabitaciones.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.vcchkBoxHabitaciones.setFont(font3)

        self.vcLayOutCongreso.addWidget(self.vcchkBoxHabitaciones)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.vcLblJornadas = QLabel(Reservar)
        self.vcLblJornadas.setObjectName(u"vcLblJornadas")
        self.vcLblJornadas.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.vcLblJornadas.sizePolicy().hasHeightForWidth())
        self.vcLblJornadas.setSizePolicy(sizePolicy2)
        self.vcLblJornadas.setMaximumSize(QSize(80, 30))
        self.vcLblJornadas.setFont(font3)
        self.vcLblJornadas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.vcLblJornadas)

        self.vcSpinBoxJornadas = QSpinBox(Reservar)
        self.vcSpinBoxJornadas.setObjectName(u"vcSpinBoxJornadas")
        self.vcSpinBoxJornadas.setEnabled(True)
        self.vcSpinBoxJornadas.setMaximum(999)

        self.horizontalLayout_8.addWidget(self.vcSpinBoxJornadas)


        self.vcLayOutCongreso.addLayout(self.horizontalLayout_8)


        self.formLayout.setLayout(6, QFormLayout.FieldRole, self.vcLayOutCongreso)

        self.vcSpinBoxNAsist = QSpinBox(Reservar)
        self.vcSpinBoxNAsist.setObjectName(u"vcSpinBoxNAsist")
        self.vcSpinBoxNAsist.setEnabled(True)
        self.vcSpinBoxNAsist.setMaximum(999)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.vcSpinBoxNAsist)


        self.verticalLayout.addLayout(self.formLayout)

        self.widget = QWidget(Reservar)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.vcbtnReservar = QPushButton(Reservar)
        self.vcbtnReservar.setObjectName(u"vcbtnReservar")
        self.vcbtnReservar.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.vcbtnReservar.sizePolicy().hasHeightForWidth())
        self.vcbtnReservar.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.vcbtnReservar.setFont(font4)
        self.vcbtnReservar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.verticalLayout.addWidget(self.vcbtnReservar)


        self.retranslateUi(Reservar)

        QMetaObject.connectSlotsByName(Reservar)
    # setupUi

    def retranslateUi(self, Reservar):
        Reservar.setWindowTitle(QCoreApplication.translate("Reservar", u"GestionarReserva", None))
#if QT_CONFIG(tooltip)
        Reservar.setToolTip(QCoreApplication.translate("Reservar", u"Gesti\u00f3n de una reserva", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("Reservar", u"Crear/Editar una reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("Reservar", u"GESTIONAR RESERVA", None))
#if QT_CONFIG(tooltip)
        self.vcLblNombre.setToolTip(QCoreApplication.translate("Reservar", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNombre.setText(QCoreApplication.translate("Reservar", u"Nombre", None))
#if QT_CONFIG(tooltip)
        self.vcTxtNombre.setToolTip(QCoreApplication.translate("Reservar", u"Nombre del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblTelefono.setToolTip(QCoreApplication.translate("Reservar", u"Tel\u00e9fono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
        self.vclblTelefono.setText(QCoreApplication.translate("Reservar", u"Telefono", None))
#if QT_CONFIG(tooltip)
        self.vcTxtTelefono.setToolTip(QCoreApplication.translate("Reservar", u"Telefono del/la organizador/a", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vclblFecha.setToolTip(QCoreApplication.translate("Reservar", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
        self.vclblFecha.setText(QCoreApplication.translate("Reservar", u"Fecha", None))
#if QT_CONFIG(tooltip)
        self.vcdateEdit.setToolTip(QCoreApplication.translate("Reservar", u"Fecha del evento", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblTipoRes.setToolTip(QCoreApplication.translate("Reservar", u"Tipo de reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblTipoRes.setText(QCoreApplication.translate("Reservar", u"Tipo de reserva", None))
#if QT_CONFIG(tooltip)
        self.vccboBoxTipoRes.setToolTip(QCoreApplication.translate("Reservar", u"Tipo de reserva", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblTipoCocina.setToolTip(QCoreApplication.translate("Reservar", u"Tipo de cocina", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblTipoCocina.setText(QCoreApplication.translate("Reservar", u"Tipo de cocina", None))
#if QT_CONFIG(tooltip)
        self.vccboBoxTipoCocina.setToolTip(QCoreApplication.translate("Reservar", u"Tipo de cocina", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcLblNAsist.setToolTip(QCoreApplication.translate("Reservar", u"N\u00famero de asistentes", None))
#endif // QT_CONFIG(tooltip)
        self.vcLblNAsist.setText(QCoreApplication.translate("Reservar", u"N\u00ba de Asistentes", None))
#if QT_CONFIG(tooltip)
        self.vcchkBoxHabitaciones.setToolTip(QCoreApplication.translate("Reservar", u"\u00bfHabitaciones para los asistentes?", None))
#endif // QT_CONFIG(tooltip)
        self.vcchkBoxHabitaciones.setText(QCoreApplication.translate("Reservar", u"Habitaciones", None))
        self.vcLblJornadas.setText(QCoreApplication.translate("Reservar", u"Jornadas:", None))
#if QT_CONFIG(tooltip)
        self.vcSpinBoxJornadas.setToolTip(QCoreApplication.translate("Reservar", u"Total de jornadas", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcSpinBoxNAsist.setToolTip(QCoreApplication.translate("Reservar", u"N\u00famero de asistentes", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vcbtnReservar.setToolTip(QCoreApplication.translate("Reservar", u"Confirmar reserva", None))
#endif // QT_CONFIG(tooltip)
        self.vcbtnReservar.setText(QCoreApplication.translate("Reservar", u"Confirmar", None))
    # retranslateUi

