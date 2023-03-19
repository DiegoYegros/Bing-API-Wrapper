import numpy as np
import whisper
import sys

if len(sys.argv) < 2:
    print("Usage: python3 trans.py [audio_file]")

model = whisper.load_model("base")

if len(sys.argv) <2:
    print("Error: No audio file specified.")
    sys.exit(1)    
audio = sys.argv[1]
transcription = model.transcribe(audio)
for sentennce in transcription["segments"]:
    print(sentennce["text"])
