import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY was not found in the .env file")

client = genai.Client(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Keep your answers clear and concise.",
    }
]

print("Chatbot started. Type 'quit' or 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in {"quit", "exit"}:
        print("Chatbot ended.")
        break

    messages.append({"role": "user", "content": user_input})

    conversation_text = "\n".join(
        f"{message['role'].capitalize()}: {message['content']}" for message in messages
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=conversation_text,
    )

    assistant_text = response.text.strip()
    messages.append({"role": "assistant", "content": assistant_text})

    print(f"Assistant: {assistant_text}\n")

# Bonus idea with Streamlit:
# 1. Install it with: pip install streamlit
# 2. Run it with: streamlit run chatbot.py
# 3. For a real Streamlit app, it is better to create a separate file such as app.py
