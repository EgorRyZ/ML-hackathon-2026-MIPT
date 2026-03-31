import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


import matplotlib.pyplot as plt



# =========================
# 1. Загрузка данных
# =========================

incidents = pd.read_excel("incidents_2000.xlsx")
thrlist = pd.read_excel("thrlist.xlsx", header=1)


# =========================
# 2. Обработка дат
# =========================

incidents["Дата инцидента"] = pd.to_datetime(
    incidents["Дата инцидента"],
    dayfirst=True
)

incidents["Региональное время"] = pd.to_datetime(
    incidents["Региональное время"],
    dayfirst=True
)


# создаём признаки времени

incidents["month"] = incidents["Дата инцидента"].dt.month
incidents["weekday"] = incidents["Дата инцидента"].dt.weekday
incidents["hour"] = incidents["Региональное время"].dt.hour

incidents["is_weekend"] = (
    incidents["weekday"] >= 5
).astype(int)

incidents["season"] = (
    incidents["month"] % 12 // 3
)


# === дополнительные временные признаки ===


# =========================
# 3. Merge справочника
# =========================

df = incidents.merge(
    thrlist,
    left_on="Код реализованной угрозы",
    right_on="Идентификатор УБИ",
    how="left"
)


# =========================
# 4. Удаляем datetime
# =========================

datetime_cols = df.select_dtypes(
    include=["datetime64"]
).columns

df = df.drop(columns=datetime_cols)


# =========================
# 5. Удаляем утечку данных
# =========================

if "Идентификатор УБИ" in df.columns:
    df = df.drop(columns=["Идентификатор УБИ"])


# =========================
# 6. Заполняем пропуски
# =========================
# ===== удалить datetime =====

df = df.drop(
    columns=df.select_dtypes(
        include=["datetime64"]
    ).columns
)

# ===== удалить утечки =====
leak_cols = [
    "Идентификатор УБИ",
    "Наименование УБИ",
    "Описание",
    "Источник угрозы (характеристика и потенциал нарушителя)",
    "Объект воздействия",
    "Статус угрозы",
    "Замечания",
    "Код предприятия"
]

for col in leak_cols:
    if col in df.columns:
        df = df.drop(columns=[col])

# =========================
# 7. Кодируем категории
# =========================

cat_cols = df.select_dtypes(
    include="object"
).columns

encoders = {}

for col in cat_cols:
    le = LabelEncoder()

    df[col] = df[col].astype(str)

    df[col] = le.fit_transform(
        df[col]
    )

    encoders[col] = le


# =========================
# 8. Определяем цель
# =========================

target = "Нарушение доступности"

X = df.drop(columns=[target])
y = df[target]


# =========================
# 9. Train/Test split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


print(df["Нарушение доступности"].value_counts())


# =========================
# 10. Обучение модели
# =========================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)


# =========================
# 11. Предсказание
# =========================

y_pred = model.predict(X_test)


# =========================
# 12. Оценка модели
# =========================

print("\n=== RESULT ===\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)






importances = model.feature_importances_

feat_imp = pd.DataFrame({
    "feature": X.columns,
    "importance": importances
})

feat_imp = feat_imp.sort_values(
    by="importance",
    ascending=False
)

print(feat_imp.head(15))



#print("Число классов:")
#print(df["Код реализованной угрозы"].nunique())

#print("\nРазмеры классов:")
#print(df["Код реализованной угрозы"].value_counts().head(20))














#      precision    recall  f1-score   support
# 
#            0       0.78      0.70      0.74       107
#            1       0.89      0.93      0.91       293
#
#     accuracy                           0.87       400
#    macro avg       0.84      0.81      0.83       400
# weighted avg       0.86      0.87      0.87       400