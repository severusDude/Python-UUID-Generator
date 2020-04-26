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
        self.generate.setGeometry(QtCore.QRect(160, 70, 75, 40))

        # COPY OUTPUT BUTTON
        self.copy_output = QtWidgets.QPushButton(self.centralWidget)
        self.copy_output.setGeometry(QtCore.QRect(293, 120, 35, 35))

        # OUTPUT
        self.uuid_output = QtWidgets.QLabel(self.centralWidget)
        self.uuid_output.setGeometry(QtCore.QRect(60, 120, 225, 35))
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
