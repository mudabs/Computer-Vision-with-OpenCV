# Computer Vision with OpenCV Demos

Repository of small OpenCV-based examples and utilities following Filipe's computer vision tutorials.

## Overview

This collection contains standalone Python scripts demonstrating common computer vision tasks using OpenCV, such as image I/O, video and webcam handling, resizing, cropping, blurring, color spaces, thresholding, edge detection, drawing, and contours.

## Repository structure

- [io_image.py](io_image.py) — load and save images
- [io_video.py](io_video.py) — read/write video files
- [io_webcam.py](io_webcam.py) — capture from webcam
- [resizing.py](resizing.py) — image resizing examples
- [crop.py](crop.py) — image cropping utilities
- [image bluring/imageblurring.py](image%20bluring/imageblurring.py) — blurring examples
- [color spaces/colorspaces.py](color%20spaces/colorspaces.py) — convert between color spaces
- [thresholding/adaptive_thresholding.py](thresholding/adaptive_thresholding.py) — adaptive thresholding
- [thresholding/global_thresholding.py](thresholding/global_thresholding.py) — global thresholding
- [edge detection/edge.py](edge%20detection/edge.py) — edge detection filters
- [Drawing/main.py](Drawing/main.py) — drawing primitives and text
- [Contours/main.py](Contours/main.py) — contour detection and processing
- [Color Detection/main.py](Color%20Detection/main.py) — color detection demo
- [Color Detection/util.py](Color%20Detection/util.py) — helper functions for color detection
- `data/` — sample images and outputs

> Note: Some folder names contain spaces; use quotes when running paths on the command line.

## Requirements

- Python 3.8 or newer
- OpenCV and NumPy

Install with pip:

```powershell
python -m pip install --upgrade pip
python -m pip install opencv-python numpy
```

If you prefer a single requirements file, create `requirements.txt` with:

```
opencv-python
numpy
```

and install with:

```powershell
python -m pip install -r requirements.txt
```

## How to run

Run scripts directly with Python. Examples:

```powershell
python io_image.py
python io_video.py
python "Color Detection/main.py"
python "Drawing/main.py"
```

If a script expects arguments (e.g., input file), open the file to see usage comments or modify the script to point at files under `data/`.

## Contributing / Next steps

- Add a `requirements.txt` or `pyproject.toml` for environment reproducibility.
- Optionally create small README files inside subfolders to explain each demo.

If you'd like, I can create a `requirements.txt` and/or add per-folder READMEs.

## License

This repository contains tutorial/demo code; add a license file if you plan to publish or share.
