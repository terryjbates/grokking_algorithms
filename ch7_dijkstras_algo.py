#!/usr/bin/env python
import sys
import os
from pprint import pprint as pprint

def main():
    
    # Create graph to store nodes and edges
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    
    # Represent weighted edges for the 'start' node
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    pprint(graph['start']['a'])
    pprint(graph['start']['b'])

    # Represent other nodes and neighbors
    graph['a'] = {}
    graph['a']['fin'] = 1

    graph['b'] = {}
    graph['b']['a'] = 3 
    graph['b']['fin'] = 5

    graph['fin'] = {}

    # Create code for costs
    infinity = float('inf')
    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    # Create code for parent nodes
    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    # Create processed node data struct
    processed = set()

    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node




    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.add(node)
        node = find_lowest_cost_node(costs)
    pprint(costs)


if __name__ == "__main__":
    main()
