import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

model = joblib.load("Random_Search.pkl")

st.title("House Price Prediction App")

st.markdown("---")
bedroom = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
bathroom = st.number_input("Number of Bathrooms", min_value=1, max_value=10, value=2)
living_area = st.number_input("Living Area", min_value=500, max_value=10000, value=2000)
condition = st.number_input("Condition of house", min_value=1, max_value=5, value=3)
school = st.number_input("School number", min_value=1, max_value=10, value=7)
st.markdown("---")

x = np.array([[bedroom, bathroom, living_area, condition, school]])
pred = st.button("Predict Price")

if pred:
    price = int(model.predict(x)[0])
    st.write(f"The predicted price of the house is: ${price:,.2f}")
else:
    st.write("Please click the 'Prediction' button")
    