import edge_tts
import asyncio
import pygame
import os
import time

VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_FILE = "output.mp3"

try:
    pygame.mixer.init()
except pygame.error:
    print("failed to initialize pygame mixer")

async def _generate_audio(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def speak(text):
    print(f"robo speaking '{text} ' ... ")

    try:
        asyncio.run(_generate_audio(text))
    except Exception as e:
        print(f"failed to generate audio: {e}")
        return

    try:
        pygame.mixer.music.load(OUTPUT_FILE)
        time.sleep(0.2)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

    except Exception as e:
        print(f"playback failed: {e}")
        

if __name__ == "__main__":
    speak("hello, world!")

