import streamlit as st
import time
from PIL import Image

# Add title
st.title("Sentiment Analysis testing at the server")
st.header('intro ')

st.subheader('sunheader')
# Optionally, include a delay to check for responsiveness
time.sleep(1)

st.text('text')
st.text('next we will see input')

# read input from user

input_text = st.text_input("Type something", "type here.........")
st.text(input_text)

input_text = st.text_area("Enter here","larger area")
st.markdown("jai ho ___jai ho___")
button = st.button("click me")
if button:
    st.text("ho gaya click")
    st.info("click ho gaya !snap me ") 

# st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMmjuocJDZz3JlQ1OVle_2F40GBhx6R8ieskfHgee7aEA9KhiV", width = 300)
selection = st.multiselect("Choose model",  ["NLP","Image","Audio"])
st.write(selection) 
