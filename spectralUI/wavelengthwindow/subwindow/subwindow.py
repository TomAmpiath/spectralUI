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

from PySide2.QtWidgets import (
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
)

from spectralUI import cachedvariables as cv
from spectralUI.wavelengthwindow.subwindow.wavelengthgrid import WavelengthGrid


class SubWindow(QDialog):
    """Dialog window to ask if they want to read wavelength list from a file / manually enter data"""

    def __init__(self):
        super().__init__()

        self.setModal(True)
        self.setWindowTitle("Choose an Option")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(
            "Choose whether to read the list of wavelengths from a file or manually enter them."
        )
        self.layout.addWidget(self.label)

        self.sub_layout = QHBoxLayout()
        self.read_from_file_button = QPushButton("Read From File")
        self.manually_enter_button = QPushButton("Manually Enter")

        self.read_from_file_button.clicked.connect(
            self.on_clicked_read_from_file_button
        )
        self.manually_enter_button.clicked.connect(
            self.on_clicked_manually_enter_button
        )

        self.sub_layout.addWidget(self.read_from_file_button)
        self.sub_layout.addWidget(self.manually_enter_button)

        self.layout.addLayout(self.sub_layout)

    def on_clicked_read_from_file_button(self):
        """Actions to be performed on button click"""
        file_name, _ = QFileDialog.getOpenFileName(
            None, "Select file containing wavelength list", "", "List File (*.txt)"
        )
        if file_name:
            f = open(file_name)
            contents = f.read()
            wl = contents.split(",")
            f.close()
            wavelenght_list = [float(w) for w in wl]
            cv.WAVELENGTH_LIST = wavelenght_list
            self.done(1)

    def on_clicked_manually_enter_button(self):
        """Actions to be performed on button click"""
        self.hide()
        wavelength_grid = WavelengthGrid
        wavelength_grid.exec()
        if wavelength_grid.result() == 1:
            self.done(1)
        else:
            self.show()
