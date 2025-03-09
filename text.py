# Description: This script demonstrates how to use the Gemini API to generate text using the Streamlit library.
# The user can input a question, and the model will generate a response based on the input.

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st  
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

## load gemini model and get response
model = genai.GenerativeModel("gemini-1.5-pro")
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

## intialize streamlit app

st.set_page_config( page_title = "Q&A Demo")

st.header("Gemini LLM Application")
input = st.text_input("Enter your question here: ", key = "question")
submit = st.button("Ask the question")

## when submit is clicked
if submit:
    response = get_response(input)
    st.write(response)