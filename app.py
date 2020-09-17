
import json
import requests
import streamlit as st

# to launch front server:
# streamlit run app.py

company = st.text_input('Company name')

if company:
    url = 'https://deeptechpredict.herokuapp.com/predict'

    params = {
        'name' : company
    }

    response = requests.get(url, params)

    resp = response.content

    a = json.loads(resp)
    st.write(a['predictions'])

