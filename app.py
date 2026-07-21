from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Creating OWN prompt 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Question={question}")
])

#Streamlit 
st.title("My Chat App")
input_text = st.text_input("Enter your message:")

#Using LLM model (gemma)

llm = Ollama(model="gemma:latest")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

#Validation based input

if input_text:
    st.write(chain.invoke({"question": input_text}))

