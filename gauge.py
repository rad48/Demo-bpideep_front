import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd
import chart_studio
# chart_studio.tools.set_credentials_file(username='NicolasNicolasNicolas', api_key='lr1c37zw81')



# ## LABORATORY AND TIME MEAN VALUES FROM PREDICT MODELS
# MEAN_NON_DT_LAB = 52
# MEAN_DT_LAB = 62
# MEAN_NON_DT_TIME = 46.2
# MEAN_DT_TIME = 39.9






# # def colorized_time(y_lab, y_time):
# #     if y_lab < MEAN_NON_DT: return 'red'
# #     elif x < MEAN_DT: return 'orange'
# #     else: return 'green'

# measure_colors=['rgba(220,20,60,0.1)', 'rgb(154,205,50)']
# range_colors=['rgb(241, 241, 241)', 'rgb(241, 241, 241)']


# # Get json ready
# def get_fig(y_lab, y_time):
#     json_input = [
#           {"title":"Lab intensity","subtitle": "Lorem ipsum", "ranges":[0, 100],"measures":[MEAN_NON_DT_LAB,MEAN_DT_LAB, 100],"markers":[y_lab*100]},
#           {"title":"Time to market","subtitle": "Lorem ipsum","ranges":[0, 100],"measures":[MEAN_NON_DT_TIME, MEAN_DT_TIME, 100],"markers":[y_time*100]}
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

## SECOND ATTEMPT

import plotly.graph_objects as go

def get_fig(y_lab, y_time):
    fig = go.Figure()

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = 180,
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.08, 0.25]},
        title = {'text': "Revenue"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 300]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 170},
            'steps': [
                {'range': [0, 150], 'color': "gray"},
                {'range': [150, 250], 'color': "lightgray"}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = 35,
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.4, 0.6]},
        title = {'text': "Profit"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 50},
            'steps': [
                {'range': [0, 25], 'color': "gray"},
                {'range': [25, 75], 'color': "lightgray"}],
            'bar': {'color': "black"}}))

    fig.add_trace(go.Indicator(
        mode = "number+gauge+delta", value = 220,
        delta = {'reference': 200},
        domain = {'x': [0.25, 1], 'y': [0.7, 0.9]},
        title = {'text' :"Satisfaction"},
        gauge = {
            'shape': "bullet",
            'axis': {'range': [None, 300]},
            'threshold': {
                'line': {'color': "black", 'width': 2},
                'thickness': 0.75,
                'value': 210},
            'steps': [
                {'range': [0, 150], 'color': "gray"},
                {'range': [150, 250], 'color': "lightgray"}],
            'bar': {'color': "black"}}))
    fig.update_layout(height = 400 , margin = {'t':0, 'b':0, 'l':0})

    return fig
