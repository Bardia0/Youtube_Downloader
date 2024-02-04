import argparse
import os
from pytube import YouTube
from pytube.cli import on_progress
from tqdm import tqdm
import re

def download_video(url, quality=None, playlist=False):
    try:
        # Ensure that the URL is enclosed in double quotes to prevent shell misinterpretation
        url = re.search(r'"(.*?)"', url).group(1) if re.search(r'"(.*?)"', url) else url
        
        yt = YouTube(url, on_progress_callback=on_progress)

        if playlist:
            print("Downloading entire playlist...")
            videos = list(yt.streams.filter(file_extension='mp4'))
        else:
            print("Downloading single video...")
            videos = list(yt.streams.filter(res=quality, file_extension='mp4'))

        if not videos:
            print(f"No {'playlist' if playlist else quality + 'p' if quality else ''} video available for {url}")
            return

        for video in videos:
            print(f"Downloading: {video.title}...")

            video.download(filename=video.title, output_path=os.getcwd())
            print("Download complete!")

            # Exit the loop in single video mode
            if not playlist:
                break

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom YouTube Downloader")
    parser.add_argument("url", help="YouTube video URL or playlist URL")
    parser.add_argument("--quality", "-q", help="Video quality (e.g., 720)")
    parser.add_argument("--playlist", "-p", action="store_true", help="Download entire YouTube playlist")

    args = parser.parse_args()
    download_video(args.url, args.quality, args.playlist)
