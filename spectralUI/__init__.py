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

import os.path

basedir = os.path.dirname(os.path.realpath(__file__))

__author__ = "Tom George Ampiath"
__license__ = "GPL3"
__maintainer__ = __author__
__version__ = "0.0.1"
__name__ = "spectralUI"
__application_name__ = "spectralUI Qt"
__version_info__ = tuple(int(part) for part in __version__.split("."))
__description__ = (
    "An open-source cross-platform general purpose tool for analyzing multispectral and hyperspectral images"
)