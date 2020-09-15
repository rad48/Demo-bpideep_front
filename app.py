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

st.write(resp, unsafe_allow_html=True)
