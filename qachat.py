from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini pro model and get responce

model= genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.header("Gemini LLM Application")

#initialize session state

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
    
input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

if submit and input:
    responce=get_gemini_response(input)
    ##Add user query and responce to session  chat history
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The response is")
    for chunk in responce:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
        
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")