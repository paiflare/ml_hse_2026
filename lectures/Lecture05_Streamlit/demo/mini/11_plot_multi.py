import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Графический калькулятор")

with st.sidebar:
    functions = st.multiselect("Функции", ["sin", "cos", "exp", "sqrt"], default=["sin", "cos"])
    x_min, x_max = st.slider("Диапазон x", -10.0, 10.0, (0.0, 10.0))
    show_grid = st.checkbox("Сетка", value=True)

if not functions:
    st.info("Выберите хотя бы одну функцию слева.")
    st.stop()
if x_min == x_max:
    st.error("Раздвиньте ручки: диапазон пустой.")
    st.stop()

x = np.linspace(x_min, x_max, 200)

fig, ax = plt.subplots()
for function in functions:  # по линии на каждую выбранную функцию
    ax.plot(x, getattr(np, function)(x), label=f"{function}(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
if show_grid:
    ax.grid()
st.pyplot(fig)
