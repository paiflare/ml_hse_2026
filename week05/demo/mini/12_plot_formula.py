import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Графический калькулятор")

with st.sidebar:
    formula = st.text_input("y =", value="sin(x) * x")
    x_min, x_max = st.slider("Диапазон x", -10.0, 10.0, (-10.0, 10.0))
    show_grid = st.checkbox("Сетка", value=True)

if x_min == x_max:
    st.error("Раздвиньте ручки: диапазон пустой.")
    st.stop()

x = np.linspace(x_min, x_max, 200)
try:
    # Только для своего компьютера: eval выполнит любой код, который ввели в поле
    y = eval(formula, vars(np) | {"x": x})
except Exception as error:
    st.error(f"Не получилось посчитать формулу: {error}")
    st.stop()

fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {formula}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
if show_grid:
    ax.grid()
st.pyplot(fig)
