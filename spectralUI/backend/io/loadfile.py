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

import os

from spectralUI.backend import error
from spectralUI.backend.io.loadmatfile import load_mat_file


def load_file(file):
    """Load spectral data from input file

    :param file: input spectral file

    :return: error code
    """
    if not os.path.isfile(file):
        return error.FILE_NOT_FOUND

    file_name, file_extension = os.path.splitext(file)

    if file_extension == ".mat":
        return load_mat_file(file)
    else:
        return error.UNKNOWN_FORMAT
