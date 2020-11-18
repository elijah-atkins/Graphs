'''
1. Translate into graph terminology
vertex - word
edges - possible one letter tranformation from a word to another word
path - one letter tranformations from beginWord to endWord

2. build your graph if needed
- creating all possivle transformations in an adjacency list would be too expensive
- we can come up with how to find out the next vertex by dertermining if it's even a valid vertex to visit

3. Traverse your graph
- since we want the shortest path, we want to use BFS
- start from beginWord and generate word tranformations based on word
- enqueue transformations that are in wordList, ignore the rest
- once we find endWord, return the path it took to get to that node

'''
alphabet = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
from collections import deque

def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i+1:]
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
    return []



wordList = ["hot","dot","dog","lot","log","cog"]

print(findLadders("hit", "cog", wordList))