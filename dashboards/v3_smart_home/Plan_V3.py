# Develop Complex Dashboard Code (Iterative) - Integrate Predictive Analysis

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.colors
from sklearn.model_selection import train_test_split # Import necessary ML libraries
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming df_complex is already defined from the previous step
# display(df_complex.head()) # Uncomment to verify data

app = Dash(__name__)

# --- Prepare Data for Predictive Analysis ---
# Define features (X) and target (y) for prediction
# We'll use numerical features and one-hot encode the Installation_Type
X = df_complex[['Installation_Cost', 'Number_of_Devices', 'Customer_Satisfaction']]
X = pd.get_dummies(X, columns=['Installation_Cost', 'Number_of_Devices', 'Customer_Satisfaction'], drop_first=True) # One-hot encode categorical features
y = df_complex['Annual_Energy_Savings']

# For simplicity in this dashboard integration, we'll train the model once on the full dataset.
# In a real-world scenario, you would split data and train appropriately.
model = LinearRegression()
# Train the model
model.fit(X, y)

# Get feature importances (using coefficients for Linear Regression)
feature_importance = pd.DataFrame({'feature': X.columns, 'importance': model.coef_})
feature_importance['importance'] = feature_importance['importance'].abs() # Use absolute value for importance visualization
feature_importance = feature_importance.sort_values('importance', ascending=False)


# --- Dashboard Layout ---
# Based on the plan, include filters and placeholders for charts

app.layout = html.Div([
    html.H1("Smart Home Installation Analytics Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.Label("Select Region:"),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['Region'].unique()] +
                        [{'label': 'All', 'value': 'All'}],
                value='All',
                clearable=False
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'margin-right': '20px'}),

        html.Div([
            html.Label("Select City:"),
            dcc.Dropdown(
                id='city-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['City'].unique()] +
                        [{'label': 'All', 'value': 'All'}],
                value='All',
                clearable=False
            ),
        ], style={'width': '30%', 'display': 'inline-block', 'margin-right': '20px'}),

         html.Div([
            html.Label("Select Installation Type:"),
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': i, 'value': i} for i in df_complex['Installation_Type'].unique()] +
                        [{'label': 'All', 'value': 'All'}],
                value='All',
                clearable=False
            ),
        ], style={'width': '30%', 'display': 'inline-block'}),
    ], style={'padding': '20px'}), # Filter controls container


    html.Div([
        # Placeholder for Hierarchical Chart (Sunburst or Treemap)
        html.Div([
            dcc.Graph(id='hierarchical-chart', style={'height': '400px'})
        ], style={'width': '50%', 'display': 'inline-block'}),

        # Placeholder for Map Visualization
         html.Div([
            dcc.Graph(id='map-visualization', style={'height': '400px'})
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'padding': '20px'}), # Top row charts container

     html.Div([
        # Placeholder for Scatter Plot
         html.Div([
            dcc.Graph(id='scatter-plot', style={'height': '400px'})
        ], style={'width': '50%', 'display': 'inline-block'}),

        # Placeholder for Predictive Analysis Visualization (e.g., Feature Importance or Prediction Plot)
         html.Div([
            dcc.Graph(id='predictive-viz', style={'height': '400px'})
        ], style={'width': '50%', 'display': 'inline-block'}),
    ], style={'padding': '20px'}), # Bottom row charts container

])

# --- Callbacks for Interactivity and Chart Updates ---

@app.callback(
    Output('city-dropdown', 'options'),
    Output('city-dropdown', 'value'), # Also update the value when options change
    Input('region-dropdown', 'value')
)
def set_cities_options(selected_region):
    if selected_region == 'All':
        cities = df_complex['City'].unique()
    else:
        cities = df_complex[df_complex['Region'] == selected_region]['City'].unique()
    city_options = [{'label': i, 'value': i} for i in cities] + [{'label': 'All', 'value': 'All'}]
    return city_options, 'All' # Reset city selection to 'All' when region changes


@app.callback(
    Output('hierarchical-chart', 'figure'),
    Output('map-visualization', 'figure'),
    Output('scatter-plot', 'figure'),
    Output('predictive-viz', 'figure'), # Add predictive viz output here
    Input('region-dropdown', 'value'),
    Input('city-dropdown', 'value'),
    Input('type-dropdown', 'value')
)
def update_complex_dashboard(selected_region, selected_city, selected_type):
    filtered_df = df_complex.copy()

    # Apply filters
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_city != 'All':
        filtered_df = filtered_df[filtered_df['City'] == selected_city]
    if selected_type != 'All':
        filtered_df = filtered_df[filtered_df['Installation_Type'] == selected_type]

    # --- Generate Hierarchical Chart (Sunburst Example) ---
    # Using Sunburst as planned, showing breakdown by Region, City, Type
    if not filtered_df.empty:
        hierarchical_fig = px.sunburst(
            filtered_df,
            path=['Region', 'City', 'Installation_Type'],
            values='Installation_Cost', # Or use 'Number_of_Devices'
            title='Hierarchical Breakdown of Installations'
        )
         # Customize tooltip for hierarchical chart
        hierarchical_fig.update_traces(hovertemplate='<b>%{label}</b><br>Cost: $%{value:,.0f}<extra></extra>')
    else:
        hierarchical_fig = go.Figure()
        hierarchical_fig.update_layout(title='No data available for selected filters')


    # --- Generate Map Visualization ---
    # Using Scattergeo to plot points on a map
    if not filtered_df.empty:
        map_fig = px.scatter_geo(
            filtered_df,
            lat='Latitude',
            lon='Longitude',
            hover_name='City',
            size='Installation_Cost', # Size markers by cost
            color='Region', # Color markers by region
            projection="albers usa", # Or a different projection
            title='Geographic Distribution of Installations'
        )
        map_fig.update_layout(geo=dict(scope='usa')) # Limit scope to USA for the example cities
        # Customize tooltip for map
        map_fig.update_traces(hovertemplate='<b>%{hover_name}</b><br>Cost: $%{size:,.0f}<br>Region: %{customdata[0]}<extra></extra>',
                              customdata=filtered_df[['Region']]) # Include Region in customdata for tooltip


    else:
        map_fig = go.Figure()
        map_fig.update_layout(title='No data available for selected filters')


     # --- Generate Scatter Plot ---
     # Relationship between Installation Cost and Annual Energy Savings
    if not filtered_df.empty:
        scatter_fig = px.scatter(
            filtered_df,
            x='Installation_Cost',
            y='Annual_Energy_Savings',
            color='Installation_Type', # Color by installation type
            hover_name='City',
            title='Installation Cost vs. Annual Energy Savings'
        )
         # Customize tooltip for scatter plot
        scatter_fig.update_traces(hovertemplate='<b>City: %{hover_name}</b><br>Cost: $%{x:,.0f}<br>Savings: $%{y:,.0f}<br>Type: %{customdata[0]}<extra></extra>',
                                  customdata=filtered_df[['Installation_Type']])
    else:
        scatter_fig = go.Figure()
        scatter_fig.update_layout(title='No data available for selected filters')


    # --- Predictive Analysis Visualization (Feature Importance Bar Chart) ---
    # Use the pre-calculated feature_importance DataFrame
    predictive_fig = px.bar(
        feature_importance,
        x='importance',
        y='feature',
        orientation='h',
        title='Feature Importance for Energy Savings Prediction',
        labels={'importance': 'Absolute Coefficient Value', 'feature': 'Feature'}
    )
    predictive_fig.update_layout(yaxis={'categoryorder':'total ascending'}) # Order features by importance

    # Return all figures
    return hierarchical_fig, map_fig, scatter_fig, predictive_fig


# Run the Dash application (for Colab inline display)
if __name__ == '__main__':
    # Note: In a real application, you might adjust the host and port
    # app.run_server(debug=True, mode='inline') # Alternative run method for newer Dash versions
     app.run(debug=True, jupyter_mode='inline')