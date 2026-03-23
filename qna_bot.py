from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.6
)

st.title("🤖 AskBuddy – AI QnA Bot")
st.markdown("My QnA Bot with LangChain and OpenAI !")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)
    

query = st.chat_input("Ask anything ?")
if query:
    st.session_state.messages.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"ai", "content":res.content})

