import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek
from tavily import TavilyClient

load_dotenv()
chat_model = os.environ.get("DEEPSEEK_MODEL")
tavily_key = os.environ.get("TAVILY_SEARCH")


@tool
def search(query: str) -> str:
    """Tool that search over the internet
    Args:
        query: the query to search for
    Returns:
        The search results
    """

    tavily_client = TavilyClient(api_key=tavily_key)
    response = tavily_client.search(query)

    return str(response)


def main():

    llm = ChatDeepSeek(model=str(chat_model), temperature=0)

    tool = [search]

    agent = create_agent(model=llm, tools=tool)
    response = agent.invoke(
        {"messages": [HumanMessage(content="what the weather in tokyo")]}
    )
    # result = agent.invoke({"messages": [{"role": "user", "content": "Summarize AI trends"}]})

    print(response["messages"])


if __name__ == "__main__":
    main()
