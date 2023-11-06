""" Here we will define the callbacks that will be used in the dashboard """

# Importing libraries
import os
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import pandas as pd 
import seaborn as sns
from dash import Dash, dcc, html, Input, Output, callback, State, no_update, dash_table, callback_context
import plotly.express as px
import plotly.graph_objects as go
from dash_bootstrap_components.themes import BOOTSTRAP
import dash_bootstrap_components as dbc
import copy
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from layout import *
import dash_auth
from users import USERNAME_PASSWORD_PAIRS

data = pd.read_excel('Data.xlsx')

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True


app = Dash(__name__,url_base_pathname = '/eau2c2_dash/', external_stylesheets=[BOOTSTRAP], prevent_initial_callbacks='initial_duplicate')

# app.css.append_css({
#     "external_url": "/assets/styles.css" 
# })

server = app.server

if (os.environ["DASH_AUTH_MODE"]== "True"):
    auth = dash_auth.BasicAuth(
        app,
        USERNAME_PASSWORD_PAIRS
    )
navbar = create_navbar()
RealtimeData = create_RealtimeData()
app.layout = html.Div([
    #For all the pages
    navbar,
    html.Div(id='page-content'),
    dcc.Location(id='url', refresh=False),

])



# Callback to display page content based on URL
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/realtime':
        return html.Div([
            html.Div(id='realtime-content', children=RealtimeData),
            # Realtime Data page
        ])
    elif pathname == '/predictions':
        return html.Div([
            html.H1('Predictions Page'),
            # Predictions page 
        ])
    elif pathname == '/recommendations':
        return html.Div([
            html.H1('Recommendations Page'),
            # Recommendations page 
        ])
    else:
        return html.Div([
            html.H1('Welcome to EAU2C2 Dashboard'),
            
        ])


# Callback to update the data table
@app.callback(
    dash.dependencies.Output('table-container', 'children'),
    dash.dependencies.Input('interval-component', 'n_intervals')
)
def update_table(n_intervals):

    table = dash_table.DataTable(
        data=data.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in data.columns],
        style_table={'height': '300px', 'overflowY': 'auto'},
        style_header={'backgroundColor': 'rgb(30, 30, 30)'},
        style_cell={
            'backgroundColor': 'rgb(50, 50, 50)',
            'color': 'white'
        },
    )

    return table






if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8819", debug=debug)
