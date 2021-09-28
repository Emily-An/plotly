# Import required libraries

import pandas as pd
import dash
from dash import html
from dash import dcc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options = [{'label': 'All Sites', 'value': 'ALL'},
                                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}],
                                             placeholder='Select a Launch Site here',
                                             searchable=True,
                                             value='ALL'
                                            ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                



# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# Function decorator to specify function input and output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def update_graph(site_dropdown):
    if site_dropdown == 'All':
        df_a = spacex_df.groupby('class').size().reset_index(name='class count')
        chart_all = px.pie(df_a, values='class count', 
        names='class count',
        title='ALL Sites')
        return chart_all
    else:
        # return the outcomes piechart for a selected site
        df_n = spacex_df[spacex_df['Launch Site'] == site_dropdown].groupby(['Launch Site', 'class']).size().reset_index(name='class count')
        chart_sel = px.pie(df_n, values='class count', names='class count', title='Launch site')
        return chart_sel



# Run the app
if __name__ == '__main__':
    app.run_server()
