from dash import html
import dash_bootstrap_components as dbc
import sys
from . import dash_helpers

sys.path.append("../")
from data_prep import data_helpers as data

# Fetch and load the data
data.load_housing_data()
housing = data.read_csv_file()
# Stratified sampling based on the income category
strat_train_set, strat_test_set = data.stratisfied_split_train_test(housing,0.2,"income_cat")

#<<<<<<<<<<<<<<<<<<<<<<Navbar menu<<<<<<<<<<<<<<<<<<<<<<<<<<<<
navbar = html.Div([
    "HELLO Navie"
])


home_page = html.Div([
    dbc.Container([

        dbc.Row([
            #
            dbc.Col(
                children=[
                    dash_helpers.draw_map(strat_train_set)
                ],
                #style={'height': '54vh', 'overflowY': 'auto'},
                md=12
            ),
        ],
        justify="center",
        className='shadow p-3 mb-3 mt-1 bg-white rounded-0'
        
        ), #End of row1
       
       
    ],fluid=True) #return dbc main Container
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