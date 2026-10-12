
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage

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
