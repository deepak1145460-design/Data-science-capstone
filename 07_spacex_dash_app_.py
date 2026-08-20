"""
Interactive Visual Analytics – Plotly Dash App
GitHub URL: << PASTE YOUR GITHUB REPO URL HERE >>

Run with:
    pip install dash pandas plotly --break-system-packages
    python 07_spacex_dash_app.py
Then open http://127.0.0.1:8050 in a browser.

Features:
  - Dropdown to select launch site (or "All Sites")
  - Pie chart: success-count share by site (or success vs failure for one site)
  - Range slider: filter by payload mass
  - Scatter chart: payload mass vs success (colored by booster version), for the
    selected site/payload range
"""

import os
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the wrangled dataset produced by the Data Wrangling notebook.
# NOTE (fixed): no manual upload required. Just like the other notebooks in
# this project, this first looks for 'dataset_part_2_clean.csv' locally, and
# if it isn't there, self-fetches IBM's static copy of the same cleaned
# dataset -- so the app can be run standalone without any extra setup.
CSV_PATH = 'dataset_part_2_clean.csv'
FALLBACK_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv"
)

if os.path.exists(CSV_PATH):
    spacex_df = pd.read_csv(CSV_PATH)
    print(f"Loaded local '{CSV_PATH}'. Rows: {len(spacex_df)}")
else:
    print(f"'{CSV_PATH}' not found locally -- fetching IBM's static copy instead...")
    spacex_df = pd.read_csv(FALLBACK_URL)
    spacex_df.to_csv(CSV_PATH, index=False)  # cache locally for reuse
    print(f"Fetched and cached dataset. Rows: {len(spacex_df)}")

max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 36}),

    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] +
                [{'label': site, 'value': site} for site in spacex_df['LaunchSite'].unique()],
        value='ALL',
        placeholder="Select a Launch Site here",
        searchable=True
    ),
    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0, max=10000, step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(
            spacex_df, values='Class', names='LaunchSite',
            title='Total Successful Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        outcome_counts = filtered_df['Class'].value_counts().reset_index()
        outcome_counts.columns = ['Class', 'count']
        outcome_counts['Class'] = outcome_counts['Class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            outcome_counts, values='count', names='Class',
            title=f'Success vs. Failure for site {selected_site}'
        )
    return fig


@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['PayloadMass'] >= low) & (spacex_df['PayloadMass'] <= high)
    filtered_df = spacex_df[mask]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['LaunchSite'] == selected_site]

    fig = px.scatter(
        filtered_df, x='PayloadMass', y='Class',
        color='BoosterVersion',
        title='Correlation between Payload and Success for selected site(s)'
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
