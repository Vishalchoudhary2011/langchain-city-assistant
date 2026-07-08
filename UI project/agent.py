from dotenv import load_dotenv
import os
import requests

from langchain.tools import tool
from tavily import TavilyClient
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

load_dotenv()

# ---------------- Weather Tool ----------------

@tool
def get_weather(city: str):
    """Get current weather of a city"""

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return data.get("message")

    return (
        f"Weather in {city}\n"
        f"Temperature: {data['main']['temp']}°C\n"
        f"Condition: {data['weather'][0]['description']}"
    )


# ---------------- News Tool ----------------

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city: str):
    """Get latest news of a city"""

    response = tavily_client.search(
        query=f"Latest news about {city}",
        max_results=3
    )

    news = []

    for article in response.get("results", []):

        news.append(
            f"• {article['title']}\n"
            f"{article['content']}\n"
            f"{article['url']}"
        )

    return "\n\n".join(news)


# ---------------- LLM ----------------

llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY"),
)

# ---------------- Agent ----------------

agent = create_agent(
    model=llm,
    tools=[get_weather, get_news],
    system_prompt="You are a helpful city assistant."
)

# ---------------- Function ----------------

def ask_agent(question: str):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    return result["messages"][-1].content