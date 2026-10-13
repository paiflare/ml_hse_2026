import random
import string

import streamlit as st


def make_password(length, use_special):
    symbols = string.ascii_letters + string.digits
    if use_special:
        symbols += string.punctuation
    return "".join(random.choices(symbols, k=length))


def generate():
    # Колбэк работает до перезапуска: свежие значения виджетов – в session_state по key
    st.session_state.password = make_password(
        st.session_state.length,
        st.session_state.use_special,
    )


st.title("Генератор паролей")

if "password" not in st.session_state:
    st.session_state.password = None

st.slider("Длина", 8, 64, 16, key="length", on_change=generate)
st.checkbox("Спецсимволы", key="use_special", on_change=generate)
st.button("Создать", on_click=generate)

if st.session_state.password:
    st.code(st.session_state.password, language=None)
