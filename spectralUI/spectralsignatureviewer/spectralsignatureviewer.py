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

from PySide2.QtWidgets import QGroupBox, QVBoxLayout

from spectralUI.spectralsignatureviewer.spectralsignature import SpectralSignature


class SpectralSignaureViewer(QGroupBox):
    """Spectral signature viewer"""

    def __init__(self):
        super().__init__()

        self.setTitle("Spectral Signature")

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.spectral_signature = SpectralSignature()

        self.layout.addWidget(self.spectral_signature)

        self.setLayout(self.layout)
