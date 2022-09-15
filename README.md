# spectralUI Prototype <img src="./resources/icons/application_icon.png" width="24">

spectralUI is an open source cross platform, general purpose tool for analyzing multispectral and hyperspectral images.

## Screenshots

#### Main Screen
<img src="./screenshots/screenshot_main_screen.PNG" width=50%/>

#### Color Image
<img src="./screenshots/screenshot_color_image.PNG" width=50%/>

#### 3D Cube
<img src="./screenshots/screenshot_cube.PNG" width=50%/>

## Requirements

* Python 3.8.5
* OpenGL supported graphics card
* Windows / Linux / Mac OS

## Installation

Clone the repository and cd into it
```bash
git clone https://www.github.com/TomAmpiath/spectralUI_Prototype
cd spectralUI_Prototype
```

Create a virtual environment using:
```bash
python -m venv venv
```

On Windows:
```commandline
\venv\Scripts\activate
```

On Linux & Mac OS:
```bash
. ./venv/bin/activate
```

Install required packages:
```bash
pip install -r requirements.txt
```

Run the application using:
```bash
python -m spectralUI
```

## Features

* Load .mat files
* Display the spectral image in each band
* Generate sRGB color image from spectral data cube
* Display 3D spectral cube
* User's can manually enter wavelength or read it from a file
* Display metadata in a table
* Plot & Compare spectral signature at different pixel positions
* Change color maps and application theme
