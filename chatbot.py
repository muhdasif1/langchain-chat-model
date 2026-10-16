from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
model = init_chat_model(model="gpt-6-luna")

# Customising your Model
model = init_chat_model(
    model="gpt-6-luna",
    temperature=1.0
)
question = input("Enter your question: ")
response = model.invoke(question)
print(response.content)