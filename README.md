# AI-Powered Document Analyzer

## Overview
The AI-Powered Document Analyzer is a Streamlit-based web application that enables users to upload PDF documents and receive:
- **Short Summary:** A concise summary of the uploaded content.
- **Long Summary:** A more detailed summary.
- **Question & Answer (QA):** Ask questions about the uploaded document, and get AI-powered answers.
This project uses advanced natural language processing (NLP) models to read, understand, and generate insights from the uploaded documents.

## Features
- **Upload Documents:** Upload PDF files through a simple drag-and-drop interface.
- **Short and Long Summaries:** Generate tailored summaries of the content.
- **Interactive Q&A:** Ask any question about the document and get precise answers.
- **Streamlined UI:** Easy-to-use interface powered by Streamlit.

## How It Works
- **File Upload:** Users upload a PDF file.
- **Content Analysis:**
  - The PDF content is extracted and processed using a text extraction tool like PyPDF2 or similar libraries.
  - Summarization and Q&A functionality are powered by a generative AI model.
- **Output:**
  - Users can choose between generating a short or long summary or entering a question for interactive Q&A.
 
## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python
- **NLP Model:** Gemini 
- **Libraries:**
  - streamlit
  - PyPDF2 (for PDF extraction)

## Installation
- Prerequisites
  - Python 3.8+
  - pip (Python package manager)

- Steps
  - Clone the repository:
    - https://github.com/VasuGadde0203/AI-Powered-Document-Analyzer.git
  - Install the required dependencies
    - pip install -r requrirements.txt
  - Run the application
    - streamlit run app.py
 
## Contact
- **Author:** Gadde Vasu Ramesh
- **Email:** vasugadde0203@gmail.com
- **GitHub:** VasuGadde0203
