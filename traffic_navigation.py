# traffic_navigation.py
import networkx as nx
from machine_learning_model import TrafficPredictionModel

def find_optimal_route(start, destination, traffic_data):
    graph = build_traffic_graph(traffic_data)
    shortest_path = nx.shortest_path(graph, source=start, target=destination, weight='weight')
    return shortest_path

def build_traffic_graph(traffic_data):
    # Build a graph based on traffic data
    G = nx.Graph()
    for edge in traffic_data:
        G.add_edge(edge['source'], edge['destination'], weight=edge['traffic_time'])
    return G
