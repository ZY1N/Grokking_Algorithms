# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greedy.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yinzhang <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/29 18:39:11 by yinzhang          #+#    #+#              #
#    Updated: 2019/11/29 19:16:59 by yinzhang         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#sets are lists without any duplicates
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"]) 
stations["kfive"] = set(["ca", "az"])

final_stations = set()

#for station, states_for_station in stations.items():
    #print states_for_station
    #print statio

#print(stations.items())
#print(stations)

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station 
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print final_stations