import streamlit as st
import helper
import pickle
from About import About
from predict import predict
from Explore import Explore
from bert_predict import bert_predict
import base64

page=st.sidebar.selectbox("Explore or predict or About or bert_predict",{"predict","Explore","About","bert_predict"})



model = pickle.load(open('Model_new/model.pkl','rb'))

st.header('Duplicate Question Detector')

if(page=="About"):

     About()

    
elif(page=="predict"):
    predict()
elif(page=="bert_predict"):
    bert_predict()

else:
    Explore()

