# Gemini + Hugging Face Intro Lab

A simple local AI lab built in Python to practice API integration, environment variable management, terminal debugging, and chatbot development with both **Google Gemini** and **Hugging Face**.

## What this repo includes

- `index.py` — first Gemini API test
- `hugging.py` — request example using a Hugging Face model and token from `.env`
- `chatbot.py` — terminal chatbot with conversation memory
- `app.py` — Streamlit chatbot interface using Gemini
- `.env` — local environment variables file (**never commit this**)

## Main learnings

This lab covered the full path from “it does not run” to “it works locally with a UI”:

- fixing a Python environment / architecture conflict on macOS
- recreating a clean virtual environment
- loading secrets safely from `.env`
- calling Gemini from Python
- extracting model response text and token usage metadata
- calling a Hugging Face endpoint with an API token
- building a multi-turn chatbot in the terminal
- building a small Streamlit chatbot app

## Project setup

### 1. Create and activate a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install google-genai python-dotenv requests streamlit
```

### 3. Create a `.env` file

```env
GOOGLE_API_KEY=your_gemini_api_key_here
HUGGING_FACE_TOKEN=your_hugging_face_token_here
```

## Run the scripts

### Gemini basic script

```bash
python index.py
```

### Hugging Face query script

```bash
python hugging.py
```

### Terminal chatbot

```bash
python chatbot.py
```

### Streamlit chatbot

```bash
streamlit run app.py
```

## Suggested repo structure

```text
genai_intro/
├── app.py
├── chatbot.py
├── hugging.py
├── index.py
├── README.md
├── requirements.txt
└── .env
```

## Recommended `.gitignore`

```gitignore
.venv/
.env
__pycache__/
*.pyc
.streamlit/
```

## Notes

- The `.env` file should stay local and private.
- The main debugging challenge in this session was a macOS architecture mismatch between `x86_64` and `arm64`.
- Once the environment was rebuilt correctly, the Gemini and Streamlit apps worked as expected.

## Next improvements

- add `requirements.txt`
- improve Streamlit UI styling
- add error handling around API calls
- keep chat history in a cleaner structure
- deploy the app later if needed

---

Built as part of a Generative AI learning session by Franco Vargas.
