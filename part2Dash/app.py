# Import required libraries and modules that the app will use.

import dash
from dash import dcc, html
from dash import dash_table
import pandas as pd
import requests
import plotly.express as px

# Fetch data from the API and convert it to a DataFrame
url = "https://data.winnipeg.ca/resource/6rcy-9uik.json"
response = requests.get(url)
data = response.json()

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Aggregate the data to count the number of addresses per collection day and convert it to a DataFrame
df_count = df.groupby('collection_day').size().reset_index(name='count')

# Initialize the Dash app
app = dash.Dash(__name__)

# Layout of the app including the data table and graph
app.layout = html.Div([
    html.H1("Winnipeg Recycling, Garbage, and Yard Waste Collection Days"), # Title
    
    html.H2("Data Table"), # Subtitle
    dash_table.DataTable( # Data table
        id='data-table', # ID
        columns=[{"name": i, "id": i} for i in df.columns], # Column names
        data=df.to_dict('records'), # Data
        page_size=10, # This displays how many rows will be on the page at the top, so it'll be 10 rows.
    ),

    # This is the graph that will display the count of addresses per collection day.
    html.H2("Collection Days Graph"),
    dcc.Graph(
        id='data-graph',
        figure=px.bar(df_count, x='collection_day', y='count', title='Count of Addresses per Collection Day', text='count')
    )
])

# Run the app, and view it on http://127.0.0.1:8050/
if __name__ == '__main__':
    app.run_server(debug=True)
