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

import matplotlib
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")

from PySide2.QtCore import QSettings

from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih


class SpectralImage(FigureCanvasQTAgg):
    """Spectral image canvas"""

    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

        ih.SPCTRL_IMG_INST = self

        self.cbar = None
        self.cax = None

    def update_canvas(self):
        """Update spectral image canvas"""
        image = cv.CURRENT_IMAGE

        self.axes.clear()

        cv.ROTATION_FLAG = False

        if image.shape[0] > image.shape[1]:
            image = np.rot90(image)
            cv.ROTATION_FLAG = True

        self.settings = QSettings("spectralUI", "spectralUI Prototype")

        self.cax = self.axes.imshow(image, cmap=self.settings.value("color map"))
        self.draw()

        spectral_signature = ih.SPCTRL_SIG_INST
        uc = spectral_signature.update_canvas
        self.mpl_connect("button_press_event", uc)

    def update_colorbar(self):
        """Update colorbar"""
        if self.cbar is not None:
            self.cbar.remove()

        cbar_orientation = "horizontal" if cv.ROTATION_FLAG else "vertical"

        self.cbar = self.fig.colorbar(self.cax, orientation=cbar_orientation)
        self.draw_idle()
