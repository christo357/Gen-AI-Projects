from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai 

genai.configure(api_key = os.getenv('GEMINI_API_KEY'))

## Function to load Gemini Pro Vision
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        image_bytes = uploaded_file.getvalue()
        
        image_parts = [
            {
                "mime_type":uploaded_file.type,
                "data":image_bytes
            }
        ]
        
        return image_parts
    else:
        raise FileNotFoundError("No File uploaded")

# initialize the streamlit app
st.set_page_config(page_title="Multi Language Invoice Extractor")

st.header("Gemini Application")
input = st.text_input("Input Prompt :", key ="input")
uploaded_file = st.file_uploader("Choose an Image of the Invoice...",type = ["jpeg", "png", "jpg"],)
image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Invoice',use_container_width=True)
    
input_prompt = """
You are an expert in understanding invoice. We will upload an image as invoice
and you will have to answer any questions based on the uploaded invoice image
"""    
    
    
submit = st.button("Tell me about the invoice")
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input, image_data, input_prompt)
    st.subheader("The Response is:")
    st.write(response)

