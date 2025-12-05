import speech_recognition as sr
import whisper
import os
import torch

MODEL_SIZE = "small"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print(f"loading whisper ({MODEL_SIZE}) to {DEVICE}... ")
model = whisper.load_model(MODEL_SIZE, device = DEVICE)

print("initializing ear")
r = sr.Recognizer()
r.pause_threshold = 1
mic = sr.Microphone()

with mic as source:
        print("adjusting to env voices")
        r.adjust_for_ambient_noise(source)
        print("done")

def listen():
    with mic as source:
        print("say anything")
        try:
            audio = r.listen(source, timeout = 5 )
        except sr.WaitTimeoutError:
            print("timeout: did u really speak?")
            return None
    try:
        temp_file = "temp.wav"
        with open(temp_file, "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe(temp_file, language = 'zh')
        text = result["text"].strip()
        os.remove(temp_file)
        print("---")
        print("u said: ", text)
        print("---")
        return text
    except sr.UnknownValueError:
        print("sorry, i can't get that")
        return None
    except sr.RequestError as e:
        print(f"request error: {e}")
        return None

if __name__ =="__main__":
    while True:
        listen()