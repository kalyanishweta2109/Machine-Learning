import numpy as np
import pickle
import pandas as pd
import streamlit as st 

#from PIL import Image -->used if there are images in dataset


pickle_in = open("log_r.pkl","rb")
log_r=pickle.load(pickle_in)


def welcome():
    return "Welcome All"

def predict_note_authentication(CLMSEX,CLMINSUR,SEATBELT,CLMAGE,LOSS):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: CLMSEX
        in: query
        type: number
        required: true
      - name: CLMINSUR
        in: query
        type: number
        required: true
      - name: SEATBELT
        in: query
        type: number
        required: true
      - name: CLMAGE
        in: query
        type: number
        required: true
      - name: LOSS
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    try:
        # Convert inputs to float
        CLMSEX = float(CLMSEX)
        CLMINSUR = float(CLMINSUR)
        SEATBELT = float(SEATBELT)
        CLMAGE = float(CLMAGE)
        LOSS = float(LOSS)

        # Log inputs for debugging
        #print("Inputs:", CLMSEX, CLMINSUR, SEATBELT, CLMAGE, LOSS)

        # Make prediction
        prediction = log_r.predict([[CLMSEX, CLMINSUR, SEATBELT, CLMAGE, LOSS]])
        print(prediction)
        return prediction
    except ValueError as e:
        print(f"ValueError: {e}")
        raise
    #prediction=log_r.predict([[CLMSEX,CLMINSUR,SEATBELT,CLMAGE,LOSS]])
    #print(prediction)
    #return prediction



def main():
    st.title("Claimants Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Claimants Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    CLMSEX = st.text_input("CLMSEX"," ")
    CLMINSUR = st.text_input("CLMINSUR"," ")
    SEATBELT = st.text_input("SEATBELT"," ")
    CLMAGE = st.text_input("CLMAGE"," ")
    LOSS=st.text_input("LOSS"," ")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(CLMSEX,CLMINSUR,SEATBELT,CLMAGE,LOSS)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
