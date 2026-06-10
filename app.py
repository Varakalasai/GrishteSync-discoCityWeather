# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import requests
import json

st.image('https://i.ibb.co/RGmb4FKk/1781072041102.png', width=200)

st.title('Disco City Weather')

city = st.text_input('Enter City Name')

if city:
    try:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_OPENWEATHERMAP_API_KEY&units=metric')
        data = response.json()
        st.write('Current Weather in ' + city)
        col1, col2, col3 = st.columns(3)
        col1.metric('Temperature', str(data['main']['temp']) + '°C')
        col2.metric('Humidity', str(data['main']['humidity']) + '%')
        col3.metric('Weather', data['weather'][0]['description'])
    except Exception as e:
        st.error('City not found or invalid API key')

st.markdown('Made with GrishteSync | Suryasticsai | <a href="https://suryasticsai.github.io/GrishteSync">GrishteSync</a>')