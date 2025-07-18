
# Final Python code for the Dash application

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import plotly.colors

# This data structure defines our 5-level hierarchy with budget data.
data = [
    # Pillar 1: Project Design
    {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Blueprint Design', 'task': 'Initial Schematics & 3D Model', 'sub_task': 'Site Survey', 'cost': 15000, 'budgeted_cost': 14000},
    {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Blueprint Design', 'task': 'Initial Schematics & 3D Model', 'sub_task': 'Conceptual Design', 'cost': 20000, 'budgeted_cost': 18000},
    {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Blueprint Design', 'task': 'Initial Schematics & 3D Model', 'sub_task': 'Detailed Drawings', 'cost': 30000, 'budgeted_cost': 28000},

    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Structural Analysis', 'task': 'Foundation & Frame Calculations', 'sub_task': 'Soil Testing', 'cost': 25000, 'budgeted_cost': 24000},
    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Structural Analysis', 'task': 'Foundation & Frame Calculations', 'sub_task': 'Load Bearing Calculations', 'cost': 35000, 'budgeted_cost': 33000},
    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Structural Analysis', 'task': 'Foundation & Frame Calculations', 'sub_task': 'Frame Design', 'cost': 35000, 'budgeted_cost': 34000},

    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'MEP Engineering', 'task': 'HVAC & Electrical Plans', 'sub_task': 'HVAC Design', 'cost': 40000, 'budgeted_cost': 38000},
    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'MEP Engineering', 'task': 'HVAC & Electrical Plans', 'sub_task': 'Electrical Design', 'cost': 45000, 'budgeted_cost': 43000},

    {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Interior Design', 'task': 'Material Selection & Layout', 'sub_task': 'Finish Selection', 'cost': 20000, 'budgeted_cost': 19000},
    {'pillar': 'Project Design', 'area': 'Architecture', 'service': 'Interior Design', 'task': 'Material Selection & Layout', 'sub_task': 'Layout Planning', 'cost': 20000, 'budgeted_cost': 18000},

    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Civil Engineering', 'task': 'Drainage & Grading Plan', 'sub_task': 'Drainage Design', 'cost': 15000, 'budgeted_cost': 14000},
    {'pillar': 'Project Design', 'area': 'Engineering', 'service': 'Civil Engineering', 'task': 'Drainage & Grading Plan', 'sub_task': 'Grading Plan', 'cost': 15000, 'budgeted_cost': 13000},


    # Pillar 2: Management & Logistics
    {'pillar': 'Management', 'area': 'Administration', 'service': 'Project Management', 'task': 'On-Site Supervision & Reporting', 'sub_task': 'Daily Supervision', 'cost': 70000, 'budgeted_cost': 68000},
    {'pillar': 'Management', 'area': 'Administration', 'service': 'Project Management', 'task': 'On-Site Supervision & Reporting', 'sub_task': 'Progress Reporting', 'cost': 60000, 'budgeted_cost': 58000},

    {'pillar': 'Management', 'area': 'Administration', 'service': 'Permits & Legal', 'task': 'City & Environmental Approvals', 'sub_task': 'Permit Application', 'cost': 50000, 'budgeted_cost': 48000},
    {'pillar': 'Management', 'area': 'Administration', 'service': 'Permits & Legal', 'task': 'City & Environmental Approvals', 'sub_task': 'Environmental Review', 'cost': 40000, 'budgeted_cost': 38000},

    {'pillar': 'Management', 'area': 'Logistics', 'service': 'Supply Chain', 'task': 'Material Sourcing & Delivery', 'sub_task': 'Material Sourcing', 'cost': 35000, 'budgeted_cost': 33000},
    {'pillar': 'Management', 'area': 'Logistics', 'service': 'Supply Chain', 'task': 'Material Sourcing & Delivery', 'sub_task': 'Delivery Coordination', 'cost': 35000, 'budgeted_cost': 34000},

    {'pillar': 'Management', 'area': 'Administration', 'service': 'Financial Management', 'task': 'Budget Tracking & Invoicing', 'sub_task': 'Budget Monitoring', 'cost': 30000, 'budgeted_cost': 29000},
    {'pillar': 'Management', 'area': 'Administration', 'service': 'Financial Management', 'task': 'Budget Tracking & Invoicing', 'sub_task': 'Invoicing', 'cost': 30000, 'budgeted_cost': 28000},

    {'pillar': 'Management', 'area': 'Logistics', 'service': 'Equipment Rental', 'task': 'Heavy Machinery & Tools', 'sub_task': 'Machinery Rental', 'cost': 30000, 'budgeted_cost': 29000},
    {'pillar': 'Management', 'area': 'Logistics', 'service': 'Equipment Rental', 'task': 'Heavy Machinery & Tools', 'sub_task': 'Tool Rental', 'cost': 25000, 'budgeted_cost': 24000},


    # Pillar 3: Construction
    {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Excavation & Grading', 'task': 'Earthwork and Site Prep', 'sub_task': 'Excavation', 'cost': 80000, 'budgeted_cost': 78000},
    {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Excavation & Grading', 'task': 'Earthwork and Site Prep', 'sub_task': 'Grading', 'cost': 80000, 'budgeted_cost': 79000},

    {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Concrete Work', 'task': 'Foundation Pouring & Curing', 'sub_task': 'Formwork', 'cost': 100000, 'budgeted_cost': 98000},
    {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Concrete Work', 'task': 'Foundation Pouring & Curing', 'sub_task': 'Pouring', 'cost': 150000, 'budgeted_cost': 148000},
    {'pillar': 'Construction', 'area': 'Site & Foundation', 'service': 'Concrete Work', 'task': 'Foundation Pouring & Curing', 'sub_task': 'Curing', 'cost': 60000, 'budgeted_cost': 58000},

    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Framing & Steel', 'task': 'Wood & Steel Frame Erection', 'sub_task': 'Wood Framing', 'cost': 280000, 'budgeted_cost': 275000},
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Framing & Steel', 'task': 'Wood & Steel Frame Erection', 'sub_task': 'Steel Erection', 'cost': 200000, 'budgeted_cost': 198000},

    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'task': 'Complete Wiring & Fixtures', 'sub_task': 'Wiring Installation', 'cost': 150000, 'budgeted_cost': 145000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Electrical', 'task': 'Complete Wiring & Fixtures', 'sub_task': 'Fixture Installation', 'cost': 90000, 'budgeted_cost': 88000},

    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Plumbing & HVAC', 'task': 'Piping, Drains & Ductwork', 'sub_task': 'Plumbing Installation', 'cost': 130000, 'budgeted_cost': 128000},
    {'pillar': 'Construction', 'area': 'MEP Systems', 'service': 'Plumbing & HVAC', 'task': 'Piping, Drains & Ductwork', 'sub_task': 'HVAC Installation', 'cost': 130000, 'budgeted_cost': 125000},

    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Drywall & Painting', 'task': 'Interior Walls and Ceilings', 'sub_task': 'Drywall Installation', 'cost': 100000, 'budgeted_cost': 98000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Drywall & Painting', 'task': 'Interior Walls and Ceilings', 'sub_task': 'Painting', 'cost': 90000, 'budgeted_cost': 88000},

    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Flooring & Tiling', 'task': 'Hardwood and Ceramic Installation', 'sub_task': 'Hardwood Installation', 'cost': 100000, 'budgeted_cost': 95000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Flooring & Tiling', 'task': 'Hardwood and Ceramic Installation', 'sub_task': 'Tiling', 'cost': 75000, 'budgeted_cost': 73000},

    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Roofing', 'task': 'Shingle and Underlayment Installation', 'sub_task': 'Underlayment', 'cost': 40000, 'budgeted_cost': 38000},
    {'pillar': 'Construction', 'area': 'Superstructure', 'service': 'Roofing', 'task': 'Shingle and Underlayment Installation', 'sub_task': 'Shingle Installation', 'cost': 80000, 'budgeted_cost': 78000},

    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Window & Door Installation', 'task': 'Exterior and Interior Openings', 'sub_task': 'Window Installation', 'cost': 50000, 'budgeted_cost': 48000},
    {'pillar': 'Construction', 'area': 'Interior & Exterior', 'service': 'Window & Door Installation', 'task': 'Exterior and Interior Openings', 'sub_task': 'Door Installation', 'cost': 40000, 'budgeted_cost': 38000},


    # New Pillar: Finishing & Landscaping
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Cabinetry Installation', 'cost': 90000, 'budgeted_cost': 88000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Cabinetry & Countertops', 'task': 'Kitchen and Bathroom Fixtures', 'sub_task': 'Countertop Installation', 'cost': 60000, 'budgeted_cost': 58000},

    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Lighting Fixtures', 'cost': 35000, 'budgeted_cost': 34000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Finishing', 'service': 'Fixtures & Hardware', 'task': 'Lighting, Faucets, and Door Knobs', 'sub_task': 'Faucets and Hardware', 'cost': 35000, 'budgeted_cost': 33000},

    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Patio and Walkway Construction', 'cost': 50000, 'budgeted_cost': 48000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Hardscaping', 'task': 'Patio, Walkways, and Retaining Walls', 'sub_task': 'Retaining Wall Construction', 'cost': 30000, 'budgeted_cost': 29000},

    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Lawn Installation', 'cost': 20000, 'budgeted_cost': 19000},
    {'pillar': 'Finishing & Landscaping', 'area': 'Landscaping', 'service': 'Softscaping', 'task': 'Lawn, Plants, and Trees', 'sub_task': 'Planting and Tree Installation', 'cost': 20000, 'budgeted_cost': 18000},
]
df_budget = pd.DataFrame(data)

app = Dash(__name__)

# Get min and max cost for the range slider
min_cost = df_budget['cost'].min()
max_cost = df_budget['cost'].max()

app.layout = html.Div([
    html.H1("Residential Construction: Hierarchical Cost Explorer"),
    html.Label("Select Pillar:"),
    dcc.Dropdown(
        id='pillar-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['pillar'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(), # Add a line break for spacing
    html.Label("Select Area:"),
    dcc.Dropdown(
        id='area-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['area'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(), # Add a line break for spacing
    html.Label("Select Service:"),
    dcc.Dropdown(
        id='service-dropdown',
        options=[{'label': i, 'value': i} for i in df_budget['service'].unique()] +
                [{'label': 'All', 'value': 'All'}],
        value='All'
    ),
    html.Br(), # Add a line break for spacing
    html.Label("Filter by Cost Range:"),
    dcc.RangeSlider(
        id='cost-range-slider',
        min=min_cost,
        max=max_cost,
        value=[min_cost, max_cost], # Default to the full range
        marks={int(min_cost): f'${int(min_cost):,}',
               int(max_cost): f'${int(max_cost):,}'}, # Add marks for min and max cost
        step=5000 # Define a step for the slider
    ),
    dcc.Graph(id='sunburst-chart')
])

@app.callback(
    Output('sunburst-chart', 'figure'),
    Output('area-dropdown', 'options'), # Add output for area dropdown options
    Output('service-dropdown', 'options'), # Add output for service dropdown options
    Input('pillar-dropdown', 'value'),
    Input('area-dropdown', 'value'),
    Input('service-dropdown', 'value'),
    Input('cost-range-slider', 'value')
)
def update_graph(selected_pillar, selected_area, selected_service, cost_range):
    filtered_df = df_budget.copy() # Use a copy to avoid modifying the original DataFrame

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


    # Apply filtering for the sunburst chart based on selected values
    if selected_pillar != 'All':
        filtered_df = filtered_df[filtered_df['pillar'] == selected_pillar]

    if selected_area != 'All':
        filtered_df = filtered_df[filtered_df['area'] == selected_area]

    if selected_service != 'All':
        filtered_df = filtered_df[filtered_df['service'] == selected_service]

    filtered_df = filtered_df[(filtered_df['cost'] >= cost_range[0]) & (filtered_df['cost'] <= cost_range[1])]

    # Define a custom color map for the pillars
    custom_color_map = {
        'Project Design': '#1f77b4',  # Muted blue
        'Management': '#ff7f0e',      # Muted orange
        'Construction': '#2ca02c',    # Muted green
        'Finishing & Landscaping': '#d62728', # Muted red
        '(?)': '#cccccc'              # Grey for any potential missing categories
    }

    # Generate the sunburst chart, coloring by pillar
    # Note: Achieving sequential color gradients within lower levels while coloring the outermost
    # ring by a discrete variable ('pillar') is a limitation of plotly.express.sunburst.
    # This requires more complex handling, potentially with plotly.graph_objects.Sunburst
    # and manual color assignment based on hierarchy and cost.
    # For this implementation, we prioritize distinct pillar colors for clarity on the top level.
    fig = px.sunburst(
        filtered_df,
        path=['pillar', 'area', 'service', 'task', 'sub_task'],
        values='cost',
        color='pillar',  # Color the outermost ring distinctly by pillar
        color_discrete_map=custom_color_map,
        custom_data=['cost', 'budgeted_cost']
    )

    # Update trace settings
    fig.update_traces(
        textinfo='label+percent parent', # Keep simplified textinfo
        hovertemplate='<b>%{label}</b><br><br>'
                      '<b>Actual Cost:</b> $%{customdata[0]:,.0f}<br>'
                      '<b>Budgeted Cost:</b> $%{customdata[1]:,.0f}<br>'
                      '<b>Variance:</b> $%{(customdata[0] - customdata[1]):,.0f}<br>'
                      '<b>Contribution to Parent:</b> %{percentParent:.2%}<br>'
                      f'<b>Contribution to Total:</b> %{{percentRoot:.2%}}<extra></extra>',
        insidetextorientation='radial',
        textfont_size=10,
        marker=dict(line=dict(color='#ffffff', width=1)), # Reduced marker line width
    )

    # Update layout settings
    fig.update_layout(
        title_text='<b>Residential Construction: Hierarchical Cost Explorer</b>',
        title_x=0.5, font=dict(family='Arial, sans-serif', size=16),
        margin=dict(t=120, l=40, r=40, b=40),
    )

    return fig, area_options, service_options

if __name__ == '__main__':
    app.run(debug=True, jupyter_mode='inline')
