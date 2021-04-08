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

import tempfile

import numpy as np
import vtk
from matplotlib import pyplot as plt

from spectralUI import cachedvariables as cv



def get_cube_textures():
    """Function to get textures for the 3D spectral cube"""
    # saving texture image for top of the cube | +Y
    datacube = cv.DATACUBE
    color_image = cv.COLOR_IMAGE
    
    # store textures to temporary directory
    with tempfile.TemporaryDirectory() as tempdir:
        plt.imsave(tempdir + "/top.png", color_image)

        plt.set_cmap("jet")

        # bottom of the cube. | -Y
        bottom = datacube[:, :, -1]
        plt.imsave(tempdir + "/bottom.png", bottom)

        # front of the cube. | +Z
        front = np.rot90(datacube[-1, :, :])
        plt.imsave(tempdir + "/front.png", front)

        # back of the cube. | -Z
        back = np.rot90(datacube[0, :, :])
        plt.imsave(tempdir + "/back.png", back)

        # left of the cube. | -X
        left = datacube[:, 0, :]
        plt.imsave(tempdir + "/left.png", left)

        # right of the cube. | +X
        right = datacube[:, -1, :]
        plt.imsave(tempdir + "/right.png", right)

        texture_list = []

        image_list = [
            "top.png",
            "bottom.png",
            "front.png",
            "back.png",
            "left.png",
            "right.png",
        ]

        for i in range(6):
            image_reader = vtk.vtkPNGReader()
            image_reader.SetFileName(tempdir + "/" + image_list[i])
            image_reader.Update()

            texture = vtk.vtkTexture()
            texture.SetInputConnection(image_reader.GetOutputPort())
            texture.InterpolateOn()
            texture_list.append(texture)

    # temporary directory gets deleted

    return texture_list
