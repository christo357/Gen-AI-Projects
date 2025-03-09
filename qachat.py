from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

## function to load gemini pro and get response
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=False)
    return response

## initialize our streamlit app
st.set_page_config(page_title="Q&A bot")

st.header("Gemini LLM Application")

if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []
    
input = st.text_input("Input", key="input")
submit = st.button("Ask Gemini")

if submit and input:
    response = get_gemini_response(input)
    
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    
    st.subheader("The Response is")
    st.write(response.text)
    
    # st.write(chunk.text)
    st.session_state['chat_history'].append(("Bot", response.text))
    
st.subheader("The Chat History is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")