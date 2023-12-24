from logging import warn
import streamlit as st
from load_gpt import load_gpt

st.write("This is Gpt-3.5 model that u can choose system personality")
col1, col2, col3,col4,col5 = st.columns(5)

with col1:
    temperature= st.number_input('temperature')
with col3:
    
   max_tokens= st.number_input('max_token')

System_Message_content= st.text_input('System_Message_content')

    
Human_Message_content= st.text_input('Human_Message_content')
    
button = st.button("Click to Start process")


if button:
    st.success(f'Welcome to llm')
    x=load_gpt(temperature,max_tokens,System_Message_content,Human_Message_content)
    st.write(f'your answer is {x}')