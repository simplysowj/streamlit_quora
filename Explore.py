import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt
#import streamlit as st
from PIL import Image

def Explore():
    st.title("EDA")
    st.title("Number of duplicate(smilar) and non-duplicate(non similar) questions")
    image = Image.open('images/eda1.png')
    st.image(image, caption='Number of duplicate(smilar) and non-duplicate(non similar) questions')
    st.text("63.08percent of questions pair are not duplicates and 36.92percent of question pairs are duplicates.")

    st.text("We have 404290 training data points. And only 36.92percent are positive. ")
    
    st.title("Unique vs Repeated qids")
    image = Image.open('images/eda2.png')
    st.image(image, caption='Unique vs Repeated qids')

    st.title("Number of times question repeated")
    image = Image.open('images/eda3.png')
    st.image(image, caption='Number of times question repeated')

    st.text("When we include both question1 and question2 then count of total number of questions are 808574.")
    st.text("Out of these 808574 questions 537929 are unique questions and rest are repeated questions.")
    st.text("Most of the questions are repeated very few times. Only a few of them are repeated multiple times.")
    st.text("And we can notice that there is One question which is the most repeated one and it is repeated 157 times.")
    st.text("There are some questions with very few characters, which does not make sense. It will be taken care of later with Data Cleaning.")

    st.title("Word Cloud for preprocesssed question1:")
    image = Image.open('images/eda4.png')
    st.image(image, caption='Word Cloud for preprocesssed question1:')
    
    st.title("Word Cloud for preprocessed question2:")
    image = Image.open('images/eda5.png')
    st.image(image, caption='Word Cloud for preprocessed question2:')

    st.title("Word Cloud for Duplicate Question pairs")
    image = Image.open('images/eda6.png')
    st.image(image, caption='Word Cloud for Duplicate Question pairs')

    st.title("Word Cloud for Non-Duplicate Question pairs")
    image = Image.open('images/eda7.png')
    st.image(image, caption='Word Cloud for Non-Duplicate Question pairs')
    
    st.title("Plot count of length of words in Clean_q1_lem and Clean_q2_lem")
    image = Image.open('images/eda8.png')
    st.image(image, caption='Plot count of length of words in Clean_q1_lem and Clean_q2_lem')

    st.title("Visualization of basic features")
    image = Image.open('images/eda_basic_1.png')
    st.image(image, caption='Visualization of basic features')

    image = Image.open('images/eda_basic_2.png')
    st.image(image, caption='Visualization of basic features')
    
    image = Image.open('images/pair_plot.png')
    st.image(image, caption='Visualization of pair plot')

     
    image = Image.open('images/eda_adv.png')
    st.image(image, caption='Visualization of adv. features')



  
