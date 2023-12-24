def create_styled_sidebar():
    import streamlit as st
    # Use the "with" syntax for Streamlit beta containers
    with st.sidebar:
        st.markdown("""
        <style>
            /* CSS to style the sidebar */
            .css-18e3th9 {
                background-color: #f1f1f1; /* Light grey background */
                color: #4f8bf9; /* Blue text */
                padding: 10px; /* Some padding around the content */
            }
            /* Style the header */
            .css-hxt7ib {
                font-weight: bold;
                font-size: 24px;
                margin-bottom: 10px; /* Space below the header */
            }
            /* Style the buttons */
            .css-1d391kg {
                background-color: #4f8bf9; /* Blue background */
                color: white; /* White text */
                margin-bottom: 5px; /* Space below the buttons */
            }
        </style>
        """, unsafe_allow_html=True)
      
        
        
        
    return True