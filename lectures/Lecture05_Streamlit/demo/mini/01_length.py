import streamlit as st

st.title("Конвертер длины")
st.write("Переводит метры в футы.")

meters = st.number_input("Метры", min_value=0.0, value=1.0, step=0.5)
# min_value – меньше ввести нельзя: длина не бывает отрицательной
feet = meters / 0.3048  # в одном футе ровно 0.3048 метра

st.success(f"{meters:.2f} м = {feet:.2f} фт")
