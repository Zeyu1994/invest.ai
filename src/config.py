from pathlib import Path
import os
from dotenv import load_dotenv
import torch


load_dotenv()

class Config:
    # Paths
    ROOT_DIR = Path(__file__).parent.parent.parent
    OUTPUT_DIR = ROOT_DIR / "output"
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    HF_AUTH_TOKEN = os.getenv("HF_AUTH_TOKEN")
    
    # Whisper Config
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    BATCH_SIZE = 16
    COMPUTE_TYPE = "float16"
    MODEL_SIZE = "large-v2"