import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY was not found in the .env file")

client = genai.Client(api_key=api_key)

st.set_page_config(page_title="Gemini Chatbot", page_icon="💬")
st.title("💬 Gemini Chatbot")
st.write("Simple chatbot built with Streamlit and Gemini.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Keep your answers clear and concise.",
        }
    ]

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    conversation_text = "\n".join(
        f"{message['role'].capitalize()}: {message['content']}"
        for message in st.session_state.messages
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=conversation_text,
    )

    assistant_text = response.text.strip()
    st.session_state.messages.append({"role": "assistant", "content": assistant_text})

    with st.chat_message("assistant"):
        st.markdown(assistant_text)
