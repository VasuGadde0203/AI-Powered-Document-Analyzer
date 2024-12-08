import streamlit as st
from helper import *

# Streamlit UI
st.title("PDF Assistant")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf", 'mp4', 'wav', 'mkv', 'mp3'])

if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1].lower()
    with st.spinner(f"Processing {file_type.upper()} file..."):
        if file_type == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        
        else:
            st.error("Unsupported file type!")
            st.stop()
    st.success(f"{file_type.upper()} file processed successfully!")

    # Buttons for Summary and QA side by side
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Short Summary"):
            with st.spinner("Generating short summary..."):
                short_summary = summarize_text(extracted_text, summary_type="short")
            st.text_area("Short Summary", short_summary, height=200)

    with col2:
        if st.button("Long Summary"):
            with st.spinner("Generating long summary..."):
                long_summary = summarize_text(extracted_text, summary_type="long")
            st.text_area("Long Summary", long_summary, height=200)

    with col3:
        if st.button("Ask a Question"):
            st.session_state.show_qa = True  # Set flag to show QA section

    if "show_qa" in st.session_state and st.session_state.show_qa:
        question = st.text_input("Enter your question here")
        if st.button("Submit Question"):
            if question:
                with st.spinner("Answering your question..."):
                    answer = ask_question(extracted_text, question)
                st.text_area("Answer", answer, height=200)
            else:
                st.warning("Please enter a question to get an answer.")