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

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih


class SpectralSignature(FigureCanvasQTAgg):
    """Spectral signature canvas"""

    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

        ih.SPCTRL_SIG_INST = self

        self.legends_list = []
        self.count = 0

    def clear_canvas(self):
        """Clear spectral signature canvas"""
        self.axes.clear()
        self.legends_list = []
        self.count = 0

    def update_canvas(self, event):
        """Update canvas when event occurs

        :param event: event that triggers update_canvas

        :return: None
        """
        if event.xdata is None or event.ydata is None:
            return

        datacube = cv.DATACUBE

        if cv.ROTATION_FLAG:
            x_coordinate, y_coordinate = int(event.ydata), int(event.xdata)
        else:
            x_coordinate, y_coordinate = int(event.xdata), int(event.ydata)

        if self.count == 4:
            self.clear_canvas()

        self.axes.set_xlim(0, datacube.shape[2])

        self.axes.plot(
            [
                datacube[y_coordinate, x_coordinate, band]
                for band in range(0, datacube.shape[2])
            ]
        )

        legend = str((x_coordinate, y_coordinate))
        self.legends_list.append(legend)
        self.axes.legend(self.legends_list)

        self.count += 1

        self.draw()
