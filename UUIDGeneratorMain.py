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

    # defining method 1 generating uuid
    def generate_uuid_1(self):
        import uuid
        output = uuid.uuid4()
        return output

    # defining method 2 generating uuid
    def generate_uuid_2(self):
        random_string = ''
        random_str_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        uuid_format = [8, 4, 4, 4, 12]
        for n in uuid_format:
            for i in range(0, n):
                random_string += str(
                    random_str_seq[r.randint(0, len(random_str_seq) - 1)])
            if n != 12:
                random_string += '-'
        return random_string

    # defining method 3 generating uuid
    def generate_uuid_3(self) -> Optional[uuid.UUID]:
        try:
            # Ask Windows for the device's permanent UUID. Throws if command missing/fails.
            txt = subprocess.check_output("wmic csproduct get uuid").decode()

            # Attempt to extract the UUID from the command's result.
            match = re.search(r"\bUUID\b[\s\r\n]+([^\s\r\n]+)", txt)
            if match is not None:
                txt = match.group(1)
                if txt is not None:
                    # Remove the surrounding whitespace (newlines, space, etc)
                    # and useless dashes etc, by only keeping hex (0-9 A-F) chars.
                    txt = re.sub(r"[^0-9A-Fa-f]+", "", txt)

                    # Ensure we have exactly 32 characters (16 bytes).
                    if len(txt) == 32:
                        return uuid.UUID(txt)
        except:
            pass  # Silence subprocess exception.

        return None

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
