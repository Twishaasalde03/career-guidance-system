import streamlit as st
from src.career_guidance_system import run_conversation

st.set_page_config(page_title="AI Career Guide", page_icon="🧭", layout="centered")

st.title("🎓 AI Career Guidance System - Brain Wonders")
st.markdown("Tell me about your **interests**, **skills**, and what kind of career you’re looking for.")

# Input box
user_input = st.text_area("🗣️ Enter your conversation with the AI:", height=200)

# Button
if st.button("Get Career Recommendations"):
    if user_input.strip():
        with st.spinner("Analyzing your preferences and matching careers..."):
            response = run_conversation(user_input)
        st.success("✅ Recommendations Ready!")
        st.markdown("### 🧠 Result:")
        st.markdown(response)
    else:
        st.warning("Please enter some conversation input first.")
