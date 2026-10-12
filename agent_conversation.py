
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage, AIMessage

load_dotenv()

agent = create_agent(model="openai:gpt-6-luna")

# First conversation
response = agent.invoke({
    "messages": [
        HumanMessage(content="What's the capital of the Moon?")
    ]
})

print("\n" + "=" * 45)
print("       FIRST CONVERSATION")
print("=" * 45)

for message in response["messages"]:
    if isinstance(message, HumanMessage):
        print(f"\n👤 HUMAN:\n{message.content}")
    elif isinstance(message, AIMessage):
        print(f"\n🤖 AI:\n{message.content}")

# Second conversation with history
response = agent.invoke({
    "messages": [
        HumanMessage(content="What's the capital of the Moon?"),
        AIMessage(content="The capital of the Moon is Luna City."),
        HumanMessage(content="Interesting, tell me more about Luna City")
    ]
})

print("\n" + "=" * 45)
print("       SECOND CONVERSATION")
print("=" * 45)

for message in response["messages"]:
    if isinstance(message, HumanMessage):
        print(f"\n👤 HUMAN:\n{message.content}")
    elif isinstance(message, AIMessage):
        print(f"\n🤖 AI:\n{message.content}")

print("\n" + "=" * 45)
print("       CONVERSATION FINISHED")
print("=" * 45)
