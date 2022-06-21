#Main Dash app 
#Created 06/21/22 2:30pm
#Author: Kahin Akram Hassan

#====================================Dependencies==================================================

from distutils.log import debug
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 

# Initiate the dash figure 
app = Dash(__name__)

# Example df -- Will fix this file much better soon. 
df = pd.DataFrame({
    "Fruit":["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount":[4, 1, 2, 2, 4, 5],
    "City":["SF", "SF", "SF", "Montreal", "NY", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children=['Hello Dashy']),
    html.Div(children=[
        """ A Dash web application example """
    ]),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
]) 

if __name__ == '__main__':
    app.run_server(debug=True)