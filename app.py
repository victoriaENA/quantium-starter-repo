from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# 1. Load and sort the data
df = pd.read_csv("formatted_sales_data.csv")
df = df.sort_values("date")

# Initialize the Dash app
app = Dash(__name__)

# --- CSS Styling Dictionary ---
# Centralizing our colors to make it easy to change the theme later!
COLORS = {
    "primary": "#E0646E",      # A nice "Pink Morsel" color
    "background": "#F4F6F9",   # A soft, modern gray/blue background
    "text": "#2C3E50",         # Dark slate for readable text
    "card_bg": "#FFFFFF"       # White for the graph background
}

# 2. App Layout
app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "fontFamily": "Segoe UI, Tahoma, Geneva, Verdana, sans-serif",
        "padding": "40px",
        "minHeight": "100vh"
    },
    children=[
        # The Header
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": COLORS["text"],
                "marginBottom": "10px",
                "fontWeight": "bold"
            }
        ),
        
        # A sub-header to make it look professional
        html.P(
            "Analyzing sales trends before and after the January 15th price increase.",
            style={
                "textAlign": "center",
                "color": "#7F8C8D",
                "marginBottom": "40px",
                "fontSize": "16px"
            }
        ),
        
        # The Radio Button Filter
        html.Div(
            style={
                "backgroundColor": COLORS["card_bg"],
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 8px 0 rgba(0,0,0,0.05)",
                "maxWidth": "800px",
                "margin": "0 auto 30px auto", # Centers the box
                "textAlign": "center"
            },
            children=[
                html.Label(
                    "Filter by Region:", 
                    style={"fontWeight": "bold", "marginRight": "20px", "color": COLORS["text"]}
                ),
                dcc.RadioItems(
                    id='region-filter',
                    options=[
                        {'label': ' North ', 'value': 'north'},
                        {'label': ' East ', 'value': 'east'},
                        {'label': ' South ', 'value': 'south'},
                        {'label': ' West ', 'value': 'west'},
                        {'label': ' All Regions ', 'value': 'all'}
                    ],
                    value='all', # The default selection
                    inline=True, # Places them horizontally
                    style={
                        "display": "inline-flex",
                        "gap": "20px",
                        "color": COLORS["text"],
                        "fontSize": "16px",
                        "cursor": "pointer"
                    }
                )
            ]
        ),
        
        # The Graph Container
        html.Div(
            style={
                "backgroundColor": COLORS["card_bg"],
                "padding": "20px",
                "borderRadius": "10px",
                "boxShadow": "0 4px 8px 0 rgba(0,0,0,0.05)",
                "maxWidth": "1200px",
                "margin": "0 auto"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# 3. The Callback (Making it Interactive)
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    # Filter the dataframe based on the radio button choice
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]
        
    # Create the new figure based on the filtered data
    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Sales Data: {selected_region.title()} Region"
    )
    
    # Style the Plotly figure to match our custom CSS
    fig.update_layout(
        plot_bgcolor=COLORS["card_bg"],
        paper_bgcolor=COLORS["card_bg"],
        font_color=COLORS["text"],
        title_x=0.5, # Centers the graph title
        margin={"l": 40, "r": 40, "t": 60, "b": 40}
    )
    
    # Make the actual line our "Pink Morsel" color
    fig.update_traces(line_color=COLORS["primary"])
    
    fig.update_xaxes(title_text="Date", showgrid=False)
    fig.update_yaxes(title_text="Sales ($)", gridcolor="#E5E8E8")
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)