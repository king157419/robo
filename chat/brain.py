from openai import OpenAI
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


my_http_client = httpx.Client(
    trust_env = False
)

client = OpenAI(
    api_key= API_KEY ,
    base_url="https://api.deepseek.com",
    http_client = my_http_client
    )

def chat(user_input):
    print("connecting 2 ds...")
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages = [
                {"role": "system", "content" : "你是一个可爱的小宝宝，名字叫做小羊。说话简短可爱，不会长篇大论。"},
                {"role": "user", "content": user_input},
            ],
            stream = False
        )

        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        print(f"brain error: {e}")
        return "哎呀 人家脑子卡住了 连接不上服务器了"

if __name__ =="__main__":
    test_reply = chat("你好 你是谁？")
    print(f"ds回复: {test_reply}")