#!/usr/bin/env python3

class EventManager:
    def __init__(self):
        self.__prefix_sums = [0]
        self.__last_i = 0
        self.__ids = {}

    def add_event(self, id, weight):
        self.__prefix_sums.append(self.__prefix_sums[-1]+weight)
        self.__last_i += 1
        self.__ids[id] = self.__last_i


    def average_weight(self, k):
        if k <= 0:
            return 0.0
        
        num_events = len(self.__prefix_sums)-1
        events_to_avg = min(num_events, k)
        start_index = len(self.__prefix_sums)-events_to_avg-1

        return (self.__prefix_sums[-1]-self.__prefix_sums[start_index])/events_to_avg