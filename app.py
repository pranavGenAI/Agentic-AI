import os
import streamlit as st
from groq import Groq

# Set your API key securely
client = Groq(api_key="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")

st.set_page_config(page_title="Groq Assistant", layout="centered")
st.title("🛠️ Groq Assistant Tool")
st.caption("Switch between a Code Debugger and a Web Search Assistant using `compound-beta-mini`")

# Tool selector
tool_mode = st.radio("Select Tool Mode", ["🔍 Web Search Tool", "🐍 Code Debugger Tool"], horizontal=True)

# Prompt input
default_query = {
    "🔍 Web Search Tool": "What are common causes of 'CrashLoopBackOff' errors in Kubernetes?",
    "🐍 Code Debugger Tool": "Will this code throw an error? `a = [1, 2]; print(a[5])`"
}

query_input = st.text_area("Enter your query:", value=default_query[tool_mode], height=150)

# Set system message based on tool
system_prompt = {
    "🔍 Web Search Tool": "You are a web assistant who answers based on up-to-date internet knowledge. Search if needed.",
    "🐍 Code Debugger Tool": "You are a code assistant who helps debug code and explain errors. Execute if needed."
}[tool_mode]

if st.button("Submit Query"):
    with st.spinner(f"Running {tool_mode}..."):
        try:
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query_input}
                ],
                model="compound-beta-mini"
            )

            st.markdown("### 🤖 Groq Response")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Failed to fetch response: {e}")
