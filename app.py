import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from tavily import TavilyClient

load_dotenv()

# Configure APIs
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# Select the Model information

MODEL_INFO = "gemini-2.0-flash"
MODEL_SCRIPT = "gemini-2.0-flash" # can take different

st.set_page_config(
    page_title="YTForge Agent",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom modern CSS theme ---
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: #f5f5f5;
        }
        h1, h2, h3 {
            text-align: center;
            color: #F9FAFB !important;
        }
        .stTextInput>div>div>input {
            border: 1px solid #6EE7B7 !important;
            border-radius: 10px;
            padding: 12px;
            background-color: #111827;
            color: white !important;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #06b6d4, #3b82f6);
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            border: none;
            transition: 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #2563eb, #06b6d4);
        }
        .card {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            margin-top: 20px;
        }
        .stRadio > div {
            justify-content: center;
        }
        footer, .stCaption {
            text-align: center;
            color: #9CA3AF;
        }
    </style>
""", unsafe_allow_html=True)


def main():
    st.markdown("<h1>🌐YTForge Agent</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#D1D5DB;'>Search any topic — from world news to research trends — and get AI-powered insights & video scripts instantly 🚀</p>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
    