import random
import string

import streamlit as st


def make_password(length, use_special):
    symbols = string.ascii_letters + string.digits
    if use_special:
        symbols += string.punctuation
    return "".join(random.choices(symbols, k=length))


st.title("Генератор паролей")

if "password" not in st.session_state:  # только в самом первом прогоне сессии
    st.session_state.password = None

length = st.slider("Длина", 8, 64, 16)
use_special = st.checkbox("Спецсимволы")

if st.button("Создать"):
    st.session_state.password = make_password(length, use_special)

if st.session_state.password:
    st.code(st.session_state.password, language=None)
