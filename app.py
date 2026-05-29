import streamlit as st
from utils.pdf_reader import extract_pdf_text
from utils.llm import generate_response

st.title("🩺 Medical Report Analyzer")

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf"]
)

if uploaded_file:

    text = extract_pdf_text(uploaded_file)

    st.subheader("Extracted Text")
    st.write(text[:1000])

    if st.button("Analyze Report"):

        prompt = f"""
        Explain this medical report in simple language.

        Report:
        {text}

        Mention:
        1. Important values
        2. Abnormal values
        3. Possible meaning

        Do not provide diagnosis.
        """

        response = generate_response(prompt)

        st.subheader("Analysis")
        st.write(response)