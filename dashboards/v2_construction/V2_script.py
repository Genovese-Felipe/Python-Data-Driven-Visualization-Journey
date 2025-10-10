"""A Dash application for exploring construction costs with advanced filters.

This script creates a standalone Dash dashboard that provides an interactive
sunburst chart for exploring hierarchical construction cost data. It serves
as the second version (V2) of the dashboard, introducing more advanced
interactivity than the V1 dashboard.

The dashboard features:
- Cascading dropdown filters for 'Pillar', 'Area', and 'Service'.
- A range slider to filter the data by cost.
- A sunburst chart that dynamically updates based on the selected filters.
- Detailed tooltips in the sunburst chart showing actual cost, budgeted
  cost, and the variance between them.
"""

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.colors

# Load data from the CSV file.
df_budget = pd.read_csv('dashboards/v2_construction/data.csv')

app = Dash(__name__)
"""The main Dash application instance for the V2 dashboard."""

# Get min and max cost for the range slider
min_cost = df_budget['cost'].min()
max_cost = df_budget['cost'].max()

# Define the layout based on identified requirements (filters, graph)
app.layout = html.Div([
    # The main container for the V2 dashboard layout.
    html.H1("Residential Construction: Hierarchical Cost Explorer"),

    # Dropdown for filtering by project pillar.
    html.Label("Select Pillar:"),
    dcc.Dropdown(
        id='pillar-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['pillar'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(),

    # Dropdown for filtering by project area.
    html.Label("Select Area:"),
    dcc.Dropdown(
        id='area-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['area'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(),

    # Dropdown for filtering by project service.
    html.Label("Select Service:"),
    dcc.Dropdown(
        id='service-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['service'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(),

    # Range slider for filtering by cost.
    html.Label("Filter by Cost Range:"),
    dcc.RangeSlider(
        id='cost-range-slider',
        min=min_cost,
        max=max_cost,
        value=[min_cost, max_cost],
        marks={int(min_cost): f'${int(min_cost):,}',
               int(max_cost): f'${int(max_cost):,}'},
        step=5000
    ),

    # The main sunburst chart visualization.
    dcc.Graph(id='sunburst-chart')
])

# Implement the callback function for interactivity and dynamic updates
@app.callback(
    Output('sunburst-chart', 'figure'),
    Output('area-dropdown', 'options'),
    Output('service-dropdown', 'options'),
    Input('pillar-dropdown', 'value'),
    Input('area-dropdown', 'value'),
    Input('service-dropdown', 'value'),
    Input('cost-range-slider', 'value')
)
def update_graph(selected_pillar, selected_area, selected_service, cost_range):
    """Updates the sunburst chart and dropdowns based on user filters.

    This callback function dynamically filters the construction cost data based
    on the selected pillar, area, service, and cost range. It then
    regenerates the sunburst chart with the filtered data and updates the
    options for the 'Area' and 'Service' dropdowns to ensure they only
    show relevant choices.

    Args:
        selected_pillar (str): The value from the 'Pillar' dropdown.
        selected_area (str): The value from the 'Area' dropdown.
        selected_service (str): The value from the 'Service' dropdown.
        cost_range (list[int]): A list containing the min and max values
                                 from the cost range slider.

    Returns:
        tuple: A tuple containing:
            - go.Figure: The updated sunburst chart.
            - list: The new options for the 'Area' dropdown.
            - list: The new options for the 'Service' dropdown.
    """
    filtered_df = df_budget.copy()

    # Determine options for Area dropdown based on selected Pillar
    if selected_pillar != 'All':
        area_options_df = df_budget[df_budget['pillar'] == selected_pillar]
    else:
        area_options_df = df_budget
    area_options = [{'label': i, 'value': i} for i in area_options_df['area'].unique()] + [{'label': 'All', 'value': 'All'}]

    # Determine options for Service dropdown based on selected Pillar and Area
    if selected_pillar != 'All':
        service_options_df = df_budget[df_budget['pillar'] == selected_pillar]
    else:
        service_options_df = df_budget

    if selected_area != 'All':
        service_options_df = service_options_df[service_options_df['area'] == selected_area]

    service_options = [{'label': i, 'value': i} for i in service_options_df['service'].unique()] + [{'label': 'All', 'value': 'All'}]

    # Apply filtering for the sunburst chart
    if selected_pillar != 'All':
        filtered_df = filtered_df[filtered_df['pillar'] == selected_pillar]

    if selected_area != 'All':
        filtered_df = filtered_df[filtered_df['area'] == selected_area]

    if selected_service != 'All':
        filtered_df = filtered_df[filtered_df['service'] == selected_service]

    filtered_df = filtered_df[(filtered_df['cost'] >= cost_range[0]) & (filtered_df['cost'] <= cost_range[1])]

    # Define a custom color map for the pillars (as identified in previous analysis)
    custom_color_map = {
        'Project Design': '#1f77b4',
        'Management': '#ff7f0e',
        'Construction': '#2ca02c',
        'Finishing & Landscaping': '#d62728',
        '(?)': '#cccccc'
    }

    # Generate the sunburst chart using px.sunburst
    # Acknowledging the limitation of combined discrete pillar colors and within-pillar cost gradients
    fig = px.sunburst(
        filtered_df,
        path=['pillar', 'area', 'service', 'task', 'sub_task'],
        values='cost',
        color='pillar',  # Color by pillar using the discrete map
        color_discrete_map=custom_color_map,
        custom_data=['cost', 'budgeted_cost'] # Include budget data for tooltips
    )

    # Update trace settings based on guidelines (line thickness, textinfo, hovertemplate)
    fig.update_traces(
        textinfo='label+percent parent', # Keep simplified textinfo for clarity
        hovertemplate='<b>%{label}</b><br><br>'
                      '<b>Actual Cost:</b> $%{customdata[0]:,.0f}<br>'
                      '<b>Budgeted Cost:</b> $%{customdata[1]:,.0f}<br>'
                      '<b>Variance:</b> $%{(customdata[0] - customdata[1]):,.0f}<br>'
                      '<b>Contribution to Parent:</b> %{percentParent:.2%}<br>'
                      f'<b>Contribution to Total:</b> %{{percentRoot:.2%}}<extra></extra>',
        insidetextorientation='radial',
        textfont_size=10, # Reasonable text size
        marker=dict(line=dict(color='#ffffff', width=1)), # Reduced marker line width
    )

    # Update layout settings (title, margins)
    fig.update_layout(
        title_text='<b>Residential Construction: Hierarchical Cost Explorer</b>', # Clear title
        title_x=0.5, # Center title
        font=dict(family='Arial, sans-serif', size=16), # Consistent font
        margin=dict(t=120, l=40, r=40, b=40), # Adjust margins for controls
    )

    return fig, area_options, service_options

# Run the Dash application (for Colab inline display)
if __name__ == '__main__':
    app.run(debug=True, jupyter_mode='inline')