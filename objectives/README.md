## Note on Graph Traversals

* Sometimes, it doesn't matter whether you do a depth-first or breadth-first search
* Breadth-first Search is very useful for finding the shortest path from a source to a dstination

## DFS Recursive

* There are two steps needed to implement a recursive solution:
    * Base-case - when to return from your funciton
    * REcursive case - when to recurse

* Base-cases
    * When node is found, return the path you took
    * When no node is found return an empty path
* Recursive-case:
    * When you find a node that is not yet visited