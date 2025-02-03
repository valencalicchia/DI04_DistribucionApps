# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(439, 157)
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vCLblTitulo = QLabel(self.centralwidget)
        self.vCLblTitulo.setObjectName(u"vCLblTitulo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vCLblTitulo.sizePolicy().hasHeightForWidth())
        self.vCLblTitulo.setSizePolicy(sizePolicy)
        self.vCLblTitulo.setMinimumSize(QSize(25, 25))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.vCLblTitulo.setFont(font)
        self.vCLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.vCLblTitulo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.vCLblUsuario = QLabel(self.centralwidget)
        self.vCLblUsuario.setObjectName(u"vCLblUsuario")
        self.vCLblUsuario.setFont(font)
        self.vCLblUsuario.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.vCLblUsuario)

        self.vCTxtUsuario = QLineEdit(self.centralwidget)
        self.vCTxtUsuario.setObjectName(u"vCTxtUsuario")
        font1 = QFont()
        font1.setPointSize(11)
        self.vCTxtUsuario.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.vCTxtUsuario)

        self.vCLblPwd = QLabel(self.centralwidget)
        self.vCLblPwd.setObjectName(u"vCLblPwd")
        self.vCLblPwd.setFont(font)
        self.vCLblPwd.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.vCLblPwd)

        self.vCTxtPwd = QLineEdit(self.centralwidget)
        self.vCTxtPwd.setObjectName(u"vCTxtPwd")
        self.vCTxtPwd.setFont(font1)
        self.vCTxtPwd.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.vCTxtPwd)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.vCBtnAcceder = QPushButton(self.centralwidget)
        self.vCBtnAcceder.setObjectName(u"vCBtnAcceder")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vCBtnAcceder.sizePolicy().hasHeightForWidth())
        self.vCBtnAcceder.setSizePolicy(sizePolicy1)
        self.vCBtnAcceder.setMinimumSize(QSize(100, 30))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.vCBtnAcceder.setFont(font2)
        self.vCBtnAcceder.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_2.addWidget(self.vCBtnAcceder)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.formLayout)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
#if QT_CONFIG(accessibility)
        Login.setAccessibleDescription(QCoreApplication.translate("Login", u"Login", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.vCLblTitulo.setToolTip(QCoreApplication.translate("Login", u"Login", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblTitulo.setText(QCoreApplication.translate("Login", u"LOGIN", None))
#if QT_CONFIG(tooltip)
        self.vCLblUsuario.setToolTip(QCoreApplication.translate("Login", u"Usuario", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblUsuario.setText(QCoreApplication.translate("Login", u"Usuario", None))
#if QT_CONFIG(tooltip)
        self.vCTxtUsuario.setToolTip(QCoreApplication.translate("Login", u"Ingrese su usuario", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.vCLblPwd.setToolTip(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
#endif // QT_CONFIG(tooltip)
        self.vCLblPwd.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
#if QT_CONFIG(tooltip)
        self.vCTxtPwd.setToolTip(QCoreApplication.translate("Login", u"Ingrese su contrase\u00f1a", None))
#endif // QT_CONFIG(tooltip)
        self.vCBtnAcceder.setText(QCoreApplication.translate("Login", u"Acceder", None))
    # retranslateUi

