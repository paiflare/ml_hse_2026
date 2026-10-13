import html

import streamlit as st

st.title("Свой HTML")

st.markdown("По умолчанию теги показываются как текст: <b>не жирный</b>")
st.markdown("А так рисуются: <b style='color: crimson'>жирный красный</b>", unsafe_allow_html=True)

st.html(
    """
    <div style="padding: 12px 16px; border: 2px solid #4a7bd0; border-radius: 8px;">
      <div style="font-size: 14px; color: gray;">Клиент 3301</div>
      <div style="font-size: 28px; font-weight: bold;">75%</div>
      <div>вероятность ухода</div>
    </div>
    """
)

name = st.text_input("Имя", value="<i>Гость</i>")
st.html(f"<p>Привет, {html.escape(name)}!</p>")  # escape – теги из ввода станут текстом
