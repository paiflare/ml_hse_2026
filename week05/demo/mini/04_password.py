import random
import string

import streamlit as st

st.title("Генератор паролей")

length = st.slider("Длина", 8, 64, 16)  # от 8 до 64, по умолчанию 16
use_special = st.checkbox("Спецсимволы")  # True, пока галочка стоит

if st.button("Создать"):
    symbols = string.ascii_letters + string.digits
    if use_special:
        symbols += string.punctuation
    password = "".join(random.choices(symbols, k=length))
    st.code(password, language=None)  # моноширинный блок с кнопкой копирования
