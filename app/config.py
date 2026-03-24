import streamlit as st

GEMINI_API_KEY = st.secrets["gemini_api_key"]

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 3
FAISS_PATH = "faiss_index"