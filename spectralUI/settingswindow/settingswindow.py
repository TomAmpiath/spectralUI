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

from matplotlib import pyplot as plt
from PySide2.QtCore import QSettings
from PySide2.QtWidgets import (
    QComboBox,
    QDialog,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QStyleFactory,
    QVBoxLayout,
)

from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih
from spectralUI import variabledefintions as vd
from spectralUI.settingswindow.cmappreview import CmapPreview


class SettingsWindow(QDialog):
    """Settings window"""

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.settings = QSettings("spectralUI", "spectralUI Prototype")

        self.setWindowTitle("Settings")
        self.setMinimumSize(400, 300)

        self.layout = QVBoxLayout()

        self.horizontal_layout_1 = QHBoxLayout()
        self.horizontal_layout_2 = QHBoxLayout()
        self.horizontal_layout_x = QHBoxLayout()

        self.label_cmap = QLabel("Change color map")
        self.combobox_cmap = QComboBox()
        self.load_cmaps()
        self.combobox_cmap.setCurrentText(cv.CURRENT_CMAP)
        self.combobox_cmap.currentIndexChanged.connect(self.update_cmap_preview)

        self.horizontal_layout_1.addWidget(self.label_cmap)
        self.horizontal_layout_1.addWidget(self.combobox_cmap)

        self.cmap_preview = CmapPreview()

        self.label_style = QLabel("Change window style")
        self.combobox_style = QComboBox()
        self.load_styles()
        self.combobox_style.setCurrentText(cv.CURRENT_STYLE)
        self.combobox_style.currentTextChanged.connect(self.update_style)

        self.horizontal_layout_2.addWidget(self.label_style)
        self.horizontal_layout_2.addWidget(self.combobox_style)

        self.button_cancel = QPushButton("Cancel")
        self.button_cancel.clicked.connect(self.exit_actions)
        self.button_default = QPushButton("Reset to Default")
        self.button_default.clicked.connect(self.reset_to_default)
        self.button_ok = QPushButton("Ok")
        self.button_ok.clicked.connect(self.update_settings)

        self.horizontal_layout_x.addWidget(self.button_cancel)
        self.horizontal_layout_x.addWidget(self.button_default)
        self.horizontal_layout_x.addWidget(self.button_ok)

        self.layout.addLayout(self.horizontal_layout_1)
        self.layout.addWidget(self.cmap_preview)
        self.layout.addLayout(self.horizontal_layout_2)
        self.layout.addLayout(self.horizontal_layout_x)

        self.setLayout(self.layout)

    def load_styles(self):
        """Load all available UI styles"""
        self.combobox_style.clear()
        for style in QStyleFactory.keys():
            self.combobox_style.addItem(style.lower())

    def update_cmap_preview(self):
        """Update the cmap preview canvas"""
        cv.CURRENT_CMAP = self.combobox_cmap.currentText()
        self.cmap_preview.update_canvas()

    def update_style(self):
        """Update the app UI style"""
        cv.CURRENT_STYLE = self.combobox_style.currentText()
        ih.APP_INST.setStyle(cv.CURRENT_STYLE)

    def load_cmaps(self):
        """Populate cmap combobox with all available cmaps"""
        self.combobox_cmap.clear()
        for color_map in plt.colormaps():
            self.combobox_cmap.addItem(color_map)

    def exit_actions(self):
        """Handle actions to be performed on exit"""
        cv.CURRENT_CMAP = self.settings.value("color map")
        cv.CURRENT_STYLE = self.settings.value("style")
        self.close()

    def reset_to_default(self):
        """Handle actions to be performed on reset to default"""
        cv.CURRENT_CMAP = vd.DEFAULT_COLOR_MAP
        cv.CURRENT_STYLE = vd.DEFAULT_STYLE

        self.combobox_cmap.setCurrentText(cv.CURRENT_CMAP)
        self.combobox_style.setCurrentText(cv.CURRENT_STYLE)
        self.update_settings()

    def update_settings(self):
        """Update user settings"""
        self.settings.setValue("color map", cv.CURRENT_CMAP)
        self.settings.setValue("style", cv.CURRENT_STYLE)

        ih.APP_INST.setStyle(self.settings.value("style"))

        if cv.CURRENT_IMAGE is not None:
            spectral_image_canvas = ih.SPCTRL_IMG_INST
            spectral_image_canvas.update_canvas()
            spectral_image_canvas.update_colorbar()

        self.done(1)
