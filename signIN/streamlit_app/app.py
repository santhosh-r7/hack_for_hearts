import streamlit as st
import PyPDF2  # For PDFs
from docx import Document  # For DOCX files
import google.generativeai as genai
from dotenv import load_dotenv
import os
from os import environ
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

load_dotenv()

# Streamlit UI setup
st.markdown(
    """
    <style>
    .appview-container .main .block-container {
        padding-top: 2rem;
        margin: 0;
    }
    .css-usj992 {
        background-color: transparent;
    }
    .subtitle {
        margin-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<h1 style='text-align: center; padding: 10px;'>SimpliMedi-Assist</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h5 class='subtitle' style='text-align: center; padding: 2px;'>Your Health in Plain English</h5>",
    unsafe_allow_html=True
)

# Create a Streamlit file uploader widget
uploaded_file = st.file_uploader("Upload a PDF, DOCX, or TXT file", type=["pdf", "docx", "txt"])


#print ("Document contains content: ", result.content)
endpoint = "https://medical-jayadeva154.cognitiveservices.azure.com/"
key = "c7c09888fc3f436092218e8b26081185"
url = input("enter url: ")
document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))
    
poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", url)
result = poller.result()

print ("Document contains content: ", result.content)
# Check if a file has been uploaded
if uploaded_file is not None:
    # Load the document
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "pdf":
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join(
            pdf_reader.pages[page_num].extract_text()
            for page_num in range(len(pdf_reader.pages))
        )
    elif file_extension == "docx":
        # Extract text from DOCX
        docx_document = Document(uploaded_file)
        text = "".join(paragraph.text + "\n" for paragraph in docx_document.paragraphs)
    elif file_extension == "txt":
        # Read text directly from TXT file
        text = uploaded_file.getvalue().decode("utf-8")

    st.markdown("### Data Preview")

    formatted_text = text.replace('\n', '<br>')
    # Create a preview with custom HTML and CSS
    preview_html = """
    <style>
    .preview-container {
        border: 2px solid #007BFF;  # Blue border
        border-radius: 5px; 
        overflow-y: auto; 
        height: 500px; 
        padding: 10px;
    }
    </style>
    <div class="preview-container">""" + formatted_text + "</div>"

    st.markdown(preview_html, unsafe_allow_html=True)
    model=genai.GenerativeModel('gemini-1.5-flash')
   
    # Set up Gemini API key
    genai.configure(api_key="AIzaSyBhyFFNAHyk6I-8akKm1oPIhO_IsKjGYxY")
    prompt = text + " explain any technical or medical terms in original words with explanation in brackets. Also suggest conditions for the given health symptoms "

   
    response =  model.generate_content(prompt)

    # Display the response
    st.markdown("### Explanation")
    st.write(response.text)


    
