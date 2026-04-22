from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

system = ("system", "You are a helpful assistant that answers questions accurately and concisely in a {style} style.")
user = ("user", "{question}")

prompt = ChatPromptTemplate.from_messages([system, user])

messages = prompt.format_messages(style="funny", question="What is the capital of France?")

for message in messages:
    print(f"{message.type}: {message.content}")

gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")
answer = gemini.invoke(messages)
print(answer.content)