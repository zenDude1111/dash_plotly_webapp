from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from datetime import date

# Import the page layouts from the pages folder
from pages import ir_cam_dashboard, nitrogen_tank_dashboard, southpole_rfi_dashboard

# Initialize Dash app directly here
app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Expose the Flask server for Gunicorn

# Define your navbar and layout as before
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("IR Cam Dashboard", href="/ir_cam_dashboard")),
        dbc.NavItem(dbc.NavLink("Nitrogen Tank Dashboard", href="/nitrogen_tank_dashboard")),
        dbc.NavItem(dbc.NavLink("Southpole RFI Dashboard", href="/southpole_rfi_dashboard")),
    ],
    brand="Dr. Barron Cosmology Lab",
    brand_href="/",
    color="secondary",
    dark=True,
)

# Assuming page layouts are defined in the same file or imported correctly
# For demonstration, define a simple layout for `home`
home_layout = html.Div([
    html.H1("Home Page"),
    html.P("Welcome to the Dash app!")
])

# Define the app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

# Define the callback for dynamic page loading
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/ir_cam_dashboard':
        return ir_cam_dashboard.layout
        pass
    elif pathname == '/nitrogen_tank_dashboard':
        return nitrogen_tank_dashboard.layout
        pass
    elif pathname == '/southpole_rfi_dashboard':
        return southpole_rfi_dashboard.layout
        pass
    else:
        return home_layout

if __name__ == '__main__':
    app.run_server(debug=True)





