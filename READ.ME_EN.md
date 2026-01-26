# Simple QR Code Generator

## Overview
A simple web service built with FastAPI. Users can upload images, and the service generates QR codes for each image. Scanning the QR code allows direct access to the image. QR codes have been tested on WeChat and QQ, and both work reliably.

## Features
- Upload images to automatically generate QR codes
- QR codes are compatible with WeChat and QQ scanning
- Hosted on GitHub Pages for stable access
- Supports PNG, JPG, JPEG, and GIF formats

## Project Structure

.
├── uploads/ # Uploaded images
├── qrcodes/ # Generated QR codes
├── code.py # FastAPI main application
├── generate_qr.py # Script to generate QR codes for latest uploads
└── README.md

## Usage
1. Clone the repository:
```bash
git clone https://github.com/O2/Simple-QR-code-generator.git

2. Install dependencies:
pip install fastapi uvicorn qrcode pillow

3. Run the service:
python code.py

4. Generate QR codes for images:
·Upload images via the local endpoint: http://127.0.0.1:8000/upload
·Or run generate_qr.py to generate a QR code for the latest uploaded image

5. Access via GitHub Pages:
·Example image URL: https://your_username.github.io/Simple-QR-code-generator/uploads/your_image.jpg
·Example QR code URL: https://your_username.github.io/Simple-QR-code-generator/qrcodes/your_qr.png

Notes:
·Make sure QR codes point to the public GitHub Pages URL, not local IP addresses
·Both WeChat and QQ can scan the QR codes, though some QQ versions may have issues opening direct image URLs; wrapping images in an HTML page is recommended