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

import numpy as np
from scipy.io import loadmat

from spectralUI import cachedvariables as cv
from spectralUI.backend import error


def load_mat_file(file):
    """Load spectral data from .mat file

    :param file: input file name

    :return: error code
    """
    try:
        mat_file = loadmat(file)
    except:
        return error.FILE_NOT_FOUND

    var_name = ""
    wl = None

    # obtain spectral data
    for key in mat_file:
        value = mat_file[key]
        if isinstance(value, np.ndarray) and len(value.shape) == 3:
            var_name = key
            break

    if var_name == "":
        return error.NO_SPECTRAL_DATA

    # obtain wave length list, if present
    for key in mat_file:
        value = mat_file[key]
        if isinstance(value, np.ndarray) and len(value.shape) == 2:
            if value.shape == (mat_file[var_name].shape[2], 1):
                wl = key
                break
        if isinstance(value, np.ndarray) and len(value.shape) == 1:
            if len(value) == mat_file[var_name].shape[2]:
                wl = key
                break

    cv.DATACUBE = mat_file[var_name]
    if wl is not None:
        cv.WAVELENGTH_LIST = np.squeeze(mat_file[wl]).tolist()
    else:
        cv.WAVELENGTH_LIST = None

    return error.NO_ERROR
