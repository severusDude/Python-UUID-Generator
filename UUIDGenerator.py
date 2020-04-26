from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip


class UserInterface(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setWindowTitle("UUID Generator")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # GENERATE UUID BUTTON
        self.generate = QtWidgets.QPushButton(self.centralWidget)
        self.generate.setGeometry(QtCore.QRect(60, 70, 175, 35))
        icon = QtGui.QIcon()
        icon.addFile("D:\Downloads\Photos\generate.ico")
        self.generate.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.generate.setText("GENERATE")
        self.generate.setFont(font)

        # COPY OUTPUT BUTTON
        self.copy_output = QtWidgets.QPushButton(self.centralWidget)
        self.copy_output.setGeometry(QtCore.QRect(293, 70, 35, 35))

        # OUTPUT
        self.uuid_output = QtWidgets.QLabel(self.centralWidget)
        self.uuid_output.setGeometry(QtCore.QRect(25, 120, 350, 35))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.uuid_output.setFont(font)
        self.uuid_output.setFrameShape(QtWidgets.QFrame.Box)
        self.uuid_output.setFrameShadow(QtWidgets.QFrame.Plain)

        # CENTRAL WIDGET
        MainWindow.setCentralWidget(self.centralWidget)
