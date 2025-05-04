from ollama import chat
from ollama import ChatResponse


model_list = {
    'llama': 'llama3.1:8b',
    'gemma' : 'gemma3:4b',
}


# Mostly the streaming model will be used in chatbots
# The general response model is for testing purposes
def query_model_stream(model=model_list['gemma'], query = [], system_role=None):
    '''
    @param model: the name of the model to use for querying
    @param query: the query to send to the model, this is a full query with the role and content
    @param system_role: the role of the system in the conversation
    '''
    if query is None or len(query) == 0:
        raise ValueError('Query cannot be empty')
    
    for q in query:
        messages = [
            {"role" : q['role'],"content" : q['content']}
            for q in query
        ]
    
    if system_role is not None:
        messages = [{'role': 'system', 'content': system_role}] + messages

    stream = chat(model=model, messages=messages,stream=True)
    
    for chunk in stream:
        yield (chunk['message']['content'])