from pytube import YouTube
import argparse

class Downloader:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Download a video from YouTube')
        self.parser.add_argument('link')
        self.parser.add_argument('output', default='.', nargs='?')
        self.parser.add_argument('-a', '--audio', action='store_true', help='Download audio only')
        self.args = self.parser.parse_args()
        self.yt = YouTube(self.args.link)

    def download(self):
        if self.args.audio:
            self.download_audio()
        else:
            self.download_video()

    def download_video(self):
        stream = self.yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream.download(self.args.output)
    
    def download_audio(self):
        stream = self.yt.streams.filter(only_audio=True).first()
        stream.download(self.args.output)

if __name__ == '__main__':
    Downloader().download()
