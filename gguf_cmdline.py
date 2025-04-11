#Now this file allows you to specify input file in text format
import argparse
import wave
import time
import os
import sys

# Add current directory to path for local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gguf_orpheus import generate_speech_from_api, AVAILABLE_VOICES

# --- Argument Parser ---
parser = argparse.ArgumentParser(description="Generate speech using Orpheus TTS")
parser.add_argument("--text", type=str, help="Text to synthesize")
parser.add_argument("--text_file", type=str, help="Path to a text file to synthesize")
parser.add_argument("--voice", type=str, default="tara", choices=AVAILABLE_VOICES, help="Voice to use")
parser.add_argument("--output", type=str, default="output.wav", help="Output filename (e.g., result.wav)")
args = parser.parse_args()

# --- Load text ---
if args.text_file:
    try:
        with open(args.text_file, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        raise ValueError(f"Failed to read text file: {e}")
elif args.text:
    text = args.text
else:
    raise ValueError("You must provide either --text or --text_file")

# --- Generate speech ---
start_time = time.monotonic()
audio_chunks = generate_speech_from_api(prompt=text, voice=args.voice)

# --- Write output to specified WAV file ---
with wave.open(args.output, "wb") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(24000)

    total_frames = 0
    for chunk in audio_chunks:
        frame_count = len(chunk) // 2
        total_frames += frame_count
        wf.writeframes(chunk)

duration = total_frames / 24000
end_time = time.monotonic()

print(f"✅ Saved output to '{args.output}'")
print(f"📦 Duration: {duration:.2f}s | ⏱️ Time taken: {end_time - start_time:.2f}s")
