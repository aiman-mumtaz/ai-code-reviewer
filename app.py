import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# --- UI CONFIG ---
st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 Smart Code Reviewer")
st.caption("Submit your code for a readability, structure, and maintainability audit.")

# --- SIDEBAR: REVIEW SETTINGS ---
with st.sidebar:
    st.header("Review Parameters")
    language = st.selectbox("Programming Language", ["Java", "Python", "JavaScript", "TypeScript", "C++"])
    strictness = st.slider("Strictness Level", 1, 5, 3)
    focus_area = st.multiselect(
        "Focus Areas", 
        ["Readability", "Design Patterns", "Security (OWASP)", "Performance", "Testability"],
        default=["Readability", "Design Patterns"]
    )

# --- MAIN UI ---
code_input = st.text_area("Paste your code here:", height=300, placeholder="public void legacyMethod()...")

# FIX: Added '2' to define the number of columns
col1, col2 = st.columns(2)
with col1:
    analyze_btn = st.button("Analyze Code", type="primary")

if analyze_btn and code_input:
    with st.spinner("Analyzing architecture..."):
        try:
            # Crafting the Professional System Prompt
            system_prompt = f"""
            You are a Senior Staff Engineer and Code Auditor. 
            Review the following {language} code specifically for:
            1. Readability: Is the naming intuitive? Is it self-documenting?
            2. Structure: Does it follow {language} best practices? (e.g., SOLID for Java, PEP8 for Python).
            3. Maintainability: Is the cyclomatic complexity too high? Are there hidden side effects?
            
            Focus heavily on: {', '.join(focus_area)}.
            Provide the review in Markdown with three sections: 
            ### ✅ The Good | ### ⚠️ Opportunities for Improvement | ### 🚀 Refactored Version.
            Strictness Level: {strictness}/5.
            """

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Review this code:\n\n{code_input}"}
                ],
                temperature=0.3,
                max_tokens=1500
            )

            # ✅ THE CRITICAL FIX: Added to access the first choice in the list
            review_content = completion.choices[0].message.content
            
            # --- DISPLAY RESULTS ---
            st.divider()
            st.markdown(review_content)
            st.success("Analysis Complete. Use the 'Refactored Version' to improve your PR.")

        except Exception as e:
            st.error(f"Analysis failed: {str(e)}")
            # Helpful debug info if it fails again
            if "completion" in locals():
                st.info("Debugging: Review the raw completion object in your terminal.")

elif analyze_btn and not code_input:
    st.warning("Please paste some code first!")

# --- FOOTER ---
st.markdown("---")
st.caption("Built for Engineering Excellence | SDE-2 Tooling")