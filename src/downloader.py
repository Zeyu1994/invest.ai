from pytubefix import YouTube
from pathlib import Path
import logging

class YouTubeDownloader:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def download_audio(self, url: str) -> Path:
        """Download audio from YouTube video"""
        try:
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            
            # Normalize filename
            filename = self._normalize_filename(yt.title) + ".m4a"
            output_path = self.output_dir / filename
            self.description = yt.description
            self.video_title = yt.title
            self.channel_name = yt.author
            
            stream.download(output_path=str(self.output_dir), filename=self._normalize_filename(yt.title))
            return output_path
            
        except Exception as e:
            logging.error(f"Error downloading video: {str(e)}")
            raise
            
    @staticmethod
    def _normalize_filename(title: str) -> str:
        """Normalize filename by replacing invalid characters"""
        invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|']
        for char in invalid_chars:
            title = title.replace(char, '_')
        return title