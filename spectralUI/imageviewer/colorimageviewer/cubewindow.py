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

import vtk
from PySide2.QtWidgets import QDialog, QVBoxLayout
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from spectralUI import cachedvariables as cv
from spectralUI.backend.processdata.cubetextures import get_cube_textures


class CubeWindow(QDialog):
    """Spectral Cube window"""

    def __init__(self):
        super().__init__()
        self.setModal(True)

        self.setWindowTitle("Spectral Cube")
        self.setMinimumSize(600, 600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.renWinInteractor = QVTKRenderWindowInteractor()
        self.layout.addWidget(self.renWinInteractor)

        self.setLayout(self.layout)

        self.renderer = vtk.vtkRenderer()
        self.renWinInteractor.GetRenderWindow().AddRenderer(self.renderer)
        interactor = self.renWinInteractor.GetRenderWindow().GetInteractor()

        datacube = cv.DATACUBE

        dim1, dim2, dim3 = datacube.shape
        if dim1 > dim2:
            dim1, dim2 = dim2, dim1

        texture_list = get_cube_textures()

        top = vtk.vtkPlaneSource()
        bottom = vtk.vtkPlaneSource()
        front = vtk.vtkPlaneSource()
        back = vtk.vtkPlaneSource()
        left = vtk.vtkPlaneSource()
        right = vtk.vtkPlaneSource()

        plane_list = [top, bottom, front, back, left, right]

        top.SetResolution(dim1, dim2)
        top.SetOrigin(0.0, 0.0, 0.0)
        top.SetPoint1(dim1, 0.0, 0.0)
        top.SetPoint2(0.0, 0.0, -1 * dim2)

        bottom.SetResolution(dim1, dim2)
        bottom.SetOrigin(0.0, -1 * dim3, 0.0)
        bottom.SetPoint1(dim1, -1 * dim3, 0.0)
        bottom.SetPoint2(0.0, -1 * dim3, -1 * dim2)

        front.SetResolution(dim1, dim3)
        front.SetOrigin(0.0, 0.0, 0.0)
        front.SetPoint1(dim1, 0.0, 0.0)
        front.SetPoint2(0.0, -1 * dim3, 0.0)

        back.SetResolution(dim1, dim3)
        back.SetOrigin(0.0, 0.0, -1 * dim2)
        back.SetPoint1(dim1, 0.0, -1 * dim2)
        back.SetPoint2(0.0, -1 * dim3, -1 * dim2)

        left.SetResolution(dim3, dim2)
        left.SetOrigin(0.0, 0.0, 0.0)
        left.SetPoint1(0.0, -1 * dim3, 0.0)
        left.SetPoint2(0.0, 0.0, -1 * dim2)

        right.SetResolution(dim3, dim2)
        right.SetOrigin(dim1, 0.0, 0.0)
        right.SetPoint1(dim1, -1 * dim3, 0.0)
        right.SetPoint2(dim1, 0.0, -1 * dim2)

        actor_list = []

        for i in range(len(plane_list)):
            mapper = vtk.vtkPolyDataMapper()
            mapper.SetInputConnection(plane_list[i].GetOutputPort())

            actor = vtk.vtkActor()
            actor.SetMapper(mapper)
            actor.SetTexture(texture_list[i])
            actor_list.append(actor)

        for actor in actor_list:
            self.renderer.AddActor(actor)

        self.renderer.ResetCamera()
        self.renderer.GetActiveCamera().Azimuth(30)
        self.renderer.GetActiveCamera().Elevation(30)

        interactor.Initialize()
        interactor.Start()

    def closeEvent(self, event):
        """Actions to be done on closing the window

        :param event: event that triggered closeEvent

        :return: None
        """
        self.renWinInteractor.Finalize()
