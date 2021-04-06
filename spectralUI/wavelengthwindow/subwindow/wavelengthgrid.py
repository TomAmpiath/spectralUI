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
from PySide2.QtWidgets import QDialog, QGridLayout, QLineEdit, QPushButton, QVBoxLayout

from spectralUI import cachedvariables as cv


class WavelengthGrid(QDialog):
    """Window for reading wavelength corresponding to each spectral band"""

    def __init__(self):
        super().__init__()

        self.setModal(True)
        self.setWindowTitle("Enter wavelength of each band")

        number_of_bands = cv.DATACUBE.shape[2]

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.line_edit_list = []
        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        row = 0
        column = 0
        for i in range(number_of_bands):
            line_edit = QLineEdit()
            validator = QDoubleValidator()
            line_edit.setValidator(validator)
            line_edit.setPlaceholderText("band " + str(i))
            line_edit.textChanged.connect(self.on_text_changed)
            self.line_edit_list.append(line_edit)
            self.grid_layout.addWidget(line_edit, row, column)
            if column % 9 == 0 and column != 0:
                column = 0
                row += 1
            else:
                column += 1

        self.proceed_button = QPushButton("Proceed")
        self.layout.addWidget(self.proceed_button, alignment=Qt.AlignHCenter)
        self.proceed_button.setEnabled(False)
        self.proceed_button.clicked.connect(self.on_proceed)

    def on_text_changed(self):
        """Actions to be performed on text changed"""
        for line_edit in self.line_edit_list:
            if not bool(line_edit.text()):
                return
        self.proceed_button.setEnabled(True)

    def on_proceed(self):
        """Actions to be performed on button click"""
        wavelength_list = []

        for line_edit in self.line_edit_list:
            wavelength_list.append(float(line_edit.text()))

        cv.WAVELENGTH_LIST = wavelength_list
        self.done(1)
