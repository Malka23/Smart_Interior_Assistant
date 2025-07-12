# Smart_Interior_Assistant
A simple and smart AI-powered app that generates interior design ideas and visual inspirations based on the type of room and desired style.
Built using **Streamlit** and **Hugging Face models** (`flan-t5` for text, `stable-diffusion` for image generation).

## ✨ Features

- 📝 AI-generated room design descriptions  
- 🖼️ Image generation with Stable Diffusion  
- ⚡ Simple and fast Streamlit UI  
- 🔐 API key management with `.env` and Streamlit Secrets

## 📦 Tech Stack

| Layer            | Tools Used                          |
|------------------|-------------------------------------|
| LLM (Text)       | `google/flan-t5-large`              |
| Diffusion(Image) | `stabilityai/stable-diffusion-2`    |
| Frontend         | `Streamlit`                         |
| API Access       | Hugging Face Inference API          |
| Security         | `.env` + Streamlit Cloud Secrets    |
