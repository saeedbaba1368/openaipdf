from logging import warn
import streamlit as st
from prompet_template import prompet_template
from langchain.llms import OpenAI

st.write("This is davinci model based template  ")
col1, col2, col3 = st.columns(3)

with col1:
    temperature= st.number_input('temperature')
with col3:
    
   input_variables= st.text_input('input_variable')


button = st.button("Click to Start process")
if button:
    st.success(f'Welcome to llm')
    x,llm=prompet_template(input_variables,temperature)
    st.write(f'your template is {x}')
    st.write(f'your answer is {llm}')
