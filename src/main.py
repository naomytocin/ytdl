import argparse
from pytubefix import YouTube
import os

def Download(link):
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()

        # save path
        save_path = os.path.join(os.path.expanduser("~"), "Documents", "Videos")
        stream.download(output_path=save_path)

        print("downloaded successfully:", save_path)
    except:
        print("error idk what happened go fix it")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="download vids from yt with link")
    parser.add_argument('link', help='yt video url')
    args = parser.parse_args()
    Download(args.link)
