import json
import requests
import streamlit as st
import pandas as pd

import awesome_streamlit as ast

def create_info_table(selected_data_info):
    info_table = pd.DataFrame()

    data_description = selected_data_info["description"]
    if data_description:
        line = pd.Series(data_description)
        line.name = "Description"
        info_table = info_table.append(line)

    tags = selected_data_info["tags"]
    if tags:
        tags = ", ".join(tags)
        line = pd.Series(tags)
        line.name = "Keywords"
        info_table = info_table.append(line)

    if len(info_table) > 0:
        info_table.columns = [""]
        st.table(info_table)


def write():
    st.sidebar.title("Input company's name :")
    company = st.sidebar.text_input('Company','Devialet')

    if company:
        # url = 'https://deeptechpredict.herokuapp.com/predict'


        a = get_data(company)

        #print company name and logo
        st.title(company.capitalize())
        st.image(a['image'], width = 100)

        #print a table with description and tags
        selected_data_info = {'description': a['description'],
                                'tags' : a['tags']}

        create_info_table(selected_data_info)


        st.write(f"Deeptech prediction : {a['prediction']}")
        st.write(f"Predict probability : {a['prediction_proba']}")
        st.write(a['time_predict'])
        st.write(a['lab_predict'])



@st.cache
def get_data(company):
        url = 'http://127.0.0.1:8080/predict'
        # url = 'https://deeptechpredict.herokuapp.com/search'

        params = {
            'name' : company
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)

        return a
