import streamlit as st
import google.generativeai as genai

st.title("🔍 Gemini API Diagnostic")
api_key = st.text_input("Enter Gemini API Key", type="password")

if st.button("List Available Models"):
    if api_key:
        genai.configure(api_key=api_key.strip())
        st.subheader("Your Authorized Models:")
        try:
            for model in genai.list_models():
                st.write(model.name)
        except Exception as e:
            st.error(f"Error fetching models: {e}")
    else:
        st.warning("Please enter your API key first.")
