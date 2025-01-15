# Importing necessary libraries
import plotly.graph_objects as go

# Define the data for the Sankey diagram
data = dict(
    type='sankey',
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["The Glen Canyon Dam", "The Hoover Dam",
               "Arizona", "California", "Wyoming", "New Mexico", "Colorado",
               "AZ_agriculture", "AZ_industry","AZ_residential",
               "CA_agriculture", "CA_industry", "CA_residential",
               "WY_agriculture", "WY_industry", "WY_residential",
               "NM_agriculture", "WY_industry", "NM_residential",
               "CO_agriculture", "WY_industry","CO_residential"],


    ),
    link=dict(
        source=[0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],  # indices correspond to labels
        target=[4, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
        value=[20, 8, 60, 5,22, 5, 1, 2, 45,5,10, 18, 1, 1, 4, 1, 1, 18, 3, 1],

    )
)

# Create the Sankey figure
fig = go.Figure(data=[go.Sankey(**data)])

# Update layout for better appearance
fig.update_layout(
    title_text="Water Distribution Sankey Diagram",
    title_x=0.5,
    title_y=0.99,
    title_xanchor='center',
    title_yanchor='top',
    font_size = 10)

# Show the figure
fig.show()
