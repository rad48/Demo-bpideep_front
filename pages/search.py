import json
import requests
import streamlit as st
import pandas as pd
import awesome_streamlit as ast
from gauge import *

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
    company = st.sidebar.text_input('Company','Afyren')

    if company:
        # url = 'https://deeptechpredict.herokuapp.com/predict'
        url = 'http://127.0.0.1:8080/predict'

        params = {
            'name' : company
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)

        #print company name and logo
        st.title(company.capitalize())
        st.image(a['image'], width = 150)
        #print a table with description and tags
        selected_data_info = {'description': a['description'],
                                'tags' : a['tags']}

        create_info_table(selected_data_info)

        # st.write(a)

        if int(a['prediction'])== 1:
            deeptech_variable = 'deeptech'
        else:
            deeptech_variable = 'not deeptech'

        st.write(f"The company is **{deeptech_variable}**")
        st.write(f"The deeptech probability is {round(float(a['prediction_proba'])*100)}% *(above 50% you can consider the company deeptech)*")
        y_lab = float(a['lab_predict'])*100
        y_time = float(a['time_predict'])*100
        # st.plotly_chart(get_fig(y_lab, y_time), filename='Deeptech decrypted')

        st.plotly_chart(get_fig(y_lab, y_time))




