import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Графический калькулятор")

function = st.selectbox("Функция", ["sin", "cos", "exp", "sqrt"])
x_min, x_max = st.slider("Диапазон x", -10.0, 10.0, (0.0, 10.0))
# value – кортеж из двух чисел: у ползунка две ручки, и вернёт он тоже кортеж

if x_min == x_max:
    st.error("Раздвиньте ручки: диапазон пустой.")
    st.stop()  # дальше строить нечего: этот прогон заканчивается здесь

x = np.linspace(x_min, x_max, 200)
y = getattr(np, function)(x)

fig, ax = plt.subplots()
ax.plot(x, y, label=f"{function}(x)")  # label – подпись линии для легенды
ax.set_title(f"График {function}(x)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)
