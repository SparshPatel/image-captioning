import streamlit as st
import os
import base64
from dotenv import load_dotenv
load_dotenv()
import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer " + os.getenv("HUGGINGFACE_API_KEY")}

def query(data):
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()[0]["generated_text"]

st.title("Image Captioning")
form = st.form(key="form")
image = form.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
o_image = st.container()
output = st.container()
submit = form.form_submit_button("Submit")

if image:
    o_image = st.image(image, caption="Uploaded Image", use_column_width=True)

if submit and image:
    output.markdown("")
    image_data = image.getvalue()
    caption = query(image_data)
    caption = caption.strip()
    if caption:
        output.write(caption)
    else:
        output.write("Please enter a caption")


