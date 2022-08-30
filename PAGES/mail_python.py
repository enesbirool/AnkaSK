from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(618, 400)
        Form.setMaximumSize(QtCore.QSize(700, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/martialarts_g.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.login_open_button = QtWidgets.QPushButton(Form)
        self.login_open_button.setEnabled(True)
        self.login_open_button.setStyleSheet("")
        self.login_open_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/assets/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_open_button.setIcon(icon1)
        self.login_open_button.setIconSize(QtCore.QSize(10, 10))
        self.login_open_button.setCheckable(True)
        self.login_open_button.setObjectName("login_open_button")
        self.horizontalLayout_6.addWidget(self.login_open_button)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.baglanti_durumu_checkBox = QtWidgets.QCheckBox(Form)
        self.baglanti_durumu_checkBox.setEnabled(False)
        self.baglanti_durumu_checkBox.setMouseTracking(True)
        self.baglanti_durumu_checkBox.setAcceptDrops(False)
        self.baglanti_durumu_checkBox.setStatusTip("")
        self.baglanti_durumu_checkBox.setText("")
        self.baglanti_durumu_checkBox.setCheckable(False)
        self.baglanti_durumu_checkBox.setTristate(False)
        self.baglanti_durumu_checkBox.setObjectName("baglanti_durumu_checkBox")
        self.horizontalLayout_6.addWidget(self.baglanti_durumu_checkBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.baglan_lanesi = QtWidgets.QHBoxLayout()
        self.baglan_lanesi.setContentsMargins(-1, 0, -1, -1)
        self.baglan_lanesi.setObjectName("baglan_lanesi")
        self.mail_edit = QtWidgets.QLineEdit(Form)
        self.mail_edit.setObjectName("mail_edit")
        self.baglan_lanesi.addWidget(self.mail_edit)
        self.password_edit = QtWidgets.QLineEdit(Form)
        self.password_edit.setObjectName("password_edit")
        self.baglan_lanesi.addWidget(self.password_edit)
        self.baglan_pushbutton = QtWidgets.QPushButton(Form)
        self.baglan_pushbutton.setObjectName("baglan_pushbutton")
        self.baglan_lanesi.addWidget(self.baglan_pushbutton)
        self.logout_pushbutton = QtWidgets.QPushButton(Form)
        self.logout_pushbutton.setObjectName("logout_pushbutton")
        self.baglan_lanesi.addWidget(self.logout_pushbutton)
        self.verticalLayout_5.addLayout(self.baglan_lanesi)
        self.verticalLayout.addLayout(self.verticalLayout_5)
        self.konu_basligi_lineEdit = QtWidgets.QLineEdit(Form)
        self.konu_basligi_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.konu_basligi_lineEdit.setInputMask("")
        self.konu_basligi_lineEdit.setObjectName("konu_basligi_lineEdit")
        self.verticalLayout.addWidget(self.konu_basligi_lineEdit)
        self.message_textEdit = QtWidgets.QTextEdit(Form)
        self.message_textEdit.setMinimumSize(QtCore.QSize(300, 100))
        self.message_textEdit.setMaximumSize(QtCore.QSize(500, 10000000))
        self.message_textEdit.setObjectName("message_textEdit")
        self.verticalLayout.addWidget(self.message_textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.herkese_button = QtWidgets.QPushButton(Form)
        self.herkese_button.setObjectName("herkese_button")
        self.horizontalLayout_3.addWidget(self.herkese_button)
        self.son_ay_button = QtWidgets.QPushButton(Form)
        self.son_ay_button.setObjectName("son_ay_button")
        self.horizontalLayout_3.addWidget(self.son_ay_button)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.kalan_mail_label = QtWidgets.QLabel(Form)
        self.kalan_mail_label.setText("")
        self.kalan_mail_label.setObjectName("kalan_mail_label")
        self.horizontalLayout_4.addWidget(self.kalan_mail_label)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.mail_sended_textBrowser = QtWidgets.QTextBrowser(Form)
        self.mail_sended_textBrowser.setObjectName("mail_sended_textBrowser")
        self.verticalLayout_4.addWidget(self.mail_sended_textBrowser)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gonder_button = QtWidgets.QPushButton(Form)
        self.gonder_button.setObjectName("gonder_button")
        self.horizontalLayout_2.addWidget(self.gonder_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Toplu Mail Gönder"))
        self.label_2.setText(_translate("Form", "Bağlantı Durumu :"))
        self.mail_edit.setPlaceholderText(_translate("Form", "Mail Adresinizi giriniz"))
        self.password_edit.setPlaceholderText(_translate("Form", "Şifrenizi Giriniz..."))
        self.baglan_pushbutton.setText(_translate("Form", "Bağlan"))
        self.logout_pushbutton.setText(_translate("Form", "Logout"))
        self.konu_basligi_lineEdit.setPlaceholderText(_translate("Form", "Konu Başlığını Giriniz..."))
        self.message_textEdit.setPlaceholderText(_translate("Form", "Mesajınızı buraya giriniz...."))
        self.herkese_button.setText(_translate("Form", "Herkese"))
        self.son_ay_button.setText(_translate("Form", "Son Ay Vermeyen"))
        self.label.setText(_translate("Form", "Kalan Mail Gönderimi : "))
        self.gonder_button.setText(_translate("Form", "Gönder"))


import assets.py_rc.icons_rc as icons_rc

