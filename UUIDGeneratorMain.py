# Backend for UUIDGenerator

import pyperclip
import sys
import qdarkstyle
from UUIDGenerator import *
from PyQt5 import QtCore, QtGui, QtWidgets
import uuid


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = UserInterface()
        self.main_ui.setupUi(self)
        self.opt_index = int()
        self.output = str()
        self.output_length = int()

        # connect button to a function
        self.main_ui.generate.clicked.connect(self.generate_click)

        # initialize copy button
        self.main_ui.copy_output.clicked.connect(self.copy_button)

    # defining action when generate button is clicked
    def generate_click(self):
        self.output = self.generate_uuid_1()
        self.output = self.output.replace('urn:uuid:', '')
        self.output_length = len(self.output)
        if self.output_length > 0:
            self.main_ui.uuid_output.clear()
            self.main_ui.uuid_output.setText(self.output)
        else:
            self.main_ui.uuid_output.setText(self.output)

    # defining action when copy button is clicked
    def copy_button(self):
        pyperclip.copy(self.output)

    # defining method generating uuid
    def generate_uuid_1(self):
        import uuid
        output = uuid.uuid4().urn
        return output

    # defining system exception
    def log_uncaught_exceptions(self, ex_cls, ex, tb):
        text = '{}: {}:\n'.format(ex_cls.__name__, ex)
        import traceback
        text += ''.join(traceback.format_tb(tb))

        print(text)
        self.main_ui.QMessageBox.critical(None, 'Error', text)
        quit()

    sys.excepthook = log_uncaught_exceptions


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    program = ControlMainWindow()
    program.show()
    sys.exit(app.exec_())
