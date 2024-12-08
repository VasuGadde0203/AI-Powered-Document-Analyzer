from PyPDF2 import PdfReader
import google.generativeai as genai
from pydub import AudioSegment
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import os
import tempfile

genai.configure(api_key="your_api_key")


def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def summarize_text(text, summary_type="short"):
    prompt = f"Provide a {summary_type} summary of the following text:\n\n{text}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    result = response.candidates[0].content.parts[0].text
    result = result.replace("**", '')
    return result

def ask_question(text, question):
    
    prompt = f"The following is a document:\n{text}\n\nAnswer the question based on the document:\n{question}"
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    result = response.candidates[0].content.parts[0].text
    result = result.replace('**', '')
    return result 


