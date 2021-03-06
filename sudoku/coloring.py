"""Graph coloring algorithms."""

import networkx as nx
from math import sqrt
from queue import *
import random

def welsh_powell(graph):
    """Runs the Welsh-Powell algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _welsh(graph):
        for node in graph.node:
            if not graph.node[node]['fixed']:
                for neighbor in graph.neighbors(node):
                    if (graph.node[neighbor]['fixed']):
                        try:
                            graph.node[node]['label'].remove(
                                graph.node[neighbor]['label'])
                        except:
                            pass

    def _update(graph):
        for node in graph.node:
            if (not graph.node[node]['fixed'] and
                    len(graph.node[node]['label']) == 1):
                graph.node[node]['fixed'] = True
                graph.node[node]['label'] = graph.node[node]['label'][0]

    def _clear(graph):
        for node in graph.node:
            if (graph.node[node]['fixed'] and
                    type(graph.node[node]['label']) is not int):
                graph.node[node]['fixed'] = False

    def _engage(graph):
        for i in range(size):
            for j in range(size):
                name = '{}{}'.format(i, j)
                if not graph.node[name]['fixed']:
                    graph.node[name]['fixed'] = True
                    _welsh(graph)
                    _update(graph)
        _clear(graph)

    size = int(sqrt(len(graph.node)))
    for node in graph.node:
        if (graph.node[node]['label'] is None):
            graph.node[node]['label'] = [(x + 1) for x in range(size)]

    for i in range(size):
        _engage(graph)
        _welsh(graph)
        _update(graph)

    return graph


def sequencial_coloring(graph):
    """Runs the Sequencial Coloring algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """

    def is_label_possible(graph, node, label):
        for neighbor in graph.neighbors(node):
            if graph.node[neighbor]['label'] == label:
                return False
        return True

    size = int(sqrt(len(graph.node)))
    labels = [(x + 1) for x in range(size)]
    for label in labels:
        for node in graph.node:
            if is_label_possible(graph, node, label):
                graph.node[node]['label'] = label
    return graph


def class_coloring(graph):
    """Runs the Class Coloring algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """

    def _init_classes_and_candidates(graph,classes,candidates):
        for node in graph.node:
            if graph.node[node]['fixed']:
                classes[graph.node[node]['label'] - 1].add(node)
            else:
                candidates.append(node)

    def _coloring(graph,candidates,classes):
        while len(candidates) != 0:
            v = candidates.pop()
            for i in range(len(classes)):
                neigh_set = set(graph.neighbors(v))
                if len(classes[i].intersection(neigh_set)) == 0:
                    classes[i].add(v)
                    graph.node[v]['label'] = i + 1
                    break

    size = int(sqrt(len(graph.node)))
    classes = [set() for x in range(size)]
    candidates = []
    _init_classes_and_candidates(graph,classes,candidates)
    _coloring(graph,candidates,classes)

    return graph

def class_coloring_backtracking(graph):
    """Runs the Class Coloring Backtracking algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _candidate_was_colored(graph,node):
        return graph.node[node]['label'] != None

    def _remove_from_class(last_colored,classes):
        for c in classes:
            if last_colored in c:
                c.remove(last_colored)

    def _init_classes_and_candidates(graph, classes, candidates):
        for node in graph.node:
            if graph.node[node]['fixed']:
                classes[graph.node[node]['label'] - 1].add(node)
            else:
                candidates.append(node)

    def _coloring(graph, candidates, classes, colored_stack):
        while len(candidates) != 0:
            v = candidates.pop()
            init_index = 0 if type(graph.node[v]['label']) != int else graph.node[v]['label']
            graph.node[v]['label'] = None
            for i in range(init_index,len(classes)):
                neigh_set = set(graph.neighbors(v))
                if len(classes[i].intersection(neigh_set)) == 0:
                    classes[i].add(v)
                    graph.node[v]['label'] = i + 1
                    colored_stack.append(v)
                    break
            if not _candidate_was_colored(graph,v):
                candidates.append(v)
                last_colored = colored_stack.pop()
                _remove_from_class(last_colored,classes)
                candidates.append(last_colored)

    size = int(sqrt(len(graph.node)))
    classes = [set() for x in range(size)]
    candidates = []
    colored_stack = []
    _init_classes_and_candidates(graph,classes,candidates)
    _coloring(graph,candidates,classes,colored_stack)

    #raise NotImplementedError('')

    return graph

def dsatur(graph):
    """Runs the Degree of Saturation heuristic algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _saturation(graph):
        candidates = 0
        for node in graph.node:
            if not graph.node[node]['fixed']:
                candidates+=1
                for neighbor in graph.neighbors(node):
                    if (graph.node[neighbor]['fixed']):
                        graph.node[node]['label'].add(
                            graph.node[neighbor]['label'])
        return candidates

    def _find_highest_saturation(graph):
        highest_saturation = -1
        for node in graph.node:
            if (not graph.node[node]['fixed'] and
                    type(graph.node[node]['label']) is not int):
                        if (len(graph.node[node]['label']) > highest_saturation):
                            highest_saturation = len(graph.node[node]['label'])
                            highest_node = node
        return highest_node

    def _find_smallest_color(graph,node):
        size = int(sqrt(len(graph.node)))
        for i in range(1,size+1):
            if not (i in graph.node[node]['label']):
                return i

    def _update_saturation(graph,node):
        for neighbor in graph.neighbors(node):
            if ( not graph.node[neighbor]['fixed'] and
                type(graph.node[neighbor]['label']) is not int):
                    graph.node[neighbor]['label'].add(
                        graph.node[node]['label'])

    for node in graph.node:
        if (graph.node[node]['label'] is None):
            graph.node[node]['label'] = set()
    candidates = _saturation(graph)
    while(candidates>0):
        highest_node = _find_highest_saturation(graph)
        color = _find_smallest_color(graph,highest_node)
        if(color != None):
            graph.node[highest_node]['label'] = color
            _update_saturation(graph,highest_node)
            candidates-=1
        else:
            break
    return graph

def bfs_heuristic(graph,max_iterations):
    """Runs the Breadth First Search heuristic algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _clear(graph):
        for node in graph.node:
            if not graph.node[node]['fixed']:
                graph.node[node]['label'] = None

    def _is_possible_color(graph,nodes,color):
        for node in nodes:
            if graph.node[node]['label'] == color:
                return False
        return True

    def _coloring(graph,node):
        size = int(sqrt(len(graph.node)))
        colors = []
        for i in range(size):
            if _is_possible_color(graph,graph.neighbors(node),i+1):
                colors.append(i+1)
        if len(colors) > 0:
            r = random.SystemRandom()
            graph.node[node]['label'] = r.choice(colors)
            return True
        return False


    def _bfs(graph,node):
        q = Queue()
        if not graph.node[node]['fixed']:
            if not _coloring(graph,node):
                return
        q.put(node)
        while not q.empty():
            v = q.get()
            neighbors = graph.neighbors(v)
            for neighbor in neighbors:
                if graph.node[neighbor]['label'] == None:
                    if not _coloring(graph,neighbor):
                        return
                    q.put(neighbor)

    def _is_valid_solution(graph):
        for node in graph.node:
            if graph.node[node]['label'] == None:
                return False
        return True

    for i in range(max_iterations):
        r = random.SystemRandom()
        _bfs(graph,r.choice(graph.nodes()))
        if _is_valid_solution(graph):
            break
        else:
            _clear(graph)

    for i in range(9):
        for j in range(9):
            print (graph.node['{}{}'.format(i,j)]['label'],end=' ')
        print()

    return graph

def dfs_heuristic(graph,max_iterations):
    """Runs the Depth First Search heuristic algorithm to color a graph.

    Arguments:
        graph (networkx.Graph): a graph.
    """
    def _clear(graph):
        for node in graph.node:
            if not graph.node[node]['fixed']:
                graph.node[node]['label'] = None

    def _is_possible_color(graph,nodes,color):
        for node in nodes:
            if graph.node[node]['label'] == color:
                return False
        return True

    def _coloring(graph,node):
        size = int(sqrt(len(graph.node)))
        colors = []
        for i in range(size):
            if _is_possible_color(graph,graph.neighbors(node),i+1):
                colors.append(i+1)
        if len(colors) > 0:
            r = random.SystemRandom()
            graph.node[node]['label'] = r.choice(colors)
            return True
        return False


    def _dfs(graph,node):
        stack = []
        if not graph.node[node]['fixed']:
            if not _coloring(graph,node):
                return
        stack.append(node)
        while not len(stack) == 0:
            v = stack.pop()
            neighbors = graph.neighbors(v)
            for neighbor in neighbors:
                if graph.node[neighbor]['label'] == None:
                    if not _coloring(graph,neighbor):
                        return
                    stack.append(neighbor)

    def _is_valid_solution(graph):
        for node in graph.node:
            if graph.node[node]['label'] == None:
                return False
        return True

    for i in range(max_iterations):
        r = random.SystemRandom()
        _dfs(graph,r.choice(graph.nodes()))
        if _is_valid_solution(graph):
            break
        else:
            _clear(graph)

    for i in range(9):
        for j in range(9):
            print (graph.node['{}{}'.format(i,j)]['label'],end=' ')
        print()

    return graph
