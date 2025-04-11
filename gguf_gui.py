import tkinter as tk
from tkinter import filedialog, messagebox
import wave
import time
import os
import sys

# Import local module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from gguf_orpheus import generate_speech_from_api, AVAILABLE_VOICES

def generate():
    input_file = file_path.get()
    voice = voice_var.get()
    output = output_name.get()

    if not input_file or not os.path.isfile(input_file):
        messagebox.showerror("Error", "Please select a valid text file.")
        return

    if not output.endswith(".wav"):
        output += ".wav"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        messagebox.showerror("Error", f"Could not read file: {e}")
        return

    try:
        audio_chunks = generate_speech_from_api(prompt=text, voice=voice)
        with wave.open(output, "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(24000)
            for chunk in audio_chunks:
                wf.writeframes(chunk)
        messagebox.showinfo("Done", f"Audio saved to {output}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("Orpheus TTS Generator")

file_path = tk.StringVar()
output_name = tk.StringVar(value="output.wav")
voice_var = tk.StringVar(value=AVAILABLE_VOICES[0])

tk.Label(root, text="Text File:").grid(row=0, column=0, sticky="e")
tk.Entry(root, textvariable=file_path, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: file_path.set(filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))).grid(row=0, column=2)

tk.Label(root, text="Voice:").grid(row=1, column=0, sticky="e")
tk.OptionMenu(root, voice_var, *AVAILABLE_VOICES).grid(row=1, column=1, sticky="w")

tk.Label(root, text="Output Filename:").grid(row=2, column=0, sticky="e")
tk.Entry(root, textvariable=output_name, width=40).grid(row=2, column=1)

tk.Button(root, text="Generate Speech", command=generate, bg="lightblue").grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
