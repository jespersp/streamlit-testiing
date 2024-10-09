import streamlit as st

st.title('My first app')

name = st.text_input('What is your name?')
if st.button('Say hello'):
    st.write(f'Why hello there, {name}!')
    st.balloons()
