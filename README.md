# LangChain Chat Model

Small Python examples that use large language models through [LangChain](https://python.langchain.com/). This project includes three scripts:

- `chatbot.py` — OpenAI chat model examples using LangChain's provider-agnostic helper.
- `model.py` — Google Gemini using the dedicated Google Generative AI integration.
- `agent_conversation.py` — An interactive LangChain AI Agent chatbot that keeps conversation history while the program is running.

The scripts load API keys from a `.env` file, send prompts to a model, and print the replies. The interactive agent lets you continue chatting until you type `exit`, `quit`, or `bye`.

## Project Files

| File | What it does |
|------|----------------|
| `chatbot.py` | Initializes an OpenAI model with a fixed prompt, then asks for a question in the terminal using custom settings. |
| `model.py` | Initializes Google Gemini and asks a single geography question. |
| `agent_conversation.py` | Creates an OpenAI-powered LangChain Agent, accepts repeated user input, displays each AI reply, and keeps conversation history during the session. |
| `.env` | Stores API keys. Keep this file private and never commit real keys. |
| `.gitignore` | Lists files and folders Git should ignore, such as `.env` and `.venv/`. |

## Setup

### 1. Create and activate a virtual environment

Open a terminal in the project root and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

If you already have a working `.venv`, you can activate and reuse it.

### 2. Install dependencies

```bash
pip install langchain langchain-openai langchain-google-genai python-dotenv
```

### 3. Configure API keys

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```

Only add the keys for the providers you plan to use. Never share your real API keys or commit `.env` to GitHub.

The `python-dotenv` package reads these variables when `load_dotenv()` runs.

## How the Code Works

The scripts follow a similar pattern:

1. Load environment variables from `.env`.
2. Create a chat model or AI Agent.
3. Send a prompt or conversation messages.
4. Print the AI response in the terminal.

## 1. `chatbot.py`

This file demonstrates two ways to use OpenAI through LangChain.

### Load environment variables

```python
from dotenv import load_dotenv

load_dotenv()
```

`load_dotenv()` reads the `.env` file and makes its variables available to the Python process. LangChain uses `OPENAI_API_KEY` to authenticate with OpenAI.

### Initialize and invoke a model

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(model="gpt-6-luna")

response = model.invoke("What can you do?")

print(response.content)
```

- `init_chat_model()` initializes a chat model.
- `invoke()` sends a prompt to the model and waits for a reply.
- `response.content` contains the reply text.

This example asks a fixed question so you can check that the API connection works.

### Customize the model and ask your own question

```python
model = init_chat_model(
    model="gpt-6-luna",
    temperature=1.0
)

question = input("Enter your question: ")

response = model.invoke(question)

print(response.content)
```

- `temperature` controls response variability, where supported by the model.
- `input()` waits for you to type a question in the terminal.
- The question is sent to the model, and its answer is printed.

Run the script:

```bash
python chatbot.py
```

## 2. `model.py`

This file uses Google Gemini instead of OpenAI.

```python
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

response = model.invoke("What's the capital of Pakistan?")

print(response.content)
```

- `ChatGoogleGenerativeAI` is the Google-specific LangChain chat model class.
- It uses `GOOGLE_API_KEY` from `.env`.
- The script asks a fixed question and prints the answer.

Run the script:

```bash
python model.py
```

## 3. `agent_conversation.py`

This file creates an interactive AI Agent using LangChain's `create_agent()` function.

You can enter questions repeatedly, read the AI's replies, and ask follow-up questions using the conversation history. The chatbot continues running until you type `exit`, `quit`, or `bye`.

### Complete Code

```python
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage

load_dotenv()

agent = create_agent(
    model="openai:gpt-6-luna"
)

# Store conversation history
messages = []

print("=" * 45)
print("       AI CHATBOT")
print("Type 'exit' to quit the chatbot")
print("=" * 45)

while True:
    # Get input from user
    user_input = input("\n👤 You: ")

    # Exit chatbot
    if user_input.lower().strip() in ["exit", "quit", "bye"]:
        print("\n🤖 AI: Goodbye! Have a great day.")
        break

    # Add user's message to conversation
    messages.append(HumanMessage(content=user_input))

    # Get AI response
    response = agent.invoke({
        "messages": messages
    })

    # Get the latest AI message
    ai_response = response["messages"][-1].content

    # Display AI response
    print(f"\n🤖 AI: {ai_response}")

    # Save conversation history
    messages = response["messages"]
```

### How It Works

**1. Load environment variables**

```python
load_dotenv()
```

Loads the API key from `.env` so the agent can authenticate with the model provider.

**2. Create the AI Agent**

```python
agent = create_agent(
    model="openai:gpt-6-luna"
)
```

Creates a LangChain Agent configured to use the specified OpenAI model.

**3. Initialize conversation history**

```python
messages = []
```

Creates an empty list to store the messages exchanged during the conversation.

**4. Get input from the user**

```python
user_input = input("\n👤 You: ")
```

Waits for the user to type a message in the terminal.

**5. Check whether the user wants to exit**

```python
if user_input.lower().strip() in ["exit", "quit", "bye"]:
    print("\n🤖 AI: Goodbye! Have a great day.")
    break
```

If the user types `exit`, `quit`, or `bye`, the `break` statement stops the loop and ends the chatbot.

**6. Add the user's message**

```python
messages.append(HumanMessage(content=user_input))
```

Creates a `HumanMessage` and adds it to the conversation history.

**7. Send messages to the agent**

```python
response = agent.invoke({
    "messages": messages
})
```

Sends the conversation history to the agent and gets a response.

**8. Extract the AI's latest response**

```python
ai_response = response["messages"][-1].content
```

Selects the last message in the returned list and extracts its text.

**9. Display the answer**

```python
print(f"\n🤖 AI: {ai_response}")
```

Prints the AI's answer in the terminal with a clear label.

**10. Save the updated conversation history**

```python
messages = response["messages"]
```

Stores the returned messages so the next interaction can use the previous conversation as context.

### Why Use a `while` Loop?

The `while True` loop allows the chatbot to continue accepting messages without restarting the program after every question.

The workflow is:

1. User enters a question.
2. The agent processes the conversation.
3. The AI responds.
4. The updated history is saved.
5. The chatbot waits for another question.
6. The loop ends when the user enters an exit command.

### Example Terminal Session

```text
=============================================
       AI CHATBOT
Type 'exit' to quit the chatbot
=============================================

👤 You: What is Python?

🤖 AI: Python is a general-purpose programming language
known for its readability and simplicity.

👤 You: Why is it popular for AI?

🤖 AI: Python has a rich ecosystem of libraries for
machine learning and AI development.

👤 You: exit

🤖 AI: Goodbye! Have a great day.
```

### Run the Agent Chatbot

```bash
python agent_conversation.py
```

**Important:** Conversation history is kept in memory while the program is running. It is not saved permanently and is cleared when the program exits.

## OpenAI vs Google in This Project

| Feature | `chatbot.py` | `model.py` | `agent_conversation.py` |
|---|---|---|---|
| LangChain interface | `init_chat_model` | `ChatGoogleGenerativeAI` | `create_agent` |
| Provider | OpenAI | Google | OpenAI |
| Model configured in example | `gpt-6-luna` | `gemini-3.1-flash-lite` | `openai:gpt-6-luna` |
| Environment variable | `OPENAI_API_KEY` | `GOOGLE_API_KEY` | `OPENAI_API_KEY` |
| Interaction | Fixed prompt, then user input | One fixed prompt | Repeated user input with conversation history |

## Security Notes

- Keep `.env` private and never commit real API keys.
- Add `.env` and `.venv/` to `.gitignore`.
- Never hardcode API keys in Python source files.
- API access and model availability depend on your provider account and the exact model IDs available to you.

## Troubleshooting

### Missing OpenAI Credentials

If you see an error saying `OPENAI_API_KEY` is missing:

1. Confirm `.env` is in the project root.
2. Confirm it contains `OPENAI_API_KEY=your_actual_key`.
3. Confirm the script calls `load_dotenv()` before creating the model or agent.
4. Run the script from the project directory.
5. Ensure the API key is valid and your account has API access.

### Model Not Found or Unavailable

Check that the model ID is correct and available to your API account, and that the required LangChain provider integration is installed.

### Missing Python Package

Activate your virtual environment and install the dependencies:

```bash
pip install langchain langchain-openai langchain-google-genai python-dotenv
```

## Learning Outcomes

By exploring this project, you can learn how to:

- Initialize chat models using LangChain.
- Work with OpenAI and Google Gemini integrations.
- Send prompts using `invoke()`.
- Build an interactive AI Agent with `create_agent()`.
- Handle `HumanMessage` objects and AI responses.
- Maintain conversation history during a session.
- Manage API keys securely using environment variables.
