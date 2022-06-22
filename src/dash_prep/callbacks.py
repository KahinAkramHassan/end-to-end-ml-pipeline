from dash import Input, Output, callback
from . import layouts as layout

#<<<<<<<<<<<<<<<<<<<<<Routing<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")],
)
def page_routing(pathname):
    
    if pathname == '/':
        return layout.home_page
    
    return layout.page_not_found

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
