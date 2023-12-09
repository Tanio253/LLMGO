import unicodedata
import streamlit as st
from pyvi.ViTokenizer import tokenize

from vector_database import vectorDB
import ura_llama
from prompt import get_examples, PROMPT_TEMPLATE


st.title("💬 Chatbot VIETSOVPETRO")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if message := st.chat_input():
    message = unicodedata.normalize('NFKD', message.strip())
    st.session_state.messages.append({"role": "user", "content": message})
    st.chat_message("user").write(message)

    examples = get_examples(message)
    context = "\n\n".join([doc.metadata.get('original_content').strip() for doc in vectorDB.similarity_search(tokenize(message.lower()))[:2]])

    prompt = PROMPT_TEMPLATE.format(examples=examples, context=context, question=message)
    
    msg = ura_llama.run(prompt)
    print(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
