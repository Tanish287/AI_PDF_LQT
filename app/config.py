# Configuration file for environment variables and settings
import os

PDF_FOLDER = os.getenv("PDF_FOLDER", "sample_pdfs")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_db.index")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
