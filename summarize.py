# summarize_script.py

import argparse
import os
from src.summarizer import Summarizer
from src.config import Config
from dotenv import load_dotenv

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description='Summarize a transcript.')
    parser.add_argument('filepath', type=str, help='Path to the text or markdown file.')
    parser.add_argument('--chain_type', type=str, choices=['summary', 'qa', 'final'], default='final', help='Type of chain to use.')
    parser.add_argument('--transcript_type', type=str, choices=['earning_transcript', 'invest_transcript'], default='invest_transcript', help='Type of transcript.')
    args = parser.parse_args()

    # Read the file
    if not os.path.exists(args.filepath):
        print(f"File {args.filepath} does not exist.")
        return
    with open(args.filepath, 'r', encoding='utf-8') as f:
        transcript = f.read()

    summarizer = Summarizer()

    # Determine which prompts to use based on the transcript type
    if args.transcript_type == 'earning_transcript':
        summary_prompt_key = 'earning_transcript_summary'
    else:
        summary_prompt_key = 'default_summary_prompt'

    # Use default prompts for QA and final prompts
    qa_prompt_key = 'default_qa_prompt'
    final_prompt_key = 'default_final_prompt'

    # Generate the summary
    summary = summarizer.summarize(
        transcript=transcript,
        chain_type=args.chain_type,
        summary_prompt_key=summary_prompt_key,
        qa_prompt_key=qa_prompt_key,
        final_prompt_key=final_prompt_key
    )
    # Save the generated summary to a file
    summary_path = os.path.splitext(args.filepath)[0] + '_summary.txt'
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    print(f"Summary saved to {summary_path}")

if __name__ == "__main__":
    main()