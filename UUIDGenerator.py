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
        icon.addFile("icons\generate.ico")
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.generate.setText("GENERATE")
        self.generate.setFont(font)
        self.generate.setIcon(icon)

        # COPY OUTPUT BUTTON
        self.copy_output = QtWidgets.QPushButton(self.centralWidget)
        self.copy_output.setGeometry(QtCore.QRect(275, 70, 35, 35))
        icon = QtGui.QIcon()
        icon.addFile("icons\copy.ico")
        self.copy_output.setIcon(icon)

        # OUTPUT
        self.uuid_output = QtWidgets.QLabel(self.centralWidget)
        self.uuid_output.setGeometry(QtCore.QRect(15, 120, 360, 35))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.uuid_output.setFont(font)
        self.uuid_output.setFrameShape(QtWidgets.QFrame.Box)
        self.uuid_output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.uuid_output.setStyleSheet("""
        QWidget {
            border: 2px solid black;
            border-radius: 4px;
            background-color: #2f3542;
        }
        """)

        # CENTRAL WIDGET
        MainWindow.setCentralWidget(self.centralWidget)
