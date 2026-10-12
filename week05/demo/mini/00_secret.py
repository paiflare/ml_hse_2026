import time

import streamlit as st  # принято сокращать до st

PASSWORD = "streamlit"

st.title("Секрет за паролем")  # самый крупный заголовок страницы
st.write("Введите пароль, чтобы увидеть секрет.")  # обычный текст

password = st.text_input("Пароль", type="password")  # вместо символов – звездочки

if password == "":
    st.info("Введите пароль и нажмите Enter.")
elif password == PASSWORD:
    st.success("Пароль верный.")
    st.write("Секрет: СЕКРЕТ Мухехе.")
else:
    st.error("Пароль неверный")

st.caption(f"Скрипт выполнен в {time.strftime('%H:%M:%S')}")
