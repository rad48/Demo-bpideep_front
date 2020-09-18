import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import chart_studio
import streamlit as st
# chart_studio.tools.set_credentials_file(username='NicolasNicolasNicolas', api_key='lr1c37zw81')



## LABORATORY AND TIME MEAN VALUES FROM PREDICT MODELS
MEAN_NON_DT_LAB = 52
MEAN_DT_LAB = 62
THRESHOLD_LAB = (MEAN_NON_DT_LAB + MEAN_DT_LAB)/2

MEAN_NON_DT_TIME = 39.9
MEAN_DT_TIME = 46.2
THRESHOLD_TIME = (MEAN_NON_DT_TIME + MEAN_DT_TIME)/2

MEAN_NON_DT_TECHNO = 54
MEAN_DT_TECHNO = 35
THRESHOLD_TECHNO = (MEAN_NON_DT_TECHNO + MEAN_DT_TECHNO)/2

def colorized_lab(x):
    if x < MEAN_NON_DT_LAB: return 'rgba(220,20,60,1)'
    elif x < MEAN_DT_LAB: return 'rgba(255,127,80,1)'
    else: return 'rgba(154,205,50,1)'

def colorized_time(x):
    if x < MEAN_NON_DT_TIME: return 'rgba(220,20,60,1)'
    elif x < MEAN_DT_TIME: return 'rgba(255,127,80,1)'
    else: return 'rgba(154,205,50,1)'




# def colorized_time(y_lab, y_time):
#     if y_lab < MEAN_NON_DT: return 'rgba(220,20,60,1)'
#     elif x < MEAN_DT: return 'rgba(255,127,80,1)'
#     else: return 'rgba(154,205,50,1)'

# measure_colors=['rgba(220,20,60,0.1)', 'rgb(154,205,50)']
# range_colors=['rgb(241, 241, 241)', 'rgb(241, 241, 241)']


# # Get json ready
# def get_fig(y_lab, y_time):
#     json_input = [
#           {"title":"Lab intensity","subtitle": "Lorem ipsum", "ranges":[0, 100],"measures":[MEAN_NON_DT_LAB,MEAN_DT_LAB, 100],"markers":[y_lab]},
#           {"title":"Time to market","subtitle": "Lorem ipsum","ranges":[0, 100],"measures":[MEAN_NON_DT_TIME, MEAN_DT_TIME, 100],"markers":[y_time]}
#         ]
#     data = pd.DataFrame(json_input)
#     return ff.create_bullet(
#                 data,
#                 markers='markers',
#                 measures='measures',
#                 ranges='ranges',
#                 subtitles='subtitle',
#                 titles='title',
#                 range_colors=range_colors,
#                 measure_colors=measure_colors
#                 )

# SECOND ATTEMPT

import plotly.graph_objects as go
@st.cache
def get_fig(y_lab, y_time):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = 40,
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.08, 0.25]},
        title = {'text': "Techno"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 0.5,
            #     'value': THRESHOLD_TECHNO},
            'steps': [
                {'range': [0, MEAN_NON_DT_TECHNO], 'color': 'rgba(220,20,60,0.2)'},
                {'range': [MEAN_NON_DT_TECHNO, MEAN_DT_TECHNO], 'color': 'rgba(255,127,80,0.2)'}],
            'bar': {'color': 'grey'}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = round(y_time),
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.4, 0.6]},
        title = {'text': "Time"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 0.5,
            #     'value': THRESHOLD_TIME},
            'steps': [
                {'range': [0, MEAN_NON_DT_TIME], 'color': 'rgba(220,20,60,0.2)'},
                {'range': [MEAN_NON_DT_TIME, MEAN_DT_TIME], 'color': 'rgba(255,127,80,0.2)'}],
            'bar': {'color': colorized_time(y_time)}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = round(y_lab),
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.7, 0.9]},
        title = {'text' :"Laboratory"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            # 'threshold': {
            #     'line': {'color': "black", 'width': 2},
            #     'thickness': 0.5,
            #     'value': THRESHOLD_LAB},
            'steps': [
                {'range': [0, MEAN_NON_DT_LAB], 'color': 'rgba(220,20,60,0.2)'},
                {'range': [MEAN_NON_DT_LAB, MEAN_DT_LAB], 'color': 'rgba(255,127,80,0.2)'}],
            'bar': {'color': colorized_lab(y_lab)}}))
    fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

    return fig
