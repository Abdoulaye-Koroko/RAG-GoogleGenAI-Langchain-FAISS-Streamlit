import os
from dotenv import load_dotenv
import google.generativeai as genai

from utils import *

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def main():
    st.set_page_config("Chat with your files")
    st.header("Chat with your pdf, word, pptx and txt documents using Gemini")

    user_question = st.text_input("Ask anything you want to know from the uploaded files")

    if user_question:
        try:
            user_input(user_question)
        except Exception:
            st.write(':red[No pdf document is provided. You need to upload a file before asking questions!]')

    with st.sidebar:
        st.title("Menu")
        uploaded_files = st.file_uploader("Upload your files and click on the Process button",
                                          accept_multiple_files=True,
                                          type=["pdf", "txt", "docx", "pptx"])
        filenames = []
        for uploaded_file in uploaded_files:
        # Save each uploaded file to a temporary location
            file_path = uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Get the absolute path of the saved file
            absolute_path = os.path.abspath(file_path)
            filenames.append(absolute_path)
        
        if st.button("Process"):
            try:
                with st.spinner("Processing..."):
                    raw_text = get_text_from_all_docs(filenames)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Vector database successfully created. You can start asking questions")
            except Exception as e:
                st.write(":red[Error during processing. See error details below.]")
                st.write(f"**Error details:** {e}")

                    

if __name__ == "__main__":
    main()