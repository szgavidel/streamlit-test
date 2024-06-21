# streamlit run test.py

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import streamlit as st 

st.radio("st.radio",["A","B","C"])
st.checkbox("st.checkbox")
st.multiselect("multiselect",['A','B','C']) 
st.slider("slider",min_value=0., max_value=1., step=0.05)
st.number_input("Number input field")
st.date_input("Date input field")
st.time_input("Time input field")
st.file_uploader("Upload file") 