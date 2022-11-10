import streamlit as st
import helper
import pickle

import base64

model = pickle.load(open('Model_new/model.pkl','rb'))

def predict():

    

    #st.header('Duplicate Question Detector')

    q1 = st.text_input('Enter question 1')
    q2 = st.text_input('Enter question 2')

    if st.button('Find'):
        query = helper.query_point_creator(q1,q2)
        result = model.predict(query)[0]
        print(result)

        if result == 1:
            st.header('Duplicate')
        elif result==0:
            st.header('Not Duplicate')
        else:
            st.header("unknown")
