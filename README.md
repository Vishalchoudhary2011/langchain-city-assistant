# 🌍 AI City Assistant

An intelligent **AI-powered City Assistant** built using **LangChain**, **Mistral AI**, **Streamlit**, **OpenWeather API**, and **Tavily Search API**.

The application uses a **LangChain Agent** that intelligently selects the appropriate tool based on the user's query to provide real-time weather updates and the latest city news.

---

## 🚀 Features

- 🤖 AI-powered LangChain Agent
- 🌤️ Real-time weather updates
- 📰 Latest city news
- 🛠️ Custom LangChain Tools
- 💬 Interactive Streamlit Chat Interface
- 🔍 Tavily Search Integration
- 📍 City-wise information
- 🧠 Automatic tool selection by the AI agent

---
Envirolment variables

MISTRAL_API_KEY="test"
TAVILY_API_KEY="test"
OPENWEATHER_API_KEY="test"

# 🧠 Agent Functionality

This project uses a **LangChain Agent** capable of reasoning about the user's request and deciding which tool(s) to invoke.

The agent can:

- Detect whether the user is asking about weather, news, or both.
- Automatically invoke the appropriate tool.
- Combine results from multiple tools into a single natural-language response.

### Example

**User Input**

```text
Tell me the latest weather and news of Indore.
```

**Agent Workflow**

```text
User Query
      │
      ▼
LangChain Agent
      │
      ├──────────────┐
      ▼              ▼
Weather Tool     News Tool
      │              │
      ▼              ▼
OpenWeather API  Tavily Search API
      │              │
      └──────┬───────┘
             ▼
      Final AI Response
```

The agent determines that the query requires information from **both tools**, executes them, and combines the responses before presenting the final answer.

---

# 🛠️ Available Tools

## 🌤️ Weather Tool

**Purpose**

Fetches the current weather of any city.

**API Used**

OpenWeather API

### Returns

- Temperature
- Weather Condition
- City Name

Example:

```text
Weather in Indore

Temperature : 30°C

Condition : Clear Sky
```

---

## 📰 News Tool

**Purpose**

Fetches the latest news related to a city.

**API Used**

Tavily Search API

### Returns

- News Headlines
- Short Summary
- Source URL

Example

```text
1. Heavy rainfall expected...

Summary...

Source:
https://...
```

---

# 🏗️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| LangChain | AI Agent Framework |
| LangGraph | Agent Execution |
| Mistral AI | Large Language Model |
| Streamlit | Frontend UI |
| OpenWeather API | Weather Information |
| Tavily Search API | Latest News |
| Python Dotenv | Environment Variables |

---

# 📂 Project Structure

```text
City-Assistant/
│
├── app.py                  # Streamlit UI
├── agent.py                # LangChain Agent
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── assets/
│   ├── home.png
│   └── chat.png
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/city-assistant.git

cd city-assistant
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_mistral_api_key

OPENWEATHER_API_KEY=your_openweather_api_key

TAVILY_API_KEY=your_tavily_api_key
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Application URL

```text
http://localhost:8501
```

---

# 💬 Example Queries

## Weather

```text
What is the weather in Delhi?
```

```text
Current weather of Mumbai
```

```text
Tell me today's weather in Jaipur.
```

---

## News

```text
Latest news of Indore
```

```text
Show today's news about Bengaluru.
```

---

## Multiple Tool Invocation

```text
Give me the weather and latest news of Indore.
```

```text
What's happening in Delhi? Also tell me the weather.
```

---

# 📸 Screenshots

## Home Page

_Add your Streamlit home page screenshot here._

---

## Chat Interface

_Add your chat interface screenshot here._

---

# 🔄 Agent Workflow

```text
                User Query
                     │
                     ▼
             LangChain Agent
                     │
      ┌──────────────┼──────────────┐
      ▼                             ▼
Weather Tool                 News Tool
(OpenWeather API)       (Tavily Search API)
      │                             │
      └──────────────┬──────────────┘
                     ▼
            AI Generated Response
                     │
                     ▼
              Streamlit Interface
```

---

# 📦 Dependencies

- langchain
- langgraph
- langchain-mistralai
- streamlit
- tavily-python
- python-dotenv
- requests

---

# 🚀 Future Improvements

- 🌤️ 7-Day Weather Forecast
- 🌍 Multi-city Comparison
- 🌫️ Air Quality Index (AQI)
- 🗺️ Google Maps Integration
- 🎙️ Voice Assistant
- 🌐 Multi-language Support
- 💾 Chat History
- 📍 Detect Current Location
- 🧾 Export Chat as PDF

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository

2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature/new-feature
```

5. Create a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Vaishvi Choudhary**

- GitHub: https://github.com/your-username
- LinkedIn: https://linkedin.com/in/your-profile

---

# ⭐ Show Your Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.