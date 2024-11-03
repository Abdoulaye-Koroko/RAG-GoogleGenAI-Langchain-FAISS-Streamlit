import os
import textwrap
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import (
PyPDFLoader,
TextLoader,
UnstructuredWordDocumentLoader,
UnstructuredPowerPointLoader
)


def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def load_pdf_file(file):
    loader = PyPDFLoader(file)
    documents = loader.load()
    all_doc_text = [doc.page_content for doc in documents]
    return all_doc_text

def load_txt_file(file):
    loader = TextLoader(file)
    documents = loader.load()
    all_doc_text = [doc.page_content for doc in documents]
    return all_doc_text

def load_word_file(file):
    loader = UnstructuredWordDocumentLoader(file)
    documents = loader.load()
    all_doc_text = [doc.page_content for doc in documents]
    return all_doc_text

def load_pptx_file(file):
    loader = UnstructuredPowerPointLoader(file)
    documents = loader.load()
    all_doc_text = [doc.page_content for doc in documents]
    return all_doc_text

def get_text_from_all_docs(filenames):
    texts = []
    for file in filenames:
        _, file_extension = os.path.splitext(file)
        if file_extension.lower() == '.pdf':
            texts.extend(load_pdf_file(file))
        elif file_extension.lower() == '.txt':
            texts.extend(load_txt_file(file))
        elif file_extension.lower() == '.docx':
            texts.extend(load_word_file(file))
        elif file_extension.lower() == '.pptx':
            texts.extend(load_pptx_file(file))
        else:
            raise ValueError(f"Insupported {file_extension.lower()}. Make sure you only uploaded pdf, txt, doc or pptx files ")
        os.remove(file)
    return " ".join(texts)
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3)

    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    #docs = new_db.similarity_search(user_question,k=5)
    docs = new_db.max_marginal_relevance_search(user_question,k=5,fetch_k=10)
    chain = get_conversational_chain()


    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    st.write(":green[Answer:]\n", to_markdown(response["output_text"]))