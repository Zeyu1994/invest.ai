from src.downloader import YouTubeDownloader
from src.transcriber import WhisperTranscriber
from src.summarizer import Summarizer
from src.config import Config
from src.prompts import SUMMARY_PROMPT

__version__ = "0.1.0"

# Export main classes for easier imports
__all__ = [
    "YouTubeDownloader",
    "WhisperTranscriber",
    "Summarizer",
    "Config"
    "SUMMARY_PROMPT"
]