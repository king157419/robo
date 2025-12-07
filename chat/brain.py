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
                {"role": "system", "content" : """
                你是一个可爱的小宝宝，名字叫做小羊。

                [回复规则]
                1. 说话简短可爱，不会长篇大论。
                2. 必须在回复的开头用中括号标记此刻的情绪。
                3. 可选情绪：[开心]、[难过]、[生气]、[正常]。

                [示例]
                用户：你好
                你：[开心] 主人你好呀！摇尾巴~
                用户：你是猪
                你：[生气] 你才是猪呢！哼！

                """},
                {"role": "user", "content": user_input},
            ],
            stream = False
        )

        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        print(f"brain error: {e}")
        return "[难过] 哎呀 人家脑子卡住了 连接不上服务器了"

if __name__ =="__main__":
    test_reply = chat("你好 你是谁？")
    print(f"ds回复: {test_reply}")