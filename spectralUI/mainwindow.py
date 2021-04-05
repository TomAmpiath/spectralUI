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

import os

from PySide2.QtCore import QSettings
from PySide2.QtGui import QCloseEvent, QIcon
from PySide2.QtWidgets import QAction, QMainWindow, QMessageBox

import spectralUI
from spectralUI import instancehandler as ih
from spectralUI import variabledefintions as vd


class MainWindow(QMainWindow):
    """Application main window"""

    def __init__(self):
        super().__init__()

        self.settings = QSettings()

        # reset window size and position to last used values
        try:
            self.resize(self.settings.value("window size"))
            self.move(self.settings.value("window position"))
        except:
            pass

        self.setWindowTitle(spectralUI.__application_name__)
        self.setMinimumSize(vd.MIN_WINDOW_WIDTH, vd.MIN_WINDOW_HEIGTH)

        icon_path = os.path.join(
            spectralUI.basedir, os.pardir, "resources", "icons", "application_icon.png"
        )
        self.setWindowIcon(QIcon(icon_path))

        self.init_menu()

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
        self.exit_action.triggered.connect(self.close)

        self.about_action.triggered.connect(self.display_about)
        self.about_qt_action.triggered.connect(ih.APP_INST.aboutQt)

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

    def closeEvent(self, event: QCloseEvent) -> None:
        """Actions to perform on window close

        :param event: triggering event

        :return: None
        """
        # store current size and position of window
        self.settings.setValue("window size", self.size())
        self.settings.setValue("window position", self.pos())
