# Google Image Downloader

> A simple script that fetches images from Google with browser simulation.

## Pre-requisites

The following Python packages are required to run the script.

- selenium
- requests
- fake_useragent
- beautifulsoup4
- lxml

You can install them via `pip install -r requirements.txt`. You also need install the ChromeDriver
for selenium to work. Please refer to [here](https://sites.google.com/a/chromium.org/chromedriver/getting-started)
on how to install it.

## Usage

```
usage: download_images.py [-h] [--worker WORKER] keyword

positional arguments:
  keyword          the keyword to search

optional arguments:
  -h, --help       show this help message and exit
  --worker WORKER  the number of workers used for downloading images
```

## Disclaimer

This script is written for the purpose of practicing programming skills. Use it at your own discretion.
