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
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QWidget

from spectralUI import instancehandler as ih
from spectralUI.imageviewer.colorimageviewer.colorimage import ColorImage
from spectralUI.imageviewer.colorimageviewer.cubewindow import CubeWindow


class ColorImageViewer(QWidget):
    """Layout for sRGB color image viewer"""

    def __init__(self):
        super().__init__()

        ih.CLR_IMG_VIEW_INST = self

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.color_image = ColorImage()
        self.open_viewer_button = QPushButton("View 3D spectral cube")
        self.open_viewer_button.setEnabled(False)

        self.open_viewer_button.clicked.connect(self.open_viewer)

        self.layout.addWidget(self.color_image)
        self.layout.addWidget(self.open_viewer_button, alignment=Qt.AlignRight)

        self.setLayout(self.layout)

    def open_viewer(self):
        """Open spectral cube viewer window"""
        self.cube_window = CubeWindow()
        self.cube_window.exec_()
