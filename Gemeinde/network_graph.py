import plotly.graph_objects as go
import networkx as nx
import pandas as pd

# Load data
df = pd.read_excel('neural.xlsx')

# Print columns to ensure we know the correct names
print("Columns in the DataFrame:", df.columns)

# Define columns
source_col = 'District'  # Replace with the actual column for the source
target_col = 'Ethnicity'  # Replace with the actual column for the target
profession_col = 'Professions'  # Replace with actual column name
passion_col = 'Passions'  # Replace with actual column name
community_col = 'Community'  # Replace with actual column name
language_col='Language'

# Create graph
G = nx.Graph()

# Add edges based on the chosen columns
for _, row in df.iterrows():
    G.add_edge(row[source_col], row[target_col])  # District → Ethnicity
    if pd.notna(row[profession_col]):
        G.add_edge(row[community_col], row[profession_col])  # Community → Professions
    if pd.notna(row[passion_col]):
        G.add_edge(row[community_col], row[passion_col])  # District → Passions
    if pd.notna(row[community_col]):
        G.add_edge(row[source_col], row[community_col])  # District → Community
    if pd.notna(row[language_col]):
        G.add_edge(row[community_col], row[language_col])  # District → Community
    

# Get node positions using a spring layout
pos = nx.spring_layout(G, seed=120, k=2, iterations=200)

# Extract edge positions
edge_x, edge_y = [], []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Extract node positions and set node sizes
node_x, node_y, node_colors, node_sizes = [], [], [], []
ethnicity_colors = {'Sachsen': 'lightgray', 'Musical': 'red', 'Greek': 'lightgray'}

# Assign colors to nodes
for node in G.nodes():
    if node in df[source_col].values:  # Districts
        node_colors.append('lightgray')
    elif node in df[target_col].values:  # Ethnicities
        node_colors.append(ethnicity_colors.get(node, 'green'))
    elif node in df[profession_col].values:  # Professions
        node_colors.append('darkblue')
    elif node in df[passion_col].values:  # Passions
        node_colors.append('orange')
    elif node in df[community_col].values:
        node_colors.append('darkred')
    elif node in df[language_col].values:
        node_colors.append('turquoise')
    else:
        node_colors.append('lightgray')
    
    node_sizes.append(30 + G.degree[node] * 10)  # Node size scaling
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

# Create edge trace
edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1, color='rgba(0,0,0,0.5)'),
    hoverinfo='none',
    mode='lines'
)

import matplotlib.colors as mcolors

def get_text_color(hex_color):
    """Determine if text should be white or dark blue based on background brightness."""
    rgb = mcolors.hex2color(mcolors.CSS4_COLORS.get(hex_color, hex_color))  # Convert color name or hex to RGB
    brightness = sum(rgb) / 3  # Simple brightness check (0 = dark, 1 = bright)
    return "#FFFFFF" if brightness < 0.5 else "#00008B"  # White for dark backgrounds, Dark Blue for light ones

# Generate text colors dynamically
text_colors = [get_text_color(c) for c in node_colors]

# Create node trace with text color adjustments
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    marker=dict(
        size=node_sizes,
        color=node_colors,
        colorscale='redor',
        line=dict(width=2, color='gray')
    ),
    text=[f" {node}" for node in G.nodes()],
    textfont=dict(color=text_colors),  # Apply dynamic text color
    hoverinfo='text'
)


# Create figure
fig = go.Figure(data=[edge_trace, node_trace])

# Update layout
fig.update_layout(
    showlegend=False,
    hovermode='closest',
    title="German Community in a Network Graph",
    title_x=0.5,
    margin=dict(b=0, l=0, r=0, t=40),
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
    plot_bgcolor='white'
)

fig.show()
