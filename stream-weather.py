import pickle
import streamlit as st

# load save model 
model = pickle.load(open('weather_model.sav', 'rb'))

# Judul Untuk Web
st.title('Data Mining Prediksi Weather')
 

# Form Input
precipitation = st.text_input('Masukan Nilai precipitation')

temp_max = st.text_input('Masukan Nilai temp max') 

temp_min = st.text_input('Masukan  Nilai temp min')

wind = st.text_input('Masukan Nilai wind')


# kode Prediksi
weather_diagnosis = ' '

#Button Prediksi
if st.button('Prediksi Weather'):
    weather_prediction = model.predict([[precipitation, temp_max, temp_min, wind,]])

    if(weather_prediction==['sun']):
       weather_diagnosis = 'Cuacanya Cerah'

    elif(weather_prediction==['drizzle']):
       weather_diagnosis = 'Cuacanya Gerims'

    elif(weather_prediction==['rain']):
       weather_diagnosis = 'Cuacanya Hujan'

    elif(weather_prediction==['snow']):
       weather_diagnosis = 'Cuacanya Bersalju'

    else:
         weather_diagnosis = 'Cuacanya Berkabut'

st.success(weather_diagnosis)