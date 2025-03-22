from ollama import chat
from ollama import ChatResponse


model_list = {
    'llama': 'llama3.1:8b',
    'gemma' : 'gemma3:4b',
}

def query_model(model=model_list['gemma'], query = None, system_role=None):
    '''
    @param model: the name of the model to use for querying
    @param query: the query to send to the model
    @param system_role: the role of the system in the conversation
    '''
    if query is None or len(query) == 0:
        raise ValueError('Query cannot be empty')
    messages = [{'role': 'user', 'content': query}]
    if system_role is not None:
        messages = [{'role': 'system', 'content': system_role}] + messages
    response : ChatResponse = chat(model=model, messages=[{'role': 'system', 'content': system_role}, {'role': 'user', 'content': query}])
    return response['message']['content']

# Mostly the streaming model will be used in chatbots
# The general response model is for testing purposes
def query_model_stream(model=model_list['gemma'], query = None, system_role=None):
    '''
    @param model: the name of the model to use for querying
    @param query: the query to send to the model
    @param system_role: the role of the system in the conversation
    '''
    if query is None or len(query) == 0:
        raise ValueError('Query cannot be empty')
    messages = [{'role': 'user', 'content': query}]
    if system_role is not None:
        messages = [{'role': 'system', 'content': system_role}] + messages
    stream = chat(model=model, messages=[{'role': 'system', 'content': system_role}, {'role': 'user', 'content': query}],stream=True)
    
    for chunk in stream:
        yield (chunk['message']['content'])
