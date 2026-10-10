from dotenv import load_dotenv
load_dotenv()

# Model Providers (Google Generative AI)
from langchain_google_genai import ChatGoogleGenerativeAI
model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
response = model.invoke("What's the capital of the Pakistan?")
print(response.content)
