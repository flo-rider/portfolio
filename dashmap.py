import pandas as pd
import numpy as np
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv('~/PycharmProjects/flo-rider.github.io/pokemon/data/pokemon-spawns.csv')
pokemon_dummies = pd.get_dummies(df['name'], prefix='pkm')
df = pd.concat([df, pokemon_dummies], axis=1)

fig = px.density_mapbox(df[df['name']=='Pikachu'], lat='lat', lon='lng',
                        mapbox_style='open-street-map',
                        zoom=9,
                        center={'lat':37.65, 'lon':-122.3},
                        radius=10,
                       width=1400,
                       height=1000)

###abcde


app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
