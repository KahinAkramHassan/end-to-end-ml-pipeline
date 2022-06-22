#Main Dash app 
#Created 06/21/22 2:30pm
#Author: Kahin Akram Hassan

#====================================Dependencies==================================================

from distutils.log import debug
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

from dash_prep import layouts as page_layout, callbacks

# Initialize the dash app 
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{
        'name':'viewport',
        'content':'width=device-width, initial-scale=1'
    }]
)

#Load the navbar 
navbar = page_layout.navbar
#Dynamic part of the app
content = html.Div(id="page-content")

#Set the app layout 
app.layout = dbc.Container(children=[
    dcc.Location(id="url",refresh=False),
    navbar,
    content
], fluid=False)

if __name__=='__main__':
    app.run_server(port=8051, debug=True)    