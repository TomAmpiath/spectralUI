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
from PySide2.QtWidgets import QSplitter, QVBoxLayout, QWidget

from spectralUI.imageviewer.imageviewer import ImageViewer
from spectralUI.metadataviewer.metadataviewer import MetadataViewer
from spectralUI.spectralsignatureviewer.spectralsignatureviewer import (
    SpectralSignaureViewer,
)


class MainWidget(QWidget):
    """Main widget"""

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.splitter_horizontal = QSplitter(Qt.Horizontal)
        self.splitter_horizontal.setSizes([200, 200])
        self.splitter_vertical = QSplitter(Qt.Vertical)
        self.splitter_vertical.setSizes([200, 200])

        self.image_viewer = ImageViewer()
        self.metadata_viewer = MetadataViewer()
        self.spectral_signature_viewer = SpectralSignaureViewer()

        self.splitter_horizontal.addWidget(self.image_viewer)
        self.splitter_horizontal.addWidget(self.metadata_viewer)

        self.splitter_vertical.addWidget(self.splitter_horizontal)
        self.splitter_vertical.addWidget(self.spectral_signature_viewer)

        self.layout.addWidget(self.splitter_vertical)

        self.setLayout(self.layout)
