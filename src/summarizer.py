from openai import OpenAI
from pathlib import Path
import logging
from typing import Optional

class Summarizer:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        
    def summarize(self, transcript: str, prompt: Optional[str] = None) -> str:
        """Summarize transcript using OpenAI API"""
        if prompt is None:
            prompt = self._get_default_prompt()
            
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": transcript}
                ],
                temperature=0.1
            )
            return response.choices[0].message.content
            
        except Exception as e:
            logging.error(f"Error in summarization: {str(e)}")
            raise
            
    @staticmethod
    def _get_default_prompt() -> str:
        """Return default summarization prompt"""
        return """Summarize the transcript provided..."""  # Your existing prompt