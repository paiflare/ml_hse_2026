# Неделя 5. Streamlit; решающие деревья и KNN

Запись лекции: [ММАД_ПИ_26_STREAMLIT | Интерактивные веб-приложения на Streamlit (11.10.2026)](https://leap-platform.ru/share/2c15bdeb-f457-4a48-8553-e820f80fc9ce)

**Лектор:** Гордей Зуев

[`05_Streamlit.md`](05_Streamlit.md) – конспект лекции. Демо и мини-приложения – в [`demo/`](demo/).

[`05_KNN_Decision_trees_RU.ipynb`](05_KNN_Decision_trees_RU.ipynb) – ноутбук семинара: метод ближайших соседей и решающие деревья.

## Лекция: Streamlit

Страница с уже обученной моделью: поля, кнопка, прогноз. Один файл на Python, без HTML и JavaScript. В конце пары у страницы есть ссылка, которую можно открыть с телефона.

Что понадобится:

```
pip install -r demo/requirements.txt
```

После установки мини-приложения запускаются из `demo/`:

```
streamlit run mini/00_secret.py --server.runOnSave true
```

Приложение с моделью – `demo/app.py`. Модель лежит в `demo/model.joblib`, ее даёт ноутбук `demo/train_model.ipynb`.
