
import json

# to launch front server:
# streamlit run app.py

import streamlit as st

company = st.text_input('Company name', 'Google')

import requests

# url = 'https://myapp.herokuapp.com'
url = 'http://127.0.0.1:8080/predict'

params = {
    'name' : company
}

response = requests.get(url, params)

resp = response.content

a = json.loads(resp)

a['predictions']

