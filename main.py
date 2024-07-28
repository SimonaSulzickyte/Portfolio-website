import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Simona Šulžickytė")
    content = """
    Hi, I hold a Bachelor's degree in Econometrics and a Master's degree in Data Analytics and Business Economics. 
    Having experience with Python, R and SQL, I possess the technical skills necessary to analyze and interpret data effectively. 
    I am a fast learner, good at time management and eager to discover new topics and tools to apply machine learning methods to real-world problems.
    """
    st.info(content)