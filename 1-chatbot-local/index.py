import streamlit as st
from util.model_util import model_list, query_model_stream

# Basic chat app - one shot
model = model_list['gemma']

prompt = st.chat_input(placeholder='Enter your question here...')

if prompt:
    print('User prompt',prompt)
    st.chat_message("user").write(prompt)
    with st.chat_message('assistant'):
        stream = query_model_stream(model=model, query=prompt)
        st.write_stream(stream)
