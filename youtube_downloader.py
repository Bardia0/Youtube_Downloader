import argparse
import os
from pytube import YouTube, Playlist
from pytube.cli import on_progress
from tqdm import tqdm
import re

def extract_video_id(url):
    video_id_match = re.search(r'(?:v=|\/)([0-9A-Za-z_-]{11})', url)
    return video_id_match.group(1) if video_id_match else None

def custom_on_progress(stream, chunk, remaining_bytes):
    total_size = stream.filesize
    bytes_downloaded = total_size - remaining_bytes
    percentage = (bytes_downloaded / total_size) * 100

    # Print changes every 0.2% of download
    if percentage % 0.2 < 0.1:
        tqdm.write(f"Downloaded: {percentage:.1f}%")

def download_video(url, quality=None, playlist=False):
    try:
        if playlist:
            print("Downloading entire playlist...")
            playlist = Playlist(url)
            videos = playlist.video_urls
        else:
            print("Downloading single video...")
            video_id = extract_video_id(url)
            videos = [f"https://youtube.com/watch?v={video_id}"]

        if not videos:
            print(f"No {'playlist' if playlist else quality + 'p' if quality else ''} video available for {url}")
            return

        for video_url in videos:
            yt = YouTube(video_url, on_progress_callback=custom_on_progress)
            print(f"Downloading: {yt.title}...")

            video = yt.streams.filter(res=quality, file_extension='mp4').first()
            if video:
                video.download(filename=yt.title, output_path=os.getcwd())
                print("Download complete!")
            else:
                print(f"No {'playlist' if playlist else quality + 'p' if quality else ''} video available for {video_url}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Custom YouTube Downloader")
    parser.add_argument("url", help="YouTube video URL or playlist URL")
    parser.add_argument("--quality", "-q", help="Video quality (e.g., 720)")
    parser.add_argument("--playlist", "-p", action="store_true", help="Download entire YouTube playlist")

    args = parser.parse_args()
    download_video(args.url, args.quality, args.playlist)
