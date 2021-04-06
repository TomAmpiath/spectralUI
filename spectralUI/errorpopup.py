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

from PySide2.QtWidgets import QMessageBox

from spectralUI.backend import error


def error_popup(error_id):
    """Function to display error popup window

    :param error_id: error id

    :return: None
    """
    msg = error.get_error_message(error_id)
    lvl = error.get_error_level(error_id)

    message_box = QMessageBox()
    message_box.setWindowTitle(lvl)
    message_box.setText(msg)
    icon = QMessageBox.Critical if lvl == error.CRITICAL else QMessageBox.Warning
    message_box.setIcon(icon)

    message_box.exec_()

    if lvl == error.CRITICAL:
        sys.exit(1)
