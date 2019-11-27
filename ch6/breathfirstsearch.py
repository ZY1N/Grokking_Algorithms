# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    breathfirstsearch.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/27 12:18:51 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/27 14:16:14 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import deque
#from _future_ import print_function

def ismangoseller(person):
    if person == "thom":
        return True
    return False

def bfs(name):
    queue = deque()
    searched = []
    queue += graph[name]

    while queue:
        person = queue.popleft()
        if ismangoseller(person):
            print(person + "is mango seller")
            return True
        else:
            #queue = queue + graph[person]
            #queue.append(graph[person])
            print("ab") 
            map(lambda x: queue.append(x), graph[person])
            #map(queue.append(graph[person]), graph[person])
    return False

#note that += queue to the list is okay 
#map(function, iterable) is also okay if the lambda appends the iterable to the queue

graph = {}
graph["you"] = ["alice", "bob", "claire"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

bfs("you")
