import plotly.graph_objects as go
## TIME GAUGE
MEAN_NON_DT = 0.52
MEAN_DT = 0.62

def colorized_time(x):
    if x < MEAN_NON_DT: return 'red'
    elif x < MEAN_DT: return 'orange'
    else: return 'green'

def fig_time(x):
    return go.Figure(go.Indicator(
                domain = {'x': [0, 1], 'y': [0, 1]},
                value = x,
                mode = "gauge+number+delta",
                title = {'text': "Time to market"},
                delta = {'reference': MEAN_DT},
                gauge = {'axis': {'range': [None, 1]},
                         'bar': {'color': colorized_time(x)},
                         'steps' : [
                             {'range': [0, MEAN_NON_DT], 'color': "lightgray"},
                             {'range': [MEAN_NON_DT, MEAN_DT], 'color': "gray"}],
                         }))
