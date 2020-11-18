'''
Understand

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 5))

Plan
1. Translate the problem into graph terminology
    vertex - user
    edges - parent-child relationship between two users
    weights - N/A
    path - a user's family tree

2. Build your graph (if needed)
    build graph based on edges we're given, each user has a directed edge to its ancestor/parent


3. Traverse the graph
    traverse all paths starting from starting_node, keep track of farthest node found with the lowest user id
    simply output that node

'''
#Execute
#import high performance data collections
from collections import deque
from collections import defaultdict
#Build out my graph with given edges
def createGraph(edges):
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))  
    visited = set()

    while len(stack) > 0:
        current = stack.pop() #tuple
        currentNode, distance = current[0], current[1]
        visited.add(current)

        if currentNode not in graph:
            if distance > earliestAncestor[1]: #second value of tuple is distance
                earliestAncestor = current
            elif distance == earliestAncestor[1] and currentNode < earliestAncestor[0]: #first value of tuple is Node
                earliestAncestor = current
        else:
            for ancestor in graph[currentNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1




#Review
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 5))
