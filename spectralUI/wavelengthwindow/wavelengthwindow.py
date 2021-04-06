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

from PySide2.QtWidgets import QDialog, QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from spectralUI import instancehandler as ih
from spectralUI.wavelengthwindow.subwindow.subwindow import SubWindow
from spectralUI.wavelengthwindow.uniformwavelength import UniformWavelength


class WavelengthWindow(QDialog):
    """Dialog Window to take user input regarding wavelength list"""

    def __init__(self):
        super().__init__()

        self.setModal(True)

        self.setWindowTitle("Choose")
        ih.WAVE_WIN = self

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.sub_layout = QHBoxLayout()

        self.label = QLabel(
            "Is wavelength increasing uniformally across each successive band?"
        )
        self.layout.addWidget(self.label)

        self.yes_button = QPushButton("Yes")
        self.sub_layout.addWidget(self.yes_button)
        self.no_button = QPushButton("No")
        self.sub_layout.addWidget(self.no_button)

        self.yes_button.clicked.connect(self.on_yes)
        self.no_button.clicked.connect(self.on_no)

        self.layout.addLayout(self.sub_layout)

    def on_yes(self):
        """Actions to be performed when user has selected Yes"""
        self.hide()
        uniform_wavelength = UniformWavelength()
        uniform_wavelength.exec()
        if uniform_wavelength.result() == 1:
            self.done(1)
        else:
            self.show()

    def on_no(self):
        """Actions to be performed when user has selected No"""
        self.hide()
        sub_window = SubWindow()
        sub_window.exec()
        if sub_window.result() == 1:
            self.done(1)
        else:
            self.show()
