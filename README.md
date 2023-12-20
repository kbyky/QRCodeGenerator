<div align="center">

<img src=./assets/title.png>

</div>

<br>

***QR Code Generator*** provides the way to create a QR Code on your local mac or PC.

<br>

<div align="center">

<img src=./assets/how-to-use.gif>

</div>

## How to build

```:shell
pip install poetry
cd ./qr-code-generator
poetry install
poetry run flet pack qrcodegen/cli.py -n QRCodeGenerator --icon assets/favicon.png
```