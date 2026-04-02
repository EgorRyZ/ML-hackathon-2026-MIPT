import streamlit as st
import pandas as pd
import joblib

# === загрузка модели ===

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")

st.title("Предсказание нарушения доступности")

st.write(
    "Введите параметры инцидента:"
)

# === ввод данных ===

enterprise_type = st.number_input(
    "Тип предприятия",
    min_value=0,
    max_value=20,
    value=1
)

hosts = st.number_input(
    "Количество хостов",
    min_value=1,
    max_value=10000,
    value=100
)

region = st.number_input(
    "Регион",
    min_value=0,
    max_value=100,
    value=1
)

month = st.number_input(
    "Месяц",
    min_value=1,
    max_value=12,
    value=1
)

weekday = st.number_input(
    "День недели",
    min_value=0,
    max_value=6,
    value=1
)

hour = st.number_input(
    "Час",
    min_value=0,
    max_value=23,
    value=12
)

success = st.number_input(
    "Успех атаки",
    min_value=0,
    max_value=1,
    value=0
)

conf = st.number_input(
    "Нарушение конфиденциальности",
    min_value=0,
    max_value=1,
    value=0
)

integrity = st.number_input(
    "Нарушение целостности",
    min_value=0,
    max_value=1,
    value=0
)

season = st.number_input(
    "Сезон",
    min_value=0,
    max_value=3,
    value=0
)

is_weekend = st.number_input(
    "Выходной",
    min_value=0,
    max_value=1,
    value=0
)

# === кнопка ===

if st.button("Предсказать"):

    data = pd.DataFrame(
        [[
            enterprise_type,
            hosts,
            region,
            success,
            month,
            weekday,
            hour,
            is_weekend,
            season,
            conf,
            integrity
        ]],
        columns=columns
    )

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(
            f"Есть риск нарушения доступности\n"
            f"Вероятность: {probability:.2f}"
        )
    else:
        st.success(
            f"Риск низкий\n"
            f"Вероятность: {probability:.2f}"
        )