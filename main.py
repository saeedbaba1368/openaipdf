import streamlit as st
from create_styled_sidebar import create_styled_sidebar
from stc_html import stc_html
from load_env import load_env



def main():
    load_env()
    stc_html()
    create_styled_sidebar()

        
if __name__=="__main__" :
    main()