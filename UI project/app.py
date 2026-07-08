import streamlit as st
from agent import ask_agent

st.set_page_config(
    page_title="🌍 City Assistant",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌍 AI City Assistant")
st.markdown(
    "Ask about **weather** 🌤️ or **latest news** 📰 for any city."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Ask something...")

if prompt:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ask_agent(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )