import os
from langchain_deepseek import ChatDeepSeek
from dotenv import load_dotenv

load_dotenv()


def main():
    print("data")
    print(os.environ.get("DEEPSEEK_API_KEY"))



main()