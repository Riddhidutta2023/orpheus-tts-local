# Orpheus-TTS-Local

A lightweight client for running [Orpheus TTS](https://huggingface.co/canopylabs/orpheus-3b-0.1-ft) locally using LM Studio API.

## Features

- 🎧 High-quality Text-to-Speech using the Orpheus TTS model
- 💻 Completely local - no cloud API keys needed
- 🔊 Multiple voice options (tara, leah, jess, leo, dan, mia, zac, zoe)
- 💾 Save audio to WAV files

## Quick Setup

1. Install [LM Studio](https://lmstudio.ai/) 
2. Download the [Orpheus TTS model (orpheus-3b-0.1-ft-q4_k_m.gguf)](https://huggingface.co/isaiahbjork/orpheus-3b-0.1-ft-Q4_K_M-GGUF) in LM Studio
3. Load the Orpheus model in LM Studio
4. Start the local server in LM Studio (default: http://127.0.0.1:1234)
5. Create a folder  and clone the repo
   ```
   git clone https://github.com/Riddhidutta2023/orpheus-tts-local.git
   ```
6. cd into the repo
7. Install dependencies:
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
8. Run the  commandline script:

   ```python
   python gguf_cmdline.py --text_file name_of_file.txt --voice tara --output my_audio.wav
   ```

## GUI Version

```python
python gguf_gui.py 
```

### Options

- `--text`: The text to convert to speech
- `--voice`: The voice to use (default: tara)
- `--output`: Output WAV file path (default: auto-generated filename)
- `--list-voices`: Show available voices
- `--temperature`: Temperature for generation (default: 0.6)
- `--top_p`: Top-p sampling parameter (default: 0.9)
- `--repetition_penalty`: Repetition penalty (default: 1.1)

## Available Voices

- tara - Best overall voice for general use (default)
- leah
- jess
- leo
- dan
- mia
- zac
- zoe

## Emotion
You can add emotion to the speech by adding the following tags:
```xml
<giggle>
<laugh>
<chuckle>
<sigh>
<cough>
<sniffle>
<groan>
<yawn>
<gasp>
```

## License

Apache 2.0

