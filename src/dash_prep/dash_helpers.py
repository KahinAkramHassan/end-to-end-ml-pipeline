#Dash's little helpers 
from dash import html, dcc
import plotly.express as px

from . import dash_constants as constants


# draw the mapbox map 
def draw_map(data):
    
    px.set_mapbox_access_token(constants.MAPBOX_TOKEN)
    
    fig = px.scatter_mapbox(
        data, 
        lat="latitude", 
        lon="longitude",
        color="median_house_value", 
        size=data["population"]/100, #district's population scaled. 
        color_continuous_scale=px.colors.cyclical.IceFire, 
        size_max=15,
        zoom=5,
        opacity=0.5,
        width=800,
        height=1000,
        center=dict(
            lat=37.5,
            lon=-120.0
        ),
    )
    return html.Div([dcc.Graph(figure=fig)]) 


