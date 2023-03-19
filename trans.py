import numpy as np
import whisper
import warnings
import sys
from os import system, devnull

warnings.simplefilter("ignore")

#Audio as Argument
def argument():
    if len(sys.argv) < 2:
        print("Usage: python3 trans.py [audio_file]")

    model = whisper.load_model("base")

    if len(sys.argv) <2:
        print("Error: No audio file specified.")
        sys.exit(1)    
    audio = sys.argv[1]
    transcription = model.transcribe(audio)
    sys("clear")
    for sentennce in transcription["segments"]:
        print(sentennce["text"])


#Audio as Input
def transcribe(audio_file):
    model = whisper.load_model("base")
    transcription = model.transcribe(audio_file)
    frase = ""
    for sentence in transcription["segments"]:
        frase += sentence["text"]
    print(f"\nFrase: {frase}\n" )
    return frase

