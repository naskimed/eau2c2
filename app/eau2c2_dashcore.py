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
from Data import *

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True


app = Dash(__name__,url_base_pathname = '/eau2c2_dash/', external_stylesheets=[dbc.themes.BOOTSTRAP], prevent_initial_callbacks='initial_duplicate')

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
Input_Table = Create_Input_Table()

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
            html.Div(id='input-table', children=Input_Table),
            html.Div(id='realtime-content', children=RealtimeData),
            html.Link(rel='stylesheet', href='/assets/styles.css'),
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

    columns_to_remove = ['TURBINAGE(Mm3)', 'FUITE(Mm3)','TRANSFERT(Mm3)','TotLach(Mm3)','Apport(Mm3)','Perte(Mm3)']
    dataX = data.drop(columns=columns_to_remove)

    table = dash_table.DataTable(
        id='realtime-table',
        data =dataX.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in dataX.columns],
        style_table={'height': '500px', 'overflowY': 'auto'},
    )

    return table

# Callback for generating buttons of the stored data
@app.callback(
    Output('button-container', 'children'),
    Input('stored', 'value'),
    prevent_initial_call=True
)
def display_simulation_buttons(stored):
    # Check if the simulation_results dictionary is available
    if not True:
        raise PreventUpdate

    # Get the keys (timestamps) from the simulation_results dictionary
    keys = list({0:0,1:1,2:2,3:3}.keys())

    # Create a list of buttons based on the keys
    buttons = [html.Button(key, id={'type': 'simulation-button', 'index': key}, n_clicks=0) for key in keys]

    return buttons







if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8820", debug=debug)
