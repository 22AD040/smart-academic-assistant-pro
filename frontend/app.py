import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "app"))

import streamlit as st
import requests
from auth.auth import login, register, save_chat, get_chat

API = "https://smart-academic-assistant-pro.onrender.com/ask"
BUILD_API = "https://smart-academic-assistant-pro.onrender.com/build"

st.set_page_config(page_title="Smart AI Assistant", layout="wide")

st.markdown("""
<style>
body { background-color: #0e1117; }
h1, h2, h3, h4 { color: white; }

.stTextInput input {
    background-color: #1c1f26;
    color: white;
    border-radius: 12px;
    padding: 10px;
}

.stButton button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    font-weight: bold;
}

.user-box {
    background: #2b313e;
    color: #ffffff;
    padding: 12px;
    border-radius: 10px;
    margin: 10px 0;
}

.chat-box {
    background: #111827;
    color: #00ffcc;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
    font-size: 15px;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

if "user" not in st.session_state:
    st.session_state.user = None

if "messages" not in st.session_state:
    st.session_state.messages = []


if not st.session_state.user:

    st.title("🎓 Smart Academic Assistant")
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            if not username or not password:
                st.warning("⚠️ Please enter credentials")
            else:
                with st.spinner("Logging in..."):
                    if login(username, password):
                        st.session_state.user = username
                        st.success("✅ Logged in")
                        st.rerun()
                    else:
                        st.error("❌ Invalid credentials")

    with tab2:
        new_user = st.text_input("New Username", key="reg_user")
        new_pass = st.text_input("New Password", type="password", key="reg_pass")

        if st.button("Register"):
            if not new_user or not new_pass:
                st.warning("⚠️ Fill all fields")
            else:
                with st.spinner("Registering..."):
                    if register(new_user, new_pass):
                        st.success("✅ Registered")
                    else:
                        st.error("❌ Username exists")


else:

    st.sidebar.title("👤 User Panel")
    st.sidebar.write(f"Welcome, {st.session_state.user}")

    if st.sidebar.button("🆕 New Chat"):
        st.session_state.messages = []
        st.rerun()

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.session_state.messages = []
        st.rerun()

    st.sidebar.markdown("## 📄 Upload PDF")
    uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:


        if uploaded_file.size > 5 * 1024 * 1024:
            st.sidebar.warning("⚠️ Upload smaller PDF (<5MB)")

        else:
            st.sidebar.success("✅ PDF Uploaded")


            st.sidebar.info("⏳ Processing PDF... this may take 1-3 minutes")

            with st.spinner("Processing PDF..."):
                try:
                    res = requests.post(
                        BUILD_API,
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                "application/pdf"
                            )
                        },
                        timeout=300
                    )

                    if res.status_code == 200:
                        st.sidebar.success("✅ PDF processed successfully")
                    else:
                        st.sidebar.error("❌ Failed to process PDF")

                except Exception as e:
                    st.sidebar.warning(f"⚠️ Backend error: {e}")


    st.sidebar.markdown("## 💬 Chat History")
    history = get_chat(st.session_state.user)

    for i, chat in enumerate(history[-10:]):
        if st.sidebar.button(chat["q"], key=f"chat_{i}"):
            st.session_state.messages = [
                {"role": "user", "content": chat["q"]},
                {"role": "assistant", "content": chat["a"]}
            ]


    st.title("🤖 Smart Academic Assistant")
    query = st.text_input("Ask your question...")
    chat_container = st.container()

    if st.button("Ask"):
        if query.strip():
            st.session_state.messages.append({"role": "user", "content": query})

            try:
                res = requests.post(API, json={"question": query}, timeout=60)

                if res.status_code == 200:
                    answer = res.json().get("answer", "⚠️ No response")
                else:
                    answer = f"❌ API Error: {res.status_code}"

            except Exception as e:
                answer = f"⚠️ {e}"

            st.session_state.messages.append({"role": "assistant", "content": answer})
            save_chat(st.session_state.user, query, answer)

            st.session_state.scroll = True
            st.rerun()

    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"<div class='user-box'>🧑 {msg['content']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-box'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

    if st.session_state.get("scroll", False):
        st.markdown(
            "<script>window.scrollTo(0, document.body.scrollHeight);</script>",
            unsafe_allow_html=True
        )
        st.session_state.scroll = False