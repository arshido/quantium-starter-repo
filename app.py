from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# 1. INITIALIZE THE APP
app = Dash(__name__)

# 2. LOAD AND PREP DATA
# Read the CSV you created in the last task
df = pd.read_csv('./formatted_data.csv')

# Crucial Step: Convert 'date' to datetime objects and sort them
# If we don't sort, the line chart will look like a scribble!
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by="date")

# 3. CREATE VISUALIZATION
# specific question: "Were sales higher before or after the price increase?"
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Soul Foods: Pink Morsel Sales Over Time",
    # Customizing the axis labels as requested
    labels={
        "date": "Date of Sale",
        "sales": "Total Sales ($)"
    }
)

# 4. DEFINE LAYOUT
# This is the specific structure the prompt asks for: Header + Visualiser
app.layout = html.Div(children=[

    # The Header
    html.H1(
        children="Pink Morsel Sales Analytics",
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': '24px'},
        id="header"
    ),

    # The Line Chart
    dcc.Graph(
        id="visualization",
        figure=fig
    )
])

# 5. RUN THE APP
if __name__ == '__main__':
    app.run(debug=True)