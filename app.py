import streamlit as st



def main():
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")

    st.header("Chat with multiple PDFs :books:")

    st.text_input("Pergunte Algo sobre seu PDF")

    with st.sidebar:
        st.subheader("Seus Documentos")
        st.file_uploader("Suba seu PDF aqui e click em 'Process': ")
        st.button("Process")



if __name__ == '__main__':
    main()