# Youtube_Downloader

A simple command-line tool to download YouTube videos or entire playlists.

## Prerequisites

- Python 3

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/Bardia0/Youtube_Downloader.git
   cd Youtube_Downloader
   ```
## How to download a single YouTube video

   ```bash
   python3 youtube_downloader.py --quality 720 <youtube-video-url>
   ```
## How to download an entire YouTube playlist

   ```bash
   python3 youtube_downloader.py --playlist <youtube-playlist-url>
   ```
   the playlist url should be as below
   ```
   https://youtube.com/playlist?<some-queries>
   ```
## For more information to use command

use help option as below

   ```bash
   python3 youtube_downloader.py --help
   ```
the options are

   ```--quality``` or ```-q```: to Specify video quality (e.g., 720)
   
and

   ```--playlist``` or ```-p```: to download entire YouTube playlist
