from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

#<<<<<<<<<<<<<<<<<<<<<<Navbar menu<<<<<<<<<<<<<<<<<<<<<<<<<<<<
navbar = html.Div([
    "HELLO Navie"
])

#<<<<<<<<<<<<<<<<<<<<<<home page<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
home_page = html.Div([
    "HELLO HOMIE"
])

#<<<<<<<<<<<<<<<<<<<<<<404 page not found<<<<<<<<<<<<<<<<<<<<<
page_not_found = html.Div(children=[
    dbc.Row(children=[
        dbc.Col(children=[
            # If the user tries to reach a different page, return a 404 message
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname was not recognised..."),
        ])
    ])
])