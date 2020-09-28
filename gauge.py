import pandas as pd
import streamlit as st
import plotly.express as px


## LABORATORY AND TIME MEAN VALUES FROM PREDICT MODELS
MEAN_NON_DT_LAB = 52
MEAN_DT_LAB = 62
THRESHOLD_LAB = (MEAN_NON_DT_LAB + MEAN_DT_LAB)/2

MEAN_NON_DT_TIME = 39.9
MEAN_DT_TIME = 46.2
THRESHOLD_TIME = (MEAN_NON_DT_TIME + MEAN_DT_TIME)/2

MEAN_NON_DT_TECHNO = 35
MEAN_DT_TECHNO = 54
THRESHOLD_TECHNO = (MEAN_NON_DT_TECHNO + MEAN_DT_TECHNO)/2

def colorized_lab(x):
    if x < MEAN_NON_DT_LAB: return 'rgba(220,20,60,1)'
    elif x < MEAN_DT_LAB: return 'rgba(255,127,80,1)'
    else: return 'rgba(154,205,50,1)'

def colorized_time(x):
    if x < MEAN_NON_DT_TIME: return 'rgba(220,20,60,1)'
    elif x < MEAN_DT_TIME: return 'rgba(255,127,80,1)'
    else: return 'rgba(154,205,50,1)'


import plotly.graph_objects as go
def get_fig(y_lab, y_time):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = 40,
        delta = {'reference': THRESHOLD_TECHNO},
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
                {'range': [0, MEAN_NON_DT_TECHNO], 'color': 'rgba(220,20,60,0.3)'},
                {'range': [MEAN_NON_DT_TECHNO, MEAN_DT_TECHNO], 'color': 'rgba(255,127,80,0.3)'}],
            'bar': {'color': 'grey'}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = round(y_time),
        delta = {'reference': THRESHOLD_TIME},
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
                {'range': [0, MEAN_NON_DT_TIME], 'color': 'rgba(220,20,60,0.3)'},
                {'range': [MEAN_NON_DT_TIME, MEAN_DT_TIME], 'color': 'rgba(255,127,80,0.3)'}],
            'bar': {'color': colorized_time(y_time)}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = round(y_lab),
        delta = {'reference': THRESHOLD_LAB},
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
                {'range': [0, MEAN_NON_DT_LAB], 'color': 'rgba(220,20,60,0.3)'},
                {'range': [MEAN_NON_DT_LAB, MEAN_DT_LAB], 'color': 'rgba(255,127,80,0.3)'}],
            'bar': {'color': colorized_lab(y_lab)}}))
    #fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})
    fig.update_layout(
        height = 400,
        margin = {'t':0, 'b':0, 'l':0},
        font_family="Courier New",
        font_color="black",
        title_font_family="Times New Roman",
        title_font_color="black",
        legend_title_font_color="black"
    )

    return fig
