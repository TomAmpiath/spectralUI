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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectralUI.  If not, see <http://www.gnu.org/licenses/>.

from spectralUI.backend.spectral2rgb.converter import spectral2rgb
from spectralUI import variabledefintions as vd

def get_color_image():
    """Get sRGB color image for the spectral image"""
    illuminant = vd.DEFAULT_ILLUMINANT
    cie_standard_observer_year = vd.DEFAULT_OBSERVER
    threshold = vd.DEFAULT_THRESHOLD

    color_image = spectral2rgb(illuminant, cie_standard_observer_year, threshold)

    return color_image