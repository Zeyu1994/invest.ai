import argparse
from pathlib import Path
from src.config import Config
from src.downloader import YouTubeDownloader
from src.transcriber import WhisperTranscriber
from src.summarizer import Summarizer

def main():
  # Add argument parser
    parser = argparse.ArgumentParser(description='Transcribe audio from YouTube URL or local file')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--youtube', '-yt', help='YouTube video URL')
    group.add_argument('--audio', '-a', help='Path to local audio file')
    args = parser.parse_args()

    # Initialize components
    downloader = YouTubeDownloader(Config.OUTPUT_DIR)
    transcriber = WhisperTranscriber(
        device = "cuda",
        batch_size=Config.BATCH_SIZE,
        compute_type=Config.COMPUTE_TYPE
    )
    summarizer = Summarizer()
    
    # Get audio path based on input type
    if args.youtube:
        audio_path = downloader.download_audio(args.youtube)

    else:
        audio_path = Path(args.audio)
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")

    
    
    # Transcribe
    result = transcriber.transcribe(audio_path, Config.HF_AUTH_TOKEN)
    
    # Format and save transcript
    transcript_path = audio_path.with_suffix('.txt')


    with open(transcript_path, 'w', encoding='utf-8') as f:
        if args.youtube:
            f.write(f"Title: {downloader.video_title}\n")
            f.write(f"Channel: {downloader.channel_name}\n")
            f.write(f"Description: {downloader.description}\n")
            f.write("\n")  # Add a newline to separate metadata from the transcript
        for segment in result['segments']:
            timestamp = f"[{int(segment['start'])//3600:02d}:{(int(segment['start'])%3600)//60:02d}:{int(segment['start'])%60:02d}]"
            line = f"{timestamp} {segment['speaker']}: {segment['text'].strip()}"
            f.write(line + '\n')
    
        
    # Summarize
    with open(transcript_path, 'r', encoding='utf-8') as f:
        transcript = f.read()
    summary = summarizer.summarize(transcript)
    
    # Save summary
    summary_path = transcript_path.with_name(transcript_path.stem + '_summary.txt')
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)

if __name__ == "__main__":
    main()