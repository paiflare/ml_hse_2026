import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Графический калькулятор")

function = st.selectbox("Функция", ["sin", "cos", "exp", "sqrt"])

x = np.linspace(0, 10, 200)
y = getattr(np, function)(x)  # getattr(np, "sin") – то же, что np.sin

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
