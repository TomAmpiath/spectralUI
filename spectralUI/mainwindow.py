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

from PySide2.QtCore import QSettings
from PySide2.QtGui import QCloseEvent, QIcon
from PySide2.QtWidgets import (
    QAction,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QStyleFactory,
)

import spectralUI
from spectralUI import cachedvariables as cv
from spectralUI import instancehandler as ih
from spectralUI import variabledefintions as vd
from spectralUI.backend import error
from spectralUI.backend.io.loadfile import load_file
from spectralUI.backend.metadata import get_metadata
from spectralUI.backend.processdata.colorimage import get_color_image
from spectralUI.backend.processdata.spectralimage import get_spectral_image
from spectralUI.errorpopup import error_popup
from spectralUI.mainwidget import MainWidget
from spectralUI.settingswindow.settingswindow import SettingsWindow
from spectralUI.wavelengthwindow.wavelengthwindow import WavelengthWindow


class MainWindow(QMainWindow):
    """Application main window"""

    def __init__(self):
        super().__init__()

        ih.MAIN_WIN = self

        self.settings = QSettings("spectralUI", "spectralUI Prototype")

        # reset window size and position to last used values
        try:
            self.resize(self.settings.value("window size"))
            self.move(self.settings.value("window position"))
        except:
            pass

        # initialize color map and app style if settings does not exist
        vd.DEFAULT_STYLE = QStyleFactory.keys()[0]
        if not self.settings.contains("color map"):
            self.settings.setValue("color map", vd.DEFAULT_COLOR_MAP)
        if not self.settings.contains("style"):
            self.settings.setValue("style", vd.DEFAULT_STYLE)

        cv.CURRENT_CMAP = self.settings.value("color map")
        cv.CURRENT_STYLE = self.settings.value("style")
        ih.APP_INST.setStyle(cv.CURRENT_STYLE)

        self.setWindowTitle(spectralUI.__application_name__)
        self.setMinimumSize(vd.MIN_WINDOW_WIDTH, vd.MIN_WINDOW_HEIGTH)

        icon_path = os.path.join(
            spectralUI.basedir, os.pardir, "resources", "icons", "application_icon.png"
        )
        self.setWindowIcon(QIcon(icon_path))

        self.init_menu()

        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

    def init_menu(self):
        """Initialize menu"""
        self.file_menu = self.menuBar().addMenu("&File")
        self.settings_menu = self.menuBar().addMenu("&Settings")
        self.help_menu = self.menuBar().addMenu("&Help")

        self.open_action = QAction("&Open", self)
        self.open_action.setShortcut("Ctrl+O")
        self.exit_action = QAction("&Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.exit_action)

        self.settings_action = QAction("&Settings", self)
        self.settings_action.setShortcut("Ctrl+P")

        self.settings_menu.addAction(self.settings_action)

        self.about_action = QAction("&About", self)
        self.about_action.setShortcut("Ctrl+A")
        self.about_qt_action = QAction("About &Qt", self)
        self.about_qt_action.setShortcut("Ctrl+B")

        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.about_qt_action)

        # triggers===============================
        self.open_action.triggered.connect(self.open_file)
        self.exit_action.triggered.connect(self.close)

        self.settings_action.triggered.connect(self.open_settings_window)

        self.about_action.triggered.connect(self.display_about)
        self.about_qt_action.triggered.connect(ih.APP_INST.aboutQt)

    def open_file(self):
        """Handle file opening"""
        file, _ = QFileDialog.getOpenFileName(
            None, "Select Spectral Image File", "", "Image File (*.mat)"
        )

        if file:
            self.update_data(file)

    def update_data(self, file=None, band_number=0):
        """Function to update all widgets"""
        datacube = cv.DATACUBE
        if file:
            result = load_file(file)

            if result != error.NO_ERROR:
                error_popup(result)
                return
            else:
                datacube = cv.DATACUBE
                if cv.WAVELENGTH_LIST is None:
                    wavelength_window = WavelengthWindow()
                    wavelength_window.exec_()
                    if wavelength_window.result() == 0:
                        return

            sRGB_image = get_color_image()
            cv.COLOR_IMAGE = sRGB_image

            color_image_canvas = ih.CLR_IMG_INST
            color_image_canvas.update_canvas()

            color_image_viewer = ih.CLR_IMG_VIEW_INST
            color_image_viewer.open_viewer_button.setEnabled(True)

            spectral_image_navbar = ih.SPCTRL_IMG_NAV_INST
            spectral_image_navbar.band_selection_combobox.clear()

            for band in range(0, datacube.shape[2]):
                spectral_image_navbar.band_selection_combobox.addItem(str(band))

            spectral_image_navbar.band_selection_combobox.setCurrentIndex(0)

            spectral_signature_canvas = ih.SPCTRL_SIG_INST
            spectral_signature_canvas.clear_canvas()

        metadata = get_metadata(band_number)
        get_spectral_image(band_number)

        metadata_table = ih.MDATA_INST
        metadata_table.update_table(metadata, band_number)

        spectral_image_canvas = ih.SPCTRL_IMG_INST
        spectral_image_canvas.update_canvas()
        spectral_image_canvas.update_colorbar()

    def open_settings_window(self):
        """Open settings winddow"""
        self.settings_window = SettingsWindow()
        self.settings_window.exec_()
        if self.settings_window.result() == 0:
            cv.CURRENT_STYLE = self.settings.value("style")
            cv.CURRENT_CMAP = self.settings.value("color map")
            ih.APP_INST.setStyle(cv.CURRENT_STYLE)

    def display_about(self):
        """About dialog for application"""
        QMessageBox.about(
            self,
            "About " + spectralUI.__application_name__,
            "<p>"
            "<b>spectralUI</b> is an open-source cross-platform, "
            "general purpose tool for analyzing multispectral and "
            "hyperspectral images."
            "</p>"
            "<p>"
            "" + spectralUI.__application_name__ + ""
            " is not meant for consumer use. This application is "
            "only a prototype and testing ground for spectralUI. For "
            "stable application, go to "
            "<a href='https://www.github.com/TomAmpiath/spectralUI'>spectralUI</a>"
            "</p>"
            "<hl>"
            "<p>"
            "Application version: <b>" + spectralUI.__version__ + "</b>"
            "</p>"
            "<p>"
            "Copyright 2021, Tom George Ampiath, All rights reserved"
            "</p>",
        )

    def closeEvent(self, event: QCloseEvent):
        """Actions to perform on window close

        :param event: triggering event

        :return: None
        """
        # store current size and position of window
        self.settings.setValue("window size", self.size())
        self.settings.setValue("window position", self.pos())
