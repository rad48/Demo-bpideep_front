
import json
import requests
import streamlit as st
import pandas as pd

# to launch front server:
# streamlit run app.py
#imports for dataviz
import os
import glob
import time
import multiprocessing
import numpy as np
import pandas as pd
from gauge import *

# if st.button('Search company'):
add_selectbox = st.sidebar.selectbox(
    'Choose',
    ('Predict', 'Search')
)

if add_selectbox == 'Predict':
    company = st.text_input('Enter the name of a company')

    if company:
        url = 'https://deeptechpredict.herokuapp.com/predict'
        # url = 'http://127.0.0.1:8080/predict'

        params = {
            'name' : company
        }

        response = requests.get(url, params)

        resp = response.content

        a = json.loads(resp)

        if a['prediction']== 1:
            deeptech_variable = 'deeptech'
        else:
            deeptech_variable = 'not deeptech'
        st.write(f"The company is {deeptech_variable}")
        st.write(f"The deeptech probability is {round(float(a['prediction_proba'])*100)}% (above 50% you can consider the company deeptech)")
        st.image(a['image'], width = 100)
        y_lab = float(a['lab_predict'])
        y_time = float(a['time_predict'])
        st.plotly_chart(get_fig(y_lab, y_time), filename='Deeptech decrypted')


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
