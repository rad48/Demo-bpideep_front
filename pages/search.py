import json
import requests
import streamlit as st
import pandas as pd
from gauge import *

COMPANY_LIST = [
            'AFYREN',
            # 'Carrefour',
            'Ynsect',
            'Devialet',
            'BlaBlaCar',
            'Renault',
            'Sanofi',
            'Biophytis',
            'Cellectis'
            ]

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
    company = st.selectbox(
                'Select a company',
                COMPANY_LIST)

    a = get_data(company)

    #print company name and logo
    st.title(company.capitalize())
    st.image(a['image'], width = 100)
    if int(a['prediction'])== 1:
        deeptech_variable = 'deeptech'
        st.write(f"The company is **{deeptech_variable}** with a probability of \
            {round(float(a['prediction_proba'])*100)}%.")
    else:
        deeptech_variable = 'not deeptech'
        st.write(f"The company is **{deeptech_variable}** with a probability of \
            {100-round(float(a['prediction_proba'])*100)}%.")

    y_lab = float(a['lab_predict'])*100
    y_time = float(a['time_predict'])*100

    st.write(f"This probability is explained by 3 deeptech criteria ranked from 0 to 100:")
    st.plotly_chart(get_fig(y_lab, y_time))


    selected_data_info = {'description': a['description'],
                            'tags' : a['tags']}

    st.title(f'Company details')
    create_info_table(selected_data_info)


@st.cache
def get_data(company):
        url = 'https://bpideeptechapi.herokuapp.com/predict'

        params = {
            'name' : company
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)

        return a
