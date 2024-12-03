import whisperx
import torch
import logging
from pathlib import Path
from typing import Dict, Any

class WhisperTranscriber:
    def __init__(self, device: str, batch_size: int, compute_type: str):
        self.device = device
        self.batch_size = batch_size
        self.compute_type = compute_type
        
    def transcribe(self, audio_path: Path, hf_token: str) -> Dict[str, Any]:
        """Transcribe audio file using WhisperX"""
        try:
            # Load model and transcribe
            model = whisperx.load_model("large-v3", self.device, compute_type=self.compute_type)
            audio = whisperx.load_audio(str(audio_path))
            result = model.transcribe(audio, batch_size=self.batch_size)
            
            # Align whisper output
            model_a, metadata = whisperx.load_align_model(
                language_code=result["language"], 
                device=self.device
            )
            result = whisperx.align(
                result["segments"], 
                model_a, 
                metadata, 
                audio, 
                self.device
            )
            
            # Diarization
            diarize_model = whisperx.DiarizationPipeline(
                use_auth_token=hf_token,
                device=self.device
            )
            diarize_segments = diarize_model(audio)
            result = whisperx.assign_word_speakers(diarize_segments, result)
            
            return result
            
        except Exception as e:
            logging.error(f"Error in transcription: {str(e)}")
            raise
        finally:
            # Cleanup
            if 'model' in locals():
                del model
            if 'model_a' in locals():
                del model_a
            torch.cuda.empty_cache()