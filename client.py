#Here I'm going to create frontend(webapp) to interact with the api

import requests
import streamlit as st
def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

#Streamlit framework

st.title("LangChain Demo with OpenAI API")
input_text= st.text_input("Write an essay on")

if input_text:
    st.write(get_openai_response(input_text))
