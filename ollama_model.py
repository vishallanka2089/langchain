#You need to have the model in your system

from langchain_ollama import ChatOllama

llm = ChatOllama(model="gemma3:1b")

res = llm.invoke("Explain LLM Architecture in as much detail as possible")

print(res.content)