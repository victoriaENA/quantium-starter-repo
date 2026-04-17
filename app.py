from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

# 1. Load the formatted data you generated in the last task
df = pd.read_csv("formatted_sales_data.csv")

# 2. Ensure the data is sorted by date (as requested)
df = df.sort_values("date")

# Initialize the Dash app
app = Dash(__name__)

# 3. Create the line chart using Plotly Express
# We are plotting Date on the X-axis and Sales on the Y-axis
fig = px.line(df, x="date", y="sales", title="Pink Morsel Sales")

# Add appropriate axis labels
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Sales ($)")

# 4. Set up the layout of the app (The Header and the Graph)
app.layout = html.Div(children=[
    # The Header
    html.H1(
        children="Pink Morsel Sales Visualiser", 
        style={"textAlign": "center"}
    ),
    
    # The Line Chart
    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)