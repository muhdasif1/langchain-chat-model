from dotenv import load_dotenv
load_dotenv()

# Initialising and invoking a model
from langchain.chat_models import init_chat_model
model = init_chat_model(model="gpt-6-luna")
response = model.invoke("What can you do?")
print(response.content)



# Customising your Model
model = init_chat_model(
    model="gpt-6-luna",
    temperature=1.0
)
question = input("Enter your question: ")
response = model.invoke(question)
print(response.content)

