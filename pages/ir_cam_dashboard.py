# ir_cam_dashboard.py
import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1('IR Cam Dashboard'), width=12)),
    dbc.Row([
        dbc.Col(html.P('This dashboard provides real-time data and analysis from the infrared camera.'), width=12),
        # Add your components here
    ]),
], fluid=True)
