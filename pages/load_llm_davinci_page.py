
import streamlit as st
from load_davinci import load_davinci


col1, col2, col3,col4 = st.columns(4)
with col1:
    question= st.text_input('question')
with col2:
    temperature= st.number_input('temperature')
with col3:
    
   max_tokens= st.number_input('max_token')
    
button = st.button("Click to Start process")


if button:
	st.success(f'Welcome to llm')
	x,y=load_davinci(question,temperature,max_tokens)
	st.write(f'your answer is {x}')
	st.write(f'number of token is {y}')
	
    
	
