import streamlit as st
import pandas as pd 

temp = st.file_uploader("stribng")
if(temp is not None):
    df= pd.read_csv(temp)
    st.dataframe(df.describe())