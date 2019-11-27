# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bfs.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/25 22:28:27 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/27 12:19:21 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_q = deque()
    search_q += graph[name]
    searched = []
    while search_q:
        person = search_q.popleft()
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller"
                return True
            else:
                search_q += graph[person]
                searched.append(person)
    return False

graph = {}
graph["you"] = ["alice", "bob", "claire"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"] 
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")
