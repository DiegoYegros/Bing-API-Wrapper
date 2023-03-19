from pytube import YouTube
import asyncio
import trans
import bingChatAPI as bingChat
from os import system, path as p
def download_audio(link):
    yt = YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    default_filename = stream.default_filename
    path = p.abspath(default_filename)  
    return path
  
async def main():
  while (True):
    system("clear")
    link = input("Ingresa enlace para transcribir audio: ")
    transcript = trans.transcribe(download_audio(link))
    print(f"Bing Chat: {await bingChat.givenTranscription(transcript)}")
    userInput = input("Deseas elegir video? (Presiona enter para continuar, N para salir) ")
    if (userInput.lower() == "n"):
      print("Hasta luego!")
      break;
if __name__ == "__main__":
  asyncio.run(main())