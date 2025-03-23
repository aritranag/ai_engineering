# Project Description

This project is a web application that creates a simple chatbot in local.
The chatbot can respond to user inputs and provide helpful information.

## Installation

To install the required packages, run the following command:

pip install -r requirements.txt

Also required, would be a local installation of Ollama. You can download it from [here](https://ollama.ai/download).

## Usage

1. Run the `index.py` file using Python: python index.py

2. Open your web browser and navigate to http://localhost:8501.

3. Start chatting with the chatbot by typing messages in the input field and pressing Enter.

4. The chatbot will respond to your queries and provide helpful information.

Streamlit tutorial - https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps

# How does it work

The project uses Streamlit for the UI.
It also has a local installation of Ollama, which is used to run the chatbot.

The util file contains functions to query the model and get the response, there are 2 versions of this function:

- one that returns the full response as a string
- another that streams the response in real-time

The index.py file contains the main code for the app. It uses Streamlit's chat_input() function to create an input field for user messages and st.chat_message() to display them.

This is the most basic version of a chatbot that can be built locally. We will continue to enhance this chatbot into something far better in subsequent modules.
