import os
import streamlit as st
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("Groq_API_Key")

st.title("Legal Aid Research Tool ⚖️")
st.sidebar.title("Upload Legal Documents")

pdf_docs = st.sidebar.file_uploader("Upload PDF Files", accept_multiple_files=True, type="pdf")

st.sidebar.title("Legal Document URLs")
urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_clicked = st.sidebar.button("Process Documents")
file_path = "faiss-store-legal.pkl"

main_placeholder = st.empty()

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

if process_clicked:
    raw_documents = []
    main_placeholder.text("Loading Documents >>> ✅✅✅")

    if pdf_docs:
        for pdf in pdf_docs:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                if page.extract_text():
                    text += page.extract_text()
            raw_documents.append(Document(page_content=text, metadata={"source": pdf.name}))

    active_urls = [url for url in urls if url.strip()]
    if active_urls:
        loader = SeleniumURLLoader(urls=active_urls)
        url_data = loader.load()
        raw_documents.extend(url_data)

    if not raw_documents:
        st.error("Please upload a PDF or enter a valid URL.")
    else:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=['\n\n', '\n', '.', ' ']
        )

        main_placeholder.text("Processing Legal Texts >>> ✅✅✅")
        docs = text_splitter.split_documents(raw_documents)

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(docs, embeddings)
        with open(file_path, "wb") as f:
            pickle.dump(vectorstore, f)

        main_placeholder.text("Legal Knowledge Base Created >>> ✅✅✅")
        time.sleep(2)

query = main_placeholder.text_input("Legal Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            
            legal_prompt = f"You are a legal aid assistant. Base your answer STRICTLY on the retrieved documents. Do not invent information. State clearly that this is not professional legal advice. Question: {query}"
            
            result = chain({"question": legal_prompt}, return_only_outputs=True)
            st.header("Legal Insights")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Reference Sources:")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(source)