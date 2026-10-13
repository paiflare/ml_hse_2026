from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

MODEL_PATH = Path(__file__).parent / "model.joblib"
# __file__ – путь к этому файлу; parent – его папка; / – склеить с именем файла


@st.cache_resource  # прочитать файл один раз на весь сервер, общий для всех сессий
def load_model():
    return joblib.load(MODEL_PATH)


if not MODEL_PATH.exists():
    st.error("Нет файла model.joblib. Сначала выполните ноутбук train_model.ipynb.")
    st.stop()

model = load_model()
features = list(model.feature_names_in_)  # колонки, на которых модель училась

st.title("Уйдёт ли клиент")
st.caption("Логистическая регрессия на данных оператора связи.")

threshold = st.sidebar.slider("Порог «уйдёт»", 0.05, 0.95, 0.5, step=0.05)
# с какой вероятности считаем, что клиент уйдёт

with st.form("client"):
    left, right = st.columns(2)
    with left:
        accountlength = st.number_input("Срок обслуживания", min_value=1, max_value=250, value=100)
        totaldayminutes = st.slider("Минут разговоров днём", 0.0, 400.0, 180.0, step=1.0)
        customerservicecalls = st.number_input("Звонков в поддержку", min_value=0, max_value=10, value=1)
    with right:
        internationalplan = st.checkbox("Международный план")
        voicemailplan = st.checkbox("Голосовая почта")
    submitted = st.form_submit_button("Предсказать")

if submitted:
    # Одна строка в том же виде, что строка CSV: Yes / No модель переведёт сама
    client = pd.DataFrame([{
        "accountlength": accountlength,
        "internationalplan": "Yes" if internationalplan else "No",
        "voicemailplan": "Yes" if voicemailplan else "No",
        "totaldayminutes": totaldayminutes,
        "customerservicecalls": customerservicecalls,
    }])
    proba = model.predict_proba(client)[0, 1]
    # строка 0 – наш единственный клиент; колонка 1 – вероятность класса 1, «ушёл»

    st.metric("Вероятность ухода", f"{proba:.1%}")
    st.progress(float(proba))
    if proba >= threshold:
        st.error("Скорее уйдёт.")
    else:
        st.success("Скорее останется.")

st.subheader("Прогноз по файлу")
uploaded = st.file_uploader("CSV с клиентами", type="csv")  # пока файла нет – None
if uploaded is None:
    st.info("Загрузите CSV с теми же колонками, что ждут признаки модели.")
else:
    batch = pd.read_csv(uploaded)
    missing = [column for column in features if column not in batch.columns]
    if missing:
        st.error(f"В файле нет колонок: {', '.join(missing)}")
    else:
        # берём только колонки модели: в CSV могут быть и другие
        proba = model.predict_proba(batch[features])[:, 1]
        batch = batch.copy()
        batch["churn_proba"] = proba
        batch["churn_pred"] = proba >= threshold  # True – уйдёт при этом пороге
        st.metric("Уйдут по прогнозу", int(batch["churn_pred"].sum()))
        st.dataframe(batch.sort_values("churn_proba", ascending=False), hide_index=True)
        st.download_button(
            "Скачать прогнозы",
            data=batch.to_csv(index=False).encode("utf-8"),
            file_name="predictions.csv",
            mime="text/csv",
            on_click="ignore",  # скачивание не перезапускает файл
        )
