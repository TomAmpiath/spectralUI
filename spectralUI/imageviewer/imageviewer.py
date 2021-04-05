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

from PySide2.QtWidgets import QTabWidget

from spectralUI.imageviewer.colorimageviewer.colorimageviewer import ColorImageViewer
from spectralUI.imageviewer.spectralimageviewer.spectralimageviewer import (
    SpectralImageViewer,
)


class ImageViewer(QTabWidget):
    """Image Viewer"""

    def __init__(self):
        super().__init__()

        self.spectral_image_viewer = SpectralImageViewer()
        self.color_image_viewer = ColorImageViewer()

        self.addTab(self.spectral_image_viewer, "Spectral Image")
        self.addTab(self.color_image_viewer, "sRGB Color Image and 3D cube")
