import ear
import mouth
import brain

def main():
    while True:
        user_text = ear.listen()
        if user_text:
            print(f"brain accepted: {user_text}")
            if "退出" in user_text or "再见" in user_text:
                mouth.speak("好的，我去休息了，白白")
                break

            reply = brain.chat(user_text)
            mouth.speak(reply)
        else:
            pass

if __name__=="__main__":
    main()