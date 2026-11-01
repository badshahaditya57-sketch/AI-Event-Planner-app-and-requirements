import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (Wide Layout for Dashboard feel)
st.set_page_config(
    page_title="AI Event Planner Dashboard",
    page_icon="🎉",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar for API Configuration and Instructions
with st.sidebar:
    st.title("⚙️ Configuration")
    api_key = st.text_input("Enter Gemini API Key", type="password", help="Paste your Google AI Studio key here")
    st.markdown("---")
    st.markdown("### About")
    st.info("This GenAI-powered dashboard helps organize weddings, birthdays, and community events with budgets, timelines, checklists, and personalized ideas.")

# 3. Main Header Section
st.title("🎉 Event Planning Intelligence Dashboard")
st.markdown("Design your perfect event with AI-driven insights, budget forecasting, and structured timelines.")
st.markdown("---")

# 4. Input Section (Using Columns for a professional layout)
st.subheader("📋 Define Event Parameters")
col1, col2, col3 = st.columns(3)

with col1:
    event_type = st.selectbox("Event Category", ["Wedding", "Birthday", "Community Event", "Corporate Party", "Gala"])
with col2:
    budget = st.number_input("Total Budget (in INR)", min_value=1000, value=50000, step=5000)
with col3:
    guests = st.number_input("Estimated Guests", min_value=1, value=50, step=10)

extra_details = st.text_area("✨ Special Requirements or Themes", placeholder="E.g., Vintage theme, 100% vegan catering, outdoor evening setting...")

st.markdown("<br>", unsafe_allow_html=True)
generate_btn = st.button("🚀 Generate Comprehensive Event Plan", use_container_width=True, type="primary")

# 5. Output Generation Engine
if generate_btn:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API Key in the sidebar to generate the plan.")
    else:
        genai.configure(api_key=api_key.strip())
        model = genai.GenerativeModel('gemini-3.5-pro')
        
        with st.spinner("Analyzing parameters and computing your event dashboard..."):
            prompt = f"""
            Act as an expert luxury event planner. Create a highly structured plan for a {event_type} for {guests} guests with a budget of {budget} INR.
            Additional details: {extra_details}.
            
            Format the response strictly with clear markdown headers, lists, and tables where appropriate:
            ### 1. 🎨 Personalized Ideas & Theme Suggestions
            ### 2. 💰 Estimated Budget Breakdown
            ### 3. 📅 Preparation Timeline
            ### 4. ✅ Vendor & Task Checklist
            """
            
            response = model.generate_content(prompt)
            
            st.success("Dashboard successfully generated!")
            st.markdown("---")
            
            # Displaying the structured AI response in a clean container
            with st.container():
                st.markdown(response.text)
