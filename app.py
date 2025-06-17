import streamlit as st
from groq import Groq

client = Groq(api_key="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")

# Streamlit UI
st.set_page_config(page_title="Groq Chatbot", layout="centered")
st.title("🧠 Groq Chatbot")
st.caption("Ask anything, powered by `compound-beta` model")

# Text input
user_input = st.text_area("Enter your message", height=100, placeholder="e.g., What is the current weather in Tokyo?")

if st.button("Submit") and user_input.strip() != "":
    with st.spinner("Thinking..."):
        try:
            completion = client.chat.completions.create(
                messages=[{"role": "user", "content": user_input}],
                model="compound-beta"
            )
            response = completion.choices[0].message.content
            st.markdown("### 🤖 Response:")
            st.write(response)
            
            # Optionally show tool calls (if any)
            if hasattr(completion.choices[0].message, "executed_tools"):
                st.markdown("### 🛠️ Tool Calls:")
                st.json(completion.choices[0].message.executed_tools)

        except Exception as e:
            st.error(f"An error occurred: {e}")
