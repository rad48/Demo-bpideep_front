import json
import requests
import streamlit as st
import pandas as pd

import awesome_streamlit as ast

months_dic = { 'January': 'jan',
            'February': 'feb',
            'March': 'mar',
            'April':'apr',
            'May':'may',
            'June':'jun',
            'July':'jul',
            'August':'aug',
            'September':'sep',
            'October':'oct',
            'November':'nov',
            'December':'dec'}

def write():
    st.sidebar.title("Input Date :")

    month = st.sidebar.selectbox(
        "Select month",
        options=list(months_dic.keys()),

    )
    year = st.sidebar.text_input('Enter Year')
    # month = st.sidebar.text_input('Month','May').capitalize()

    if year and month in months_dic.keys():
        url = 'https://deeptechpredict.herokuapp.com/search'
        st.title(f"Top foundings of {month} {year}")
        st.markdown("""This app exctract french start-ups with the 10 highest founding rounds of a specified month and year.
                     It then predicts their probability of being classified as a Deeptech.""")

        a = get_data(year, months_dic[month])

        # Styling the dataframe
        dict_df = {'Company' : a['name'], 'Last funding (million €)': a['amount'], 'Deeptech': a['prediction']}

        def highlight_1(s):
            if s.Deeptech == str(1):
                return ['color: white;background-color: green;font-weight: bold']*3
            else:
                return ['background-color: white']*3

        df = pd.DataFrame.from_dict(dict_df)
        df['index'] = range(1,11)
        df = df.set_index('index')
        df = df.style.apply(highlight_1, axis = 1 )


        st.table(df)

@st.cache
def get_data(year, month):
        url = 'http://127.0.0.1:8080/search'
        # url = 'https://deeptechpredict.herokuapp.com/search'

        params = {
            'year' : year,
            'month': month
        }

        response = requests.get(url, params)
        resp = response.content
        a = json.loads(resp)
        return a


if __name__ == "__main__":
    write()
