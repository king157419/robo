import ear
import mouth
import brain
import face
import threading
import re
import random
import time



def run_bot_logic():
    time.sleep(1)
    face.face_app.set_emotion("开心")
    mouth.speak("主人，小羊醒啦", "开心")
    face.face_app.set_emotion("正常")

    while True:
        user_text = ear.listen()
        if user_text:
            print(f"brain accepted: {user_text}")
            face.face_app.set_emotion("难过")
            if "退出" in user_text or "再见" in user_text:
                mouth.speak("好的，我去休息了，白白", "难过")
                import os
                os._exit(0)

            face.face_app.set_emotion("思考")
            full_reply = brain.chat(user_text)

            match = re.search(r"\[(.*?)\]", full_reply)

            if match :
                emotion = match.group(1)
                content = re.sub(r"\[(.*?)\]", "", full_reply).strip()
            else:
                emotion = "正常"
                content = full_reply
                print(f"回复: {content}, 情绪: {emotion}")

            face.face_app.set_emotion(emotion)
            mouth.speak(content, emotion)

            face.face_app.set_emotion("正常")

        else:
            pass

def main():
    t = threading.Thread(target = run_bot_logic, daemon = True)
    t.start()
    print("initializing face")
    face.face_app.start()



if __name__=="__main__":
    main()