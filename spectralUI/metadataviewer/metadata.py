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

from PySide2.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih
from spectralUI.backend.metadata import get_properties_list


class Metadata(QTableWidget):
    """Metadata Table"""

    def __init__(self):
        super().__init__()

        ih.MDATA_INST = self

        self.setRowCount(7)
        self.setColumnCount(2)
        self.setEditTriggers(self.NoEditTriggers)
        self.setHorizontalHeaderItem(0, QTableWidgetItem("Property"))
        self.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.properties_list = get_properties_list()
        self.len = len(self.properties_list)

        for i in range(self.len):
            self.setItem(i, 0, QTableWidgetItem(self.properties_list[i]))
        self.setItem(self.len, 0, QTableWidgetItem("Current Wavelength (nm)"))

    def update_table(self, metadata, current_band=0):
        """Update table with new metadata

        :param metadata: new metadata
        :param current_band: current band of spectral image (default 0)

        :return: None
        """
        for i in range(self.len):
            self.setItem(i, 1, QTableWidgetItem(metadata[i]))
        current_wavelength = cv.WAVELENGTH_LIST[current_band]
        self.setItem(self.len, 1, QTableWidgetItem(str(current_wavelength)))
