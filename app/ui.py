import streamlit as st
import requests

st.title("AI PDF Q&A System")

st.header("Upload PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
if uploaded_file:
    files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
    response = requests.post("http://localhost:8000/upload_pdf/", files=files)
    st.write(response.json())

st.header("Ask a Question")
query = st.text_input("Enter your question:")
if st.button("Submit Query") and query:
    response = requests.post("http://localhost:8000/query/", data={"query": query})
    result = response.json()
    st.write("**Answer:**", result.get("answer"))
    st.write("**Context:**", result.get("context"))
