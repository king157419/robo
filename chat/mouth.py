import requests
import pygame
import os
import time
import threading
import json

API_URL = "http://127.0.0.1:9880/tts"

EMOTION_MAP = {
    "开心": {
        "file" : r"D:\desk\ref\happy.wav",
        "text" : ""
    },
    "难过": {
        "file" : r"D:\desk\ref\sad.wav",
        "text" : ""
    },
    "生气": {
        "file" : r"D:\desk\ref\anrgy.wav",
        "text" : ""
    },
    "正常": {
        "file" : r"D:\desk\ref\general.wav",
        "text" : ""
    }
}



def play_audio(filename):
    try:
        if pygame.mixer.get_init() is None:
            pygame.mixer.init(frequency = 32000)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        time.sleep(0.5)

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()
    except Exception as e:
        print(f"failed to load...")

def speak(text, emotion="正常"):

    print(f"[GPT-SoVITS generating] ({emotion}): {text}")

    current_emotion_data = EMOTION_MAP.get(emotion, EMOTION_MAP["正常"])

    if not current_emotion_data["file"]:
         print(f"no audio file found for emotion: {emotion}")
         return

    payload = {
        "text": text,
        "text_lang": "zh",
        "ref_audio_path": current_emotion_data["file"],
        "prompt_text": current_emotion_data["text"],
        "prompt_lang": "zh",
        "text_split_method": "cut5",
        "batch_size": 1,
        "media_type": "wav",
        "streaming_mode": False,
        "top_k": 15,
        "top_p": 1.0,
        "temperature": 1.0


    }

    try:
        response = requests.post(API_URL, json = payload)
        
        if response.status_code == 200:
            audio_content = response.content
            output_file = "output_sovits.wav"
            with open(output_file, "wb") as f:
                f.write(audio_content)

                print(f"saying:")
            play_audio(output_file)
        else:
            print(f"failed to generate audio  {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"failed to connect: {e}")


if __name__ =="__main__":
    speak("主人，我是你的新声音，听起来怎么样","开心")

    