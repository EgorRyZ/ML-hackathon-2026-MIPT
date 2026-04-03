import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt



feature_names = {
    "Тип предприятия": "Тип предприятия",
    "Количество хостов": "Количество хостов",
    "Код реализованной угрозы": "Код угрозы",
    "Регион размещения предприятия": "Регион",
    "month": "Месяц",
    "weekday": "День недели",
    "hour": "Час",
    "is_weekend": "Выходной",
    "season": "Сезон",
    "Успех": "Успешная атака",
    "Нарушение конфиденциальности": "Нарушена конфиденциальность",
    "Нарушение целостности": "Нарушена целостность"
}



# === загрузка модели ===

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")



uploaded_file = st.file_uploader(
    "Загрузите Excel файл",
    type=["xlsx"]
)

if uploaded_file:

    df = pd.read_excel(uploaded_file)

    preds = model.predict(df)

    df["Prediction"] = preds

    st.write(df.head())

# st.write("Колонки модели:")
# st.write(columns)
# === загрузка Excel ===


if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.write("Загруженные данные:")
    st.write(df.head())

    # предсказания
    preds = model.predict(df)

    df["Prediction"] = preds

    st.write("Результаты:")
    st.write(df.head())

    # кнопка скачивания
    st.download_button(
        label="Скачать результат",
        data=df.to_csv(index=False).encode(),
        file_name="predictions.csv",
        mime="text/csv"
    )
    



st.header("Важность признаков")

importances = model.feature_importances_


feat_df = pd.DataFrame({
    "feature": columns,
    "importance": importances
})

feat_df["feature"] = feat_df["feature"].map(
    lambda x: feature_names.get(x, x)
)

# сортировка
feat_df = feat_df.sort_values(
    by="importance",
    ascending=True
)

# построение графика
fig, ax = plt.subplots()

ax.barh(
    feat_df["feature"],
    feat_df["importance"]
)

ax.set_xlabel("Важность")
ax.set_title("Диаграмма важности признаков")

st.pyplot(fig)



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

threat_code = st.number_input(
    "Код реализованной угрозы",
    min_value=0,
    max_value=300,
    value=1
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

inputs = {}


for col in columns:
    
    label = feature_names.get(col, col)

    inputs[col] = st.number_input(
    label,
    value=0
)

if st.button("Предсказать"):


    data = pd.DataFrame(
    [inputs],
    columns=columns
)

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        st.error(
            f"Есть риск нарушения доступности.\n"
            f"Вероятность: {probability:.2f}"
        )
    else:
        st.success(
            f"Риск низкий.\n"
            f"Вероятность: {probability:.2f}"
        )





# python -m streamlit run app.py