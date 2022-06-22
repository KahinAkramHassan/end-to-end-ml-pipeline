import yaml

with open("config/mapbox_token.yml","r") as token:
    MAPBOX_TOKEN = yaml.load(token,Loader=yaml.FullLoader)
    