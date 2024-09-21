import os
from dotenv import load_dotenv
import google.generativeai as genai

from utils import *

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    st.set_page_config("Chat with your pdf files")
    st.header("Chat with your pdf documents using Gemini")

    user_question = st.text_input("Ask anything you want to know from the uploaded files")

    if user_question:
        try:
            user_input(user_question)
        except Exception:
            st.write(':red[No pdf document is provided. You need to upload a pdf file before asking questions!]')
            
    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your pdf files and click on the Process button", accept_multiple_files=True)
        if st.button("Process"):
            try:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Vector database successfully created. You can start asking questions")
            except Exception:
                st.write(":red[Error during processing. Make sure you uploaded a valid pdf file!]")
                
                    

if __name__ == "__main__":
    main()