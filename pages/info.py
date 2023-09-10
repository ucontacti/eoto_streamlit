import streamlit as st
import pandas as pd
from prediction import predict

uploaded_file = st.file_uploader("Upload your file ...", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col="Id")
    st.dataframe(df)
    df["predicted"] = predict(df.drop("Species", axis=1))
    st.dataframe(df)