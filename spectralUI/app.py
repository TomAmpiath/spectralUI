# This file is part of spectralUI.
#
# Copyright 2021, Tom George Ampiath, All rights reserved.
#
# spectralUI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# spectralUI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectralUI.  If not, see <http://www.gnu.org/licenses/>.

import sys

from PySide2.QtWidgets import QApplication

from spectralUI import instancehandler as ih
from spectralUI.mainwindow import MainWindow


class Application(QApplication):
    """Main application"""

    def __init__(self, args):
        super().__init__(args)

        ih.APP_INST = self

        main_window = MainWindow()
        main_window.show()

        sys.exit(self.exec_())


def main():
    """Main function and application entry point"""
    app = Application([])
