# Chat-with-PDFs
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <title>MultiPDF Chat App</title>
</head>

<body>
    <h1>MultiPDF Chat App</h1>
    <p>The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.</p>

    <h2>How It Works</h2>
    <img src="multipdf_chat_app_diagram.png" alt="MultiPDF Chat App Diagram">
    <p>The application follows these steps to provide responses to your questions:</p>

    <ol>
        <li>PDF Loading: The app reads multiple PDF documents and extracts their text content.</li>
        <li>Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.</li>
        <li>Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.</li>
        <li>Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.</li>
        <li>Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.</li>
    </ol>

    <h2>Dependencies and Installation</h2>
    <p>To install the MultiPDF Chat App, please follow these steps:</p>

    <ol>
        <li>Clone the repository to your local machine.</li>
        <li>Install the required dependencies by running the following command:</li>
    </ol>

    <pre><code>pip install -r requirements.txt</code></pre>

    <p>Obtain an API key from OpenAI and add it to the .env file in the project directory.</p>

    <pre><code>OPENAI_API_KEY=your_secret_api_key</code></pre>

    <h2>Usage</h2>
    <p>To use the MultiPDF Chat App, follow these steps:</p>

    <ol>
        <li>Ensure that you have installed the required dependencies and added the OpenAI API key to the .env file.</li>
        <li>Run the main.py file using the Streamlit CLI. Execute the following command:</li>
    </ol>

    <pre><code>streamlit run app.py</code></pre>

    <p>The application will launch in your default web browser, displaying the user interface.</p>

    <p>Load multiple PDF documents into the app by following the provided instructions.</p>

    <p>Ask questions in natural language about the loaded PDFs using the chat interface.</p>

    <p>Access the MultiPDF Chat App project <a href="https://ozzychatpdfs.streamlit.app/">here</a>.</p>
</body>

</html>
