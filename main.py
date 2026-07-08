from dotenv import load_dotenv
import os
import requests
from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, AIMessage
from tavily import TavilyClient
from langchain.agents import create_agent

load_dotenv() 

# Weather tool
print("Mistral Key:", os.getenv("MISTRAL_API_KEY"))
print("Weather Key:", os.getenv("OPENWEATHER_API_KEY"))
print("Tavily Key:", os.getenv("TAVILY_API_KEY"))

@tool
def get_weather(city: str):
    """Get Current weather of a city"""
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather"f"?q={city}&appid={API_KEY}&units=metric"
    

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return f"Error: {data.get('message', 'Something went wrong')}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"weather in {city}: {desc}, {temp}°C"


#Tavily news tools

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def get_news(city:str): 
    """Get latest news about city"""

    response = tavily_client.search(
        query=f"Latest news about {city}",
        search_depth="basic",
        max_results=3
        )
    
    results = response.get("results", [])

    if not results:
        return f"No latest news found for {city}."
    

    news = []

    for i, article in enumerate(results, start=1):
        title = article.get("title", "No Title")
        content = article.get("content", "No Content Available")
        url = article.get("url", "No URL")

        news.append(
            f"{i}. {title}\n"
            f"Summary: {content[:100]}...\n"
            f"Source: {url}\n"
        )
    return f"Latest news of {city}:\n\n" + "\n\n".join(news)


llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=os.getenv("MISTRAL_API_KEY"),
)


agent = create_agent(
    model=llm,
    tools=[get_weather, get_news],
    system_prompt="You are a helpful city assistant",
)

print("City agent | type exit to quit")

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break
    result = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]}
        )

    print(result['message'][-1].content )