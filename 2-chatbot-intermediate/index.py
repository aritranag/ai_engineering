import streamlit as st
from util.model_util import model_list, query_model_stream

# Intermediate chat app - remembers the chat
model = model_list['gemma']

prompt = st.chat_input(placeholder='Enter your question here...')
system_role = "You are a helpful assistant"

# Setting up the title
st.title("Chat")


# Add a bit of memory to the chat, such that we can continue the conversation
if "messages" not in st.session_state:
    # session state is a dictionary that stores the chat history
    st.session_state["messages"] = []

# Lets show all the messages in app rerun by looping through the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt:
    print('User prompt : ',prompt)
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # Now we will construct the prompt
    prompt = st.session_state.messages

    with st.chat_message('assistant'):
        stream = query_model_stream(model=model, query=prompt,system_role=system_role)
        response = st.write_stream(stream)
    
    st.session_state.messages.append({'role': 'assistant', 'content': response})
