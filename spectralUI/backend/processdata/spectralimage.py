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

from spectralUI import cachedvariables as cv


def get_spectral_image(band_number=0):
    """Function to get spectral image at given band number

    :param band_number: band number (default 0)

    :return: None
    """
    spectral_image = cv.DATACUBE[:, :, band_number]
    cv.CURRENT_IMAGE = spectral_image
