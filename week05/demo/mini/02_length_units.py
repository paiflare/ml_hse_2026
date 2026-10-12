import streamlit as st

METERS_IN = {"м": 1.0, "фт": 0.3048, "дюйм": 0.0254}  # сколько метров в одной единице

st.title("Конвертер длины")
st.write("Переводит длину между метрами, футами и дюймами.")

value = st.number_input("Длина", min_value=0.0, value=1.0, step=1.0)
unit_from = st.selectbox("Из", list(METERS_IN))  # list(словарь) – список его ключей
unit_to = st.selectbox("В", list(METERS_IN), index=1)  # index=1 – по умолчанию второй вариант

meters = value * METERS_IN[unit_from]  # сначала в метры
result = meters / METERS_IN[unit_to]  # потом из метров в нужную единицу

if value == 0:
    st.warning("Введите длину больше нуля.")
else:
    st.success(f"{value:.2f} {unit_from} = {result:.2f} {unit_to}")
