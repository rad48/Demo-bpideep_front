import json
import requests
import streamlit as st
import pandas as pd
# import awesome_streamlit as ast
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
    company = st.sidebar.text_input('Company')

    if company == 'Le wagon':
        st.title('Le wagon')
        st.image('https://s3-eu-west-1.amazonaws.com/dealroom-images/89/MTAwOjEwMDpjb21wYW55QHMzLWV1LXdlc3QtMS5hbWF6b25hd3MuY29tL2RlYWxyb29tLWltYWdlcy8yMDIwLzAzLzAzLzQ2NDgwOTNhNmYxN2Y3OWU3YzRlZDg0ZWVjOWI1YmY4.png', width = 50)
        st.image('https://i.imgflip.com/4fexmq.jpg', width = 900)

    elif company:
        a = get_data(company)

        #print company name and logo
        # st.title(company.capitalize())
        st.title(company.capitalize())
        st.image(a['image'], width = 100)
        if int(a['prediction'])== 1:
            deeptech_variable = 'deeptech'
        else:
            deeptech_variable = 'not deeptech'

        st.write(f"The company is **{deeptech_variable}** with a probability of {round(float(a['prediction_proba'])*100)}% *(above 50%, it is deeptech)*.")
        y_lab = float(a['lab_predict'])*100
        y_time = float(a['time_predict'])*100

        st.write(f"This probability is explained by 3 deeptech criteria ranked from 0 to 100:")
        st.plotly_chart(get_fig(y_lab, y_time))


        selected_data_info = {'description': a['description'],
                                'tags' : a['tags']}

        st.title(f'Company details.')
        create_info_table(selected_data_info)


@st.cache
def get_data(company):
        # url = 'http://127.0.0.1:8080/predict'
        url = 'https://deeptechpredict.herokuapp.com/predict'

        params = {
            'name' : company
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)

        return a
