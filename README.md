 # ReadMe
 This notebook transcribes YouTube videos using WhisperX

 ## Prerequisites
 1. pytubefix - For downloading YouTube videos
 2. WhisperX - For high-accuracy transcription (https://github.com/m-bain/whisperX)
    - If using CUDA 11.x: Install ctranslate2==3.24.0
    - Install numpy<2 if required
    - Requires GPU with CUDA support
 ## Getting Started
 1. Install WhisperX:
    ```bash
    pip install git+https://github.com/m-bain/whisperX.git
    ```

 2. Install other dependencies:
    ```bash
    pip install -r requirements.txt
    ```

 3. Create a .env file with your API keys:
    ```
    OPENAI_API_KEY=your_openai_key
    HF_AUTH_TOKEN=your_huggingface_token
    ```
 ## Running the Script
 ```bash
 # For YouTube videos
 python transcribe_video.py --youtube https://www.youtube.com/watch?v=ZEyPHhBKgJ4

 # For local audio files  
 python transcribe_video.py --audio path/to/audio.mp3
 ```


# 
