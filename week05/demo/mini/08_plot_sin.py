import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Графический калькулятор")

x = np.linspace(0, 10, 200)  # 200 чисел от 0 до 10 с равным шагом
y = np.sin(x)

fig, ax = plt.subplots()  # fig – вся картинка, ax – оси внутри неё
ax.plot(x, y)
st.pyplot(fig)  # вместо plt.show(): отправить картинку на страницу
