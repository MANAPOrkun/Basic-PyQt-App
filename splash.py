from PyQt5 import QtCore, QtGui, QtWidgets

import login
from register import register_form


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(923, 479)

        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.progressBar)

        self.timer.start(100)

        Form.setStyleSheet("")
        self.frame = QtWidgets.QFrame(Form)

        self.frame.setGeometry(QtCore.QRect(10, 10, 791, 461))
        self.frame.setStyleSheet(
            "image: url(:/background/Resources/1920x1080-px-Moon-satellite-simple-space-1473897.jpg);\n"
            "background-color: rgb(0, 0, 0);\n"
            "border-size:10px;\n"
            "border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.my_progressBar = QtWidgets.QProgressBar(self.frame)

        self.my_progressBar.setGeometry(QtCore.QRect(20, 400, 751, 31))
        self.my_progressBar.setStyleSheet("QProgressBar{\n"
                                          "    ;\n"
                                          "    background-color: rgb(30, 30, 30);\n"
                                          "    border-style: none;\n"
                                          "    border-radius: 10px;\n"
                                          "    text-align: center;\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    image:null;\n"
                                          "}\n"
                                          "QProgressBar::chunk{\n"
                                          "    \n"
                                          "    background-color:rgb(85, 170, 255);\n"
                                          "    border-radius: 10px;\n"
                                          "    image:null;\n"
                                          "}")
        self.my_progressBar.setProperty("value", 24)
        self.my_progressBar.setObjectName("my_progressBar")
        self.label = QtWidgets.QLabel(self.frame)

        self.label.setGeometry(QtCore.QRect(340, 330, 101, 51))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("image:null;\n"
                                 "background-color: rgba(255, 255, 255, 0);\n"
                                 "border-size:0px;\n"
                                 "border-radius:0px;\n"
                                 "color:white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)

        self.label_2.setGeometry(QtCore.QRect(290, 10, 221, 81))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(35)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("image:null;\n"
                                   "background-color: rgba(255, 255, 255, 0);\n"
                                   "border-size:0px;\n"
                                   "border-radius:0px;\n"
                                   "color:white;")
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(Form)

        self.frame_2.setGeometry(QtCore.QRect(680, 80, 241, 271))
        self.frame_2.setStyleSheet("image: url(:/background/Resources/astranaut.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def progressBar(self):

        value = self.my_progressBar.value()
        if value < 100:
            value = value + 4
            self.my_progressBar.setValue(value)
        else:
            self.timer.stop()

            self.ui = register_form()
            self.window = QtWidgets.QMainWindow()
            self.ui.setupUi(self.window)
            self.window.show()
            Form.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Loading"))
        self.label_2.setText(_translate("Form", "The Moon"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
