
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
    year = st.text_input('Year','2020')
    month = st.text_input('Month','may')

    if year and month:
        # url = 'https://deeptechpredict.herokuapp.com/search'
        url = 'http://127.0.0.1:8080/search'
        params = {
            'year' : year,
            'month': month
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)


        # Styling the dataframe
        dict_df = {'Company' : a['name'], 'Last funding (million €)': a['amount'], 'Deeptech': a['prediction']}

        def highlight_1(s):
            if s.Deeptech == str(1):
                return ['color: white;background-color: green;font-weight: bold']*3
            else:
                return ['background-color: white']*3

        df = pd.DataFrame.from_dict(dict_df).style.apply(highlight_1, axis = 1 )
        df = df.hide_index()

        st.dataframe(df)





