from dash import Dash, dcc, html, callback
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
# if there are pages in the app, import them here

# Initialize Dash app with Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])
server = app.server

# Define the navbar with the brand name and links to other pages in the app if applicable
navbar = dbc.NavbarSimple(
    children=[
    ],
    brand="Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
    className="justify-content-between",
)

# Define the app layout
app.layout = html.Div([
    navbar,
    html.Div(id='page-content', children=["This is the main content area"])
], id="main-container")


# Define callbacks and functions here

# static files (css, js, images) are automatically served from the assets directory


# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)