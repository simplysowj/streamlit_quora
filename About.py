import streamlit as st
from PIL import Image

def About():

    st.title("All about Quora : ")
   
    image = Image.open('images/quora.png')
    st.image(image, caption='quora')
    
    image = Image.open('images/description1.png')
    st.image(image, caption='About')


    image = Image.open('images/des2.png')
    st.image(image, caption='description')

