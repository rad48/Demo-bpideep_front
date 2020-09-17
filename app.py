
import json
import requests
import streamlit as st

# to launch front server:
# streamlit run app.py

<<<<<<< HEAD
import streamlit as st


company = st.text_input('Company name', 'Google')

import requests

#imports for dataviz
import os
import glob
import time
import multiprocessing
import numpy as np
import pandas as pd
import plotly.graph_objects as go
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

predict_time = 0.75

st.plotly_chart(fig_time(predict_time))
