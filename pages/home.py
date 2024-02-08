# home.py
import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1('Home Page'), width=12)),
    dbc.Row(dbc.Col([
        # Your content here, using dbc components for styling
    ])),
], fluid=True)

