import time

import streamlit as st


@st.cache_data
def slow_square(number):
    time.sleep(3)  # притворяемся тяжёлым расчётом
    return number * number


number = st.slider("Число", 1, 10, 5)
st.write("Квадрат:", slow_square(number))
