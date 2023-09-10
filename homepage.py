import streamlit as st
import numpy as np
from prediction import predict
from PIL import Image

st.title('Classifying Iris Flowers')


st.markdown('Example toy model to classify iris flowers. based on their \
             sepal/petal and length/width.')


st.header("Plant Features")
col1, col2 = st.columns(2)

with col1:
    st.text("Sepal characteristics")
    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 1.5)
    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 2.5)

with col2:
    st.text("Pepal characteristics")
    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 1.5)
    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)


image = Image.open("data/sepal-petal.jpg")
st.image(image)

st.text('')
if st.button("Predict type of Iris"):
    result = predict(
        np.array([[sepal_l, sepal_w, petal_l, petal_w]]))
    st.text(result[0])
