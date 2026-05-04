import streamlit as st
import fitz
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-powered feedback!")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("Reading resume..."):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()

    st.success("Resume loaded!")

    if st.button("🔍 Analyze Resume"):
        with st.spinner("AI is analyzing..."):
            prompt = f"""You are an expert HR and resume coach.
Analyze this resume and provide:
1. ✅ Strengths (what is good)
2. ❌ Weaknesses (what is missing)
3. 💡 Improvements (specific suggestions)
4. 🎯 Job Roles that match this profile

Resume:
{text[:3000]}"""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )

            result = response.choices[0].message.content
            st.markdown("## 📊 Analysis Result")
            st.write(result)