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

from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih

matplotlib.use("Qt5Agg")


class ColorImage(FigureCanvasQTAgg):
    """sRGB color image canvas"""

    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        self.axes.set_frame_on(False)
        self.axes.set_xticks([])
        self.axes.set_yticks([])
        super().__init__(self.fig)

        ih.CLR_IMG_INST = self

        self.cax = None

    def update_canvas(self):
        """Updated sRGB color image canvas"""
        self.axes.clear()

        image = cv.COLOR_IMAGE

        if image.shape[0] > image.shape[1]:
            image = np.rot90(image)

        self.cax = self.axes.imshow(image)
        self.draw()
