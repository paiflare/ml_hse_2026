import random
import string

import streamlit as st


def make_password(length, use_special):
    symbols = string.ascii_letters + string.digits
    if use_special:
        symbols += string.punctuation
    return "".join(random.choices(symbols, k=length))


st.title("Генератор паролей")

with st.form("settings"):  # "settings" – ключ формы, у каждой формы свой
    length = st.slider("Длина", 8, 64, 16)
    use_special = st.checkbox("Спецсимволы")
    submitted = st.form_submit_button("Создать")

if submitted:
    st.code(make_password(length, use_special), language=None)
