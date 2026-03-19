from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview",
    contents="Explain how AI works in a few words",
)

assistant_text = response.text
prompt_tokens = response.usage_metadata.prompt_token_count
completion_tokens = response.usage_metadata.candidates_token_count
total_tokens = response.usage_metadata.total_token_count

print("Assistant reply:")
print(assistant_text)
print()
print(f"Prompt tokens: {prompt_tokens}")
print(f"Completion tokens: {completion_tokens}")
print(f"Total tokens: {total_tokens}")