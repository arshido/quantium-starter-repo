from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. LOAD DATA
df = pd.read_csv('./formatted_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 2. INITIALIZE APP
app = Dash(__name__)

# 3. DEFINE LAYOUT
app.layout = html.Div(className="wrapper", children=[

    # CARD 1: HEADER
    html.Div(className="header_card", children=[
        html.H1("Soul Foods: Sales Analytics", id="header"),
        html.P("Analyze the impact of the Pink Morsel price increase (Jan 2021)")
    ]),

    # CARD 2: CONTROLS
    html.Div(className="control_card", children=[
        html.H3("Filter by Region:"),
        dcc.RadioItems(
            id='region_selector',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All Regions', 'value': 'all'}
            ],
            value='all',
            inline=True
        )
    ]),

    # CARD 3: GRAPH
    html.Div(className="graph_card", children=[
        dcc.Graph(id="visualization")
    ])
])


# 4. CALLBACK
@app.callback(
    Output('visualization', 'figure'),
    Input('region_selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        # Minimalist title since the header handles the main context
        title=f"Daily Sales Trend: {selected_region.capitalize()}",
        labels={"date": "Date", "sales": "Revenue ($)"}
    )

    # UPDATING THE CHART LOOK TO MATCH THE THEME
    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_family="Poppins, sans-serif",
        font_color="#2c3e50",
        title_font_size=20,
        xaxis=dict(showgrid=False),  # Cleaner look without vertical gridlines
        yaxis=dict(showgrid=True, gridcolor="#f0f0f0"),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # Make the line color match our "Pink Morsel" theme
    fig.update_traces(line_color='#e91e63', line_width=2)

    return fig


# 5. RUN APP
if __name__ == '__main__':
    app.run(debug=True)