import os
import gradio as gr
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
os.environ['OPENAI_API_KEY'] = ''

llm = OpenAI()
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])
    def respond(message, chat_history):
        bot_message = conversation.invoke(message)['response']
        chat_history.append((message, bot_message))
        return "", chat_history
    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()