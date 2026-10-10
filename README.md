# LangChain Chat Model Examples

Small Python examples that call large language models through [LangChain](https://python.langchain.com/). There are two scripts:

- `chatbot.py` — OpenAI chat model via LangChain’s provider-agnostic helper
- `model.py` — Google Gemini via the dedicated Google Generative AI integration

Both scripts load API keys from a `.env` file, send a prompt to a model, and print the reply.

## Project files

| File | What it does |
|------|----------------|
| `chatbot.py` | Initializes an OpenAI model twice: once with a fixed prompt, then again with custom settings and your own question |
| `model.py` | Initializes Google Gemini and asks a single geography question |
| `.env` | Stores API keys (keep this file private; never commit real keys) |

## Setup

1. Create and activate a virtual environment (this project already has `.venv` if you prefer to reuse it).
2. Install dependencies:

```bash
pip install langchain langchain-openai langchain-google-genai python-dotenv
```

3. Put your keys in `.env` in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

`python-dotenv` reads these variables when each script starts.

## How the code works

Every script follows the same pattern:

1. Load environment variables so LangChain can authenticate.
2. Create a chat model object.
3. Call `invoke(...)` with a string prompt.
4. Print `response.content` (the text of the model’s reply).

### `chatbot.py`

This file shows two ways to use OpenAI through LangChain.

**1. Load secrets**

```python
from dotenv import load_dotenv
load_dotenv()
```

`load_dotenv()` reads `.env` and sets `OPENAI_API_KEY` in the process environment. LangChain uses that key automatically.

**2. Initialize and invoke (default settings)**

```python
from langchain.chat_models import init_chat_model
model = init_chat_model(model="gpt-6-luna")
response = model.invoke("What can you do?")
print(response.content)
```

- `init_chat_model` is LangChain’s helper that picks the right provider from the model name. Here it talks to OpenAI.
- `invoke` sends one message and waits for a full reply.
- `response` is a message object; `.content` is the answer text.

This first block always asks *"What can you do?"* so you can confirm the API works.

**3. Customize the model and ask your own question**

```python
model = init_chat_model(
    model="gpt-6-luna",
    temperature=1.0
)
question = input("Enter your question: ")
response = model.invoke(question)
print(response.content)
```

- A new model instance is created with `temperature=1.0`. Temperature controls randomness: closer to `0` is more focused; closer to `1` is more varied.
- `input(...)` waits for you to type a question in the terminal.
- That question is sent to the same model family, and the answer is printed.

Run it with:

```bash
python chatbot.py
```

You will see the first canned reply, then a prompt asking for your own question.

### `model.py`

This file uses Google Gemini instead of OpenAI.

```python
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
response = model.invoke("What's the capital of the Pakistan?")
print(response.content)
```

- `ChatGoogleGenerativeAI` is the Google-specific chat class (not the generic `init_chat_model` helper).
- It uses `GOOGLE_API_KEY` from `.env`.
- `gemini-3.1-flash-lite` is a fast, lightweight Gemini model.
- The script asks a fixed question and prints the answer (Islamabad).

Run it with:

```bash
python model.py
```

## OpenAI vs Google in this project

| | `chatbot.py` | `model.py` |
|---|---|---|
| Library | `langchain.chat_models.init_chat_model` | `langchain_google_genai.ChatGoogleGenerativeAI` |
| Model | `gpt-6-luna` | `gemini-3.1-flash-lite` |
| Auth env var | `OPENAI_API_KEY` | `GOOGLE_API_KEY` |
| Interaction | Fixed prompt, then your typed question | One fixed prompt |

The two styles are interchangeable for a simple Q&A: create a model object, call `invoke`, read `.content`.

