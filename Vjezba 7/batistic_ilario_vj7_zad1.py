import networkx as nx
from batistic_ilario_vj7_helper_functions import loadGraph
from time import time

def djiskra_algorithm(graph):
    start = time()
    #shortest_path = nx.shortest_path(graph, weight='weight', method='dijkstra')
    shortest_path = nx.shortest_path(graph, source='LHR', target='VIE', weight='weight', method='dijkstra')
    end = time()
    shortest_path_length = nx.shortest_path_length(graph, source='LHR', target='VIE', weight='weight', method='dijkstra')
    print(f"\n\nDJIKSTRA: \n\nShortest path: {shortest_path}\n\nShortest path lenght: {shortest_path_length is None if 0 else shortest_path_length}\n\nTime: {end - start}")


def belman_form_algorithm(graph):
    start = time()
    #shortest_path = nx.shortest_path(graph, weight='weight', method='bellman-ford')
    shortest_path = nx.shortest_path(graph, source='LHR', target='VIE', weight='weight', method='bellman-ford')
    end = time()
    shortest_path_length = nx.shortest_path_length(graph, source='LHR', target='VIE', weight='weight', method='bellman-ford')
    print(f"\n\nBELLMAN FORD: \n\nShortest path: {shortest_path}\n\nShortest path lenght: {shortest_path_length is None if 0 else shortest_path_length}\n\nTime: {end - start}")


def zad1():
    graph = loadGraph("gradovi-udaljenost.net")
    djiskra_algorithm(graph)
    belman_form_algorithm(graph)