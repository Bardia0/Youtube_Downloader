# Youtube_Downloader

A simple command-line tool to download YouTube videos or entire playlists.

## Prerequisites

- Python 3
- pytube
- 
  ```bash
  pip install pytube```

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Bardia0/Youtube_Downloader.git
   cd Youtube_Downloader
   ```
## How to download a single YouTube video

   ```bash
   python3 youtube_downloader.py <youtube-video-url>
   ```
## Download a single YouTube video with an specific quality
   ```bash
   python3 youtube_downloader.py --quality 720 <youtube-video-url>
   ```
## How to download an entire YouTube playlist

   ```bash
   python3 youtube_downloader.py --playlist "<youtube-playlist-url>"
   ```
   Notice that the playlist url should be something like below
   ```
   https://youtube.com/playlist?list=<some-queries>
   ```
   or
   ```
   https://www.youtube.com/playlist?list=<some-queries>
   ```
   
## For more information about using the command

use help option as below

   ```bash
   python3 youtube_downloader.py --help
   ```
the options are

   ```--quality``` or ```-q```: to Specify video quality (e.g., 720)
   
and

   ```--playlist``` or ```-p```: to download entire YouTube playlist
