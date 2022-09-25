import pickle

import streamlit as st

pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))


st.title("Laptop Predictor")

company = st.selectbox('Brand',df['Company'].unique())
