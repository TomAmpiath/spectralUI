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

from PySide2.QtCore import Qt
from PySide2.QtGui import QDoubleValidator
from PySide2.QtWidgets import (
    QDialog,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from spectralUI import cachedvariables as cv


class UniformWavelength(QDialog):
    """Dialog window to get starting and ending wavelength from user"""

    def __init__(self):
        super().__init__()

        self.setModal(True)
        self.setWindowTitle("Enter wavelength")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.sub_layout = QGridLayout()

        self.layout.addLayout(self.sub_layout)

        validator = QDoubleValidator()

        self.label_starting = QLabel("Starting wavelength")
        self.starting_wavelength = QLineEdit()
        self.starting_wavelength.textChanged.connect(self.on_text_changed)
        self.starting_wavelength.setValidator(validator)
        self.sub_layout.addWidget(self.label_starting, 0, 0)
        self.sub_layout.addWidget(self.starting_wavelength, 0, 1)

        self.label_ending = QLabel("Ending Wavelength")
        self.ending_wavelength = QLineEdit()
        self.ending_wavelength.textChanged.connect(self.on_text_changed)
        self.ending_wavelength.setValidator(validator)
        self.sub_layout.addWidget(self.label_ending, 1, 0)
        self.sub_layout.addWidget(self.ending_wavelength, 1, 1)

        self.button_proceed = QPushButton("Proceed")
        self.button_proceed.setEnabled(False)
        self.button_proceed.clicked.connect(self.on_proceed)
        self.layout.addWidget(self.button_proceed, alignment=Qt.AlignCenter)

    def on_text_changed(self):
        """Actions to be performed on text changed"""
        self.button_proceed.setEnabled(
            bool(self.starting_wavelength.text())
            and bool(self.ending_wavelength.text())
        )

    def on_proceed(self):
        """Actions to be performed on button press"""
        wavelength_list = []
        start = float(self.starting_wavelength.text())
        end = float(self.ending_wavelength.text()) + 1
        number_of_bands = cv.DATACUBE.shape[2]
        increment_factor = (end - start) / number_of_bands

        i = start
        while i <= end:
            wavelength_list.append(i)
            i += increment_factor

        cv.WAVELENGTH_LIST = wavelength_list
        self.done(1)
