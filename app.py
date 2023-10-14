import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

def get_pdf_text(pdf_docs):
    text = []
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text.append(page.extract_text())
    return "".join(text)

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter( 
        separator="\n", 
        chunk_size=1000, 
        chunk_overlap=200, 
        length_function=len
        )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory)
    return conversation_chain

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None


    st.header("Chat with multiple PDFs :books:")

    st.text_input("Pergunte Algo sobre seu PDF")

    with st.sidebar:
        st.subheader("Seus Documentos")
        pdf_docs = st.file_uploader(
            "Suba seu PDF aqui e click em 'Process': ", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                
                #get the text chunks
                text_chunks = get_text_chunks(raw_text)
                
                #create vector store
                vectorstore = get_vectorstore(text_chunks)

                #create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

    st.session_state.conversation

if __name__ == '__main__':
    main()