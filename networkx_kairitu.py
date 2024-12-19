import networkx as nx
import pandas as pd

# Load data (example using pandas)
data = pd.read_csv("network_data.csv") # Assuming CSV with 'source' and 'target' columns

# Create a graph
graph = nx.from_pandas_edgelist(data, source='source', target='target')

# Perform analysis (example: calculate degree centrality)
degree_centrality = nx.degree_centrality(graph)

#Print degree centrality
print(degree_centrality)

# Visualize the graph (example using matplotlib)
nx.draw(graph)
plt.show()
