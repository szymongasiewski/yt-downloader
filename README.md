# YouTube Video and Audio Downloader

## Description
Python script that downloads YouTube video and audio.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/your-username/yt-downloader.git
    ```
2. Install required dependencies:
    ```shell
    pip install -r requirements.txt
    ```


## Usage
```shell
python3 downloader.py <url_to_video> <optional_destination> [OPTIONS]
```
### Options
- `-a, --audio`: Download the audio only, ignoring video content

## Example
```shell
pyhon3 downloader.py https://www.youtube.com/watch?v=d0wnl04d3r /path/to/destination -a