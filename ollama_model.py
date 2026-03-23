#You need to have the model in your system

from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:1b")

res = llm.stream("What is the stock price of Microsoft")

for chunk in res:
    print(chunk.content, end="")