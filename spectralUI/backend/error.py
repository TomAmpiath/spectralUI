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

import sys

# Error Levels
CRITICAL, WARNING, INFO = range(3)

ERROR_RANGE = 5

# Error IDs
(
    NO_ERROR,
    FILE_NOT_FOUND,
    NO_SPECTRAL_DATA,
    UNKNOWN_FORMAT,
    ERROR_ERROR,
) = range(ERROR_RANGE)

# dict -> error id: (error message, error level)
error_dict = {
    FILE_NOT_FOUND: ("File Not Found", CRITICAL),
    NO_SPECTRAL_DATA: ("No Spectral Data Found in Input File", WARNING),
    UNKNOWN_FORMAT: ("Unknown File Format.", WARNING),
    ERROR_ERROR: ("Unknown Error ID", CRITICAL),
}


def get_error_message(error_id):
    """Get error message corresponding to error_id

    :param error_id: error id

    :return: message corresponding to error_id
    """
    if error_id not in range(ERROR_RANGE):
        sys.exit(ERROR_ERROR)
    return error_dict[error_id][0]


def get_error_level(error_id):
    """Get error level corresponding to error_id

    :param error_id: error id

    :return: error level corresponding to error_id
    """
    if error_id not in range(ERROR_RANGE):
        sys.exit(ERROR_ERROR)
    return error_dict[error_id][1]
