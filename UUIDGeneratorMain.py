# Backend for UUIDGenerator

import pyperclip
import sys
from UUIDGenerator import *
from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Optional
import re
import subprocess
import uuid


class ControlMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = UserInterface()
        self.main_ui.setupUi(self)
        self.opt_index = int()
        self.output = str()
        self.output_str = str()
        print(f"button {self.opt_index} is enabled")

        self.main_ui.generate.clicked.connect(self.generate_click)

        self.main_ui.copy_output.clicked.connect(self.copy_button)

    def generate_click(self):
        self.output = self.generate_uuid_1()
        self.output_str += self.output
        self.output_str = self.output_str.replace('urn:uuid:', '')
        self.main_ui.uuid_output.setText(self.output_str)

    def copy_button(self):
        pyperclip.copy(self.output_str)

    # defining method 1 generating uuid
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
    program = ControlMainWindow()
    program.show()
    sys.exit(app.exec_())
