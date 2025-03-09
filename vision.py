# Description: This script is a Streamlit application that uses the Gemini model to answer questions based on an image and a text prompt.
# The user can input a text prompt and upload an image, and the model will generate a response based on the input.


from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st  
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

## load gemini model and get response
model = genai.GenerativeModel("gemini-1.5-flash")
def get_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

## intialize streamlit app

st.set_page_config( page_title = "Q&A Demo")

st.header("Gemini LLM Application")
input = st.text_input("Input Prompt: ", key = "input")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
image = ""
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image( image, caption='Uploaded Image.')
submit = st.button("Ask the question")

## when submit is clicked
if submit:
    response = get_response(input, image)
    st.write(response)