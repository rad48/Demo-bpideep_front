import chart_studio.plotly as py
import plotly.figure_factory as ff
import pandas as pd



## LABORATORY AND TIME MEAN VALUES FROM PREDICT MODELS
MEAN_NON_DT_LAB = 0.52
MEAN_DT_LAB = 0.62
MEAN_NON_DT_TIME = 0.52
MEAN_DT_TIME = 0.62






def colorized_time(y_lab, y_time):
    if x < MEAN_NON_DT: return 'red'
    elif x < MEAN_DT: return 'orange'
    else: return 'green'

# Get json ready
def get_fig(x)
    json_input = [
          {"title":"Link to labo","subtitle": "Lorem ipsum", "ranges":[MEAN_NON_DT_LAB, MEAN_DT_LAB],"measures":[MEAN_NON_DT_LAB,MEAN_DT_LAB],"markers":[y_lab]},
          {"title":"Time to market","subtitle": "Lorem ipsum","ranges":[MEAN_NON_DT_TIME, MEAN_DT_TIME],"measures":[MEAN_NON_DT_TIME, MEAN_DT_TIME],"markers":[y_time]}
        ]
    data = pd.DataFrame(json_input)
    return    ff.create_bullet(
        data, markers='markers', measures='measures',
        ranges='ranges', subtitles='subtitle', titles='title',
    )
