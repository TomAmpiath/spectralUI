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

from PySide2.QtWidgets import QComboBox, QHBoxLayout, QLabel

from spectralUI import instancehandler as ih


class SpectralImageNavbar(QHBoxLayout):
    """Navbar for spectral image viewer"""

    def __init__(self):
        super().__init__()

        ih.SPCTRL_IMG_NAV_INST = self

        self.label_select_band = QLabel("Select band : ")
        self.band_selection_combobox = QComboBox()

        self.insertStretch(0, 10)
        self.addWidget(self.label_select_band)
        self.addWidget(self.band_selection_combobox)

        self.band_selection_combobox.currentIndexChanged.connect(self.change_band)

    def change_band(self):
        """Actions to perform when band number is changed"""
        main_window = ih.MAIN_WIN
        main_window.update_data(band_number=self.band_selection_combobox.currentIndex())
