import streamlit as st
from groq import Groq
import os

# Setup Groq client
client = Groq(api_key="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")

# Streamlit page config
st.set_page_config(page_title="Agentic AI Powered", layout="centered")
st.markdown(
    """
    <style>
    .big-title {
        font-size: 32px;
        font-weight: 700;
        text-align: center;
        color: #4a7cfc;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: gray;
        margin-bottom: 2rem;
    }
    .response-box {
        background-color: #f4f6fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #d3d3d3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and subtitle
st.markdown('<div class="big-title">🧠 Agentic AI Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything', unsafe_allow_html=True)

# User input
with st.form("chat_form"):
    user_input = st.text_area("💬 Your Question", height=120)
    submitted = st.form_submit_button("🚀 Submit")

# If user submitted input
if submitted and user_input.strip() != "":
    with st.spinner("🧠 Thinking..."):
        try:
            completion = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="compound-beta"
            )
            response = completion.choices[0].message.content

            st.markdown("### 🤖 Groq's Response")
            st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

            # Optional tool call display
            if hasattr(completion.choices[0].message, "executed_tools"):
                st.markdown("### 🛠️ Tool Calls Used")
                st.json(completion.choices[0].message.executed_tools)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
