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

from numpy import amax, amin, mean

from spectralUI import cachedvariables as cv

properties_list = [
    "Height",
    "Width",
    "No: of Bands",
    "Max. Intensity of Current Band",
    "Min. Intensity of Current Band",
    "Mean Intensity of Current Band",
]


def get_properties_list():
    """Returns the list of properties"""
    return properties_list


def get_metadata(band_number=0):
    """Returns a dictionary containing metadata or error code if any error occurs.

    :param band_number: current band number (default 0)

    :return: metadata dictionary
    """
    datacube = cv.DATACUBE
    metadata = [
        str(datacube.shape[0]),
        str(datacube.shape[1]),
        str(datacube.shape[2]),
        str(amax(datacube[:, :, band_number])),
        str(amin(datacube[:, :, band_number])),
        str(mean(datacube[:, :, band_number])),
    ]

    return metadata
