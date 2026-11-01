import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API
# For local testing, set an environment variable or hardcode temporarily
# On Streamlit Cloud, use st.secrets
api_key = st.secrets.get("GEMINI_API_KEY", "YOUR_LOCAL_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🎉 AI Celebration & Event Planner")
st.write("Plan weddings, birthdays, and community events in seconds.")

event_type = st.selectbox("Event Type", ["Wedding", "Birthday", "Community Event"])
budget = st.number_input("Total Budget (in INR)", min_value=1000, value=50000)
guests = st.number_input("Estimated Number of Guests", min_value=1, value=50)
extra_details = st.text_area("Any special themes or requirements?")

if st.button("Generate Event Plan"):
    with st.spinner("Generating budgets, timelines, and checklists..."):
        prompt = f"""
        Act as an expert event planner. Create a detailed plan for a {event_type} for {guests} guests with a budget of {budget} INR.
        Additional details: {extra_details}.
        
        Provide the output formatted in markdown with the following sections:
        1. **Personalized Ideas & Theme Suggestions**
        2. **Estimated Budget Breakdown**
        3. **Preparation Timeline**
        4. **Vendor Checklist**
        """
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error generating plan: {e}")
