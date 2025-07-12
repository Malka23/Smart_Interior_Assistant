import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

TEXT_GEN_API = "https://api-inference.huggingface.co/models/google/flan-t5-large"
IMG_GEN_API = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def generate_text(prompt):
    response = requests.post(TEXT_GEN_API, headers=headers, json={"prompt": prompt})
    if response.status_code == 200:
        return response.json()["generated_text"]
    else:
        return "Error generating text. Please try again"


def generate_image(prompt):
    response = requests.post(IMG_GEN_API, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.content  # raw image bytes
    else:
        st.error("⚠️ Error generating image.")
        return None
#Streamlit UI
st.set_page_config(page_title="Smart Interior Assistant", layout="centered")
st.title("🛋️ Smart Interior Assistant")
st.markdown("Describe your room and style — AI will design and visualize it!")
#inputs
room = st.text_input("Enter the type of room", placeholder="e.g., Bedroom, Living Room")
style = st.text_input("Enter the interior style or mood", placeholder="e.g., Scandinavian, Bohemian")

if st.button("✨ Generate Design"):
    if room and style:
        user_prompt = f"Describe a {style} style interior design for a {room}. Include furniture, layout, lighting, and colors."

        with st.spinner("Generating interior description..."):
            description = generate_text(user_prompt)
            st.markdown("### 📝 Design Description")
            st.write(description)

        with st.spinner("Creating image..."):
            image_bytes = generate_image(user_prompt)
            if image_bytes:
                st.image(image_bytes, caption=f"{style} {room}", use_column_width=True)
    else:
        st.warning("Please fill in both the room and the style.")



