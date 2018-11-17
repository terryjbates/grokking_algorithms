#!/usr/bin/env python

from collections import deque

def person_is_seller(name):
        return name[-1] == 'm'

def main():
    graph ={}
    seen_people = set()

    graph['you'] = ['tom', 'dick', 'humper']
    graph['dick'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['humper'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []

    search_queue = deque()
    search_queue += graph["you"]

    while search_queue:
        person = search_queue.popleft()
        if person_is_seller(person):
            print("{} sells MANGOOOO!".format(person))
            return True
        else:
            search_queue += graph[person]
    return False



if __name__ == "__main__":
    main()
