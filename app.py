import streamlit as st
import requests
import json

# Streamlit UI
st.set_page_config(page_title="Ollama Chat App", page_icon="🤖")
st.title("🤖 Ollama Chatbot (Python Frontend)")
st.write("Chat with a local AI model using Ollama")

# User input
prompt = st.text_area("Enter your question:", height=120)

model = st.selectbox(
    "Choose a model",
    ["tinyllama", "mistral", "phi"]
)

if st.button("Generate Response"):
    if prompt.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            url = "http://localhost:11434/api/generate"
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False
            }

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success("Response:")
                st.write(result["response"])
            else:
                st.error("Failed to connect to Ollama.")