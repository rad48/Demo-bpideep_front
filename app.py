
import json
import requests
import streamlit as st

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

#### INITIAL CODE

# url = 'https://myapp.herokuapp.com'
# url = 'http://127.0.0.1:8080/predict'

# params = {
#     'name' : company
# }

# response = requests.get(url, params)

# resp = response.content

# a = json.loads(resp)

# a['predictions']



### NEW CODE
company = st.text_input("Enter the name of a company")

if company:
    url = 'https://deeptechpredict.herokuapp.com/predict'
    params = {
        'name' : company
    }
    response = requests.get(url, params)
    resp = response.content

    a = json.loads(resp)
    st.write(a['prediction'])
    y_lab = float(a['lab_predict'])
    y_time = float(a['time_predict'])
    st.plotly_chart(get_fig(y_lab, y_time), filename='Deeptech decrypted')
