#import high performance data collections
from collections import deque
from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    #node
    stack.append((starting_node, 0))  
    visited = set()
    earliestAncestor = (starting_node, 0)

    while len(stack) > 0:
        current = stack.pop()
        currentNode, distance = current[0], current[1]
        visited.add(current)

        if currentNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = current
            elif distance == earliestAncestor[1] and currentNode < earliestAncestor[0]:
                earliestAncestor = current
        else:
            for ancestor in graph[currentNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def createGraph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 5))
