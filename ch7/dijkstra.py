# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dijkstra.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/27 19:58:34 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/29 15:35:58 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#step one is to make the graph of the map
graph = {}
graph["start"] = {} 
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {} 
graph["a"]["fin"] = 1

graph["b"] = {} 
graph["b"]["a"] = 3 
graph["b"]["fin"] = 5

graph["fin"] = {}

#step 2 is to make a table for the costs of the first node

infinity = float("inf")
infinity = float("inf") 

costs = {}
costs["a"] = 6 
costs["b"] = 2 
costs["fin"] = infinity

#step 3 is to make hash table for the parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

#make an array to keep track of where we are going
processed = []

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
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
