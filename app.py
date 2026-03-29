import streamlit as st
import pandas as pd
import pickle

with open('car_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="AI Car Price Predictor", page_icon="🚗")
st.title("🚗 Предсказание стоимости автомобиля")
st.write("Введите параметры автомобиля ниже, чтобы узнать его примерную рыночную стоимость.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    horsepower = st.slider("Мощность (л.с.)", 40, 500, 120)
    enginesize = st.number_input("Объем двигателя", 50, 500, 150)
    curbweight = st.number_input("Вес авто (кг)", 500, 5000, 1500)
    wheelbase = st.number_input("Колесная база", 80.0, 130.0, 95.0)

with col2:
    carwidth = st.number_input("Ширина кузова", 60.0, 80.0, 65.0)
    carlength = st.number_input("Длина кузова", 140.0, 210.0, 170.0)
    boreratio = st.number_input("Диаметр цилиндра", 2.0, 5.0, 3.3)
    symboling = st.selectbox("Рейтинг риска (от -3 до 3)",
                             [-3, -2, -1, 0, 1, 2, 3], index=3)

if st.button("Рассчитать стоимость", type="primary"):
    input_data = pd.DataFrame([[
        symboling, wheelbase, carlength, carwidth,
        curbweight, enginesize, boreratio, horsepower
    ]], columns=['symboling', 'wheelbase', 'carlength', 'carwidth', 'curbweight', 'enginesize', 'boreratio', 'horsepower'])

    prediction = model.predict(input_data)

    st.success(f"### Примерная стоимость: ${prediction[0]:,.2f}")
    st.info("Расчет произведен на основе алгоритма Random Forest.")
