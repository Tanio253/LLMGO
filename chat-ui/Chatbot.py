import streamlit as st

from vector_database import vectorDB
import ura_llama
from prompt import get_examples, PROMPT_TEMPLATE


st.title("💬 Chatbot VIETSOVPETRO")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if message := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": message})
    st.chat_message("user").write(message)

    examples = get_examples(message)
    context = "\n".join([doc.page_content for doc in vectorDB.similarity_search(message)])

    prompt = PROMPT_TEMPLATE.format(examples=examples, context=context, question=message)
    msg = ura_llama.run(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
