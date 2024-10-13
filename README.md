# RAG Application with Gemini, LangChain, FAISS and Streamlit

This project is a Retrieval-Augmented Generation (RAG) application that allows you to chat with an uploaded PDF file. It leverages Gemini, LangChain, and FAISS for efficient document retrieval and interaction. The project uses Poetry for dependency management and Streamlit for user interface.

**Author**: Abdoulaye Koroko (abdoulayekoroko@gmail.com)

## Project Description

This application enables users to upload a PDF file and interact with its content through a chat interface. The core components include:
- **Gemini**: for advanced language understanding and generation.
- **LangChain**: to manage the conversational context and memory.
- **FAISS**: for efficient similarity search and document retrieval.
- **Streamlit**: for usage interface

## Installation

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Abdoulaye-Koroko/RAG-GoogleGenAI-Langchain-FAISS-Streamlit.git
    cd RAG-GoogleGenAI-Langchain-FAISS-Streamlit
    ```

2. **Install Poetry** (if not already installed):
    ```bash
    pip install poetry
    ```

3. **Install dependencies**:
    ```bash
    poetry install
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root directory and add your Gemini API key:
    ```env
    GOOGLE_API_KEY = <your_gemini_api_key>
    ```
    You can generate your Gemini API key for free at [Google AI Studio](https://ai.google.dev/aistudio?hl=fr)
## Usage

1. **Run the application**:
    ```bash
    poetry run streamlit run app/app.py
    ```
You will have an interface as follows:

![Application interface home](/home/korokoa/projects/GenAI/RAG-GoogleGenAI-Langchain-FAISS-Streamlit/examples/app_home.png)

2. **Upload a PDF file and compute the vector database**:
    - Open your browser and navigate to the local server address (usually `http://localhost:8501`).
    - Use the interface to upload a PDF file.
    - Click on Process button to compute the vector database


3. **Interact with the PDF**:
    - Start chatting with the content of the uploaded PDF by asking anything you would like to know about the uploaded documents:

    ![Application interface home](/home/korokoa/projects/GenAI/RAG-GoogleGenAI-Langchain-FAISS-Streamlit/examples/app.PNG)

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request. Any questions or suggestions ? Write me: abdoulayekoroko@gmail.com.

Thank you

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


