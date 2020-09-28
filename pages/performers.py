import json
import requests
import streamlit as st
import pandas as pd

months_dic = {
            'May':'MAY',
            'September':'SEP'}

def write():
    st.sidebar.title("Input Date:")

    month = st.sidebar.selectbox(
        "Select month",
        options=list(months_dic.keys()),

    )
    year = st.sidebar.selectbox(
        "Select year",
        options = [2019, 2020])


    if year and month in months_dic.keys():
        st.title(f"Top fundings of {month} {year}")
        st.markdown("""This app exctracts French start-ups with the 10 highest founding rounds of a specified month and year.
                     It then predicts their probability of being classified as a Deeptech.""")

        a = get_data(year, months_dic[month])

        # Styling the dataframe
        dict_df = {'Company' : a['name'], 'Last funding (million €)': a['amount'], 'Deeptech': a['prediction']}

        def highlight_1(s):
            if s.Deeptech == 1:
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
        url = 'https://bpideeptechapi.herokuapp.com/search'

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
