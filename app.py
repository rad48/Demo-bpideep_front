
import json
import requests
import streamlit as st
import pandas as pd

# to launch front server:
# streamlit run app.py

# if st.button('Search company'):
add_selectbox = st.sidebar.selectbox(
    'Choose',
    ('Predict', 'Search')
)

if add_selectbox == 'Predict':
    company = st.text_input('Company name')

    if company:
        # url = 'https://deeptechpredict.herokuapp.com/predict'
        url = 'http://127.0.0.1:8080/predict'

        params = {
            'name' : company
        }

        response = requests.get(url, params)

        resp = response.content

        a = json.loads(resp)

        st.write(f"Deeptech prediction : {a['prediction']}")
        st.write(f"Predict probability : {a['prediction_proba']}")
        st.write(a['time_predict'])
        st.write(a['lab_predict'])
        st.image(a['image'], width = 100)


elif add_selectbox == 'Search':
    year = st.text_input('Year')
    month = st.text_input('Month')

    if year and month:
        url = 'https://deeptechpredict.herokuapp.com/search'
        # url = 'http://127.0.0.1:8080/search'
        params = {
            'year' : year,
            'month': month
        }

        response = requests.get(url, params)

        resp = response.content

        a = json.loads(resp)

        df = pd.DataFrame.from_dict(a)
        st.dataframe(df)





