graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}


def iteractive_dfs(graph, start, path=None):
    """iterative depth first search from start"""
    if path is None:
        path = []
    q = [start]
    while q:
        v = q.pop()
        if v not in path:
            path = path + [v]
            q += graph[v]
    return path

print(iteractive_dfs(graph, 'A'))



graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # (vertex, path)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F')))

'''
†***********************
4 Bread-Firsth Search — Поиск вширину
***********************


'''

graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
from queue import deque


def bfs(graph, start):
    visited, queue = [], deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.append(vertex)
            queue.extendleft(set(graph[vertex]) - set(visited))
    return visited

print(bfs(graph, 'A'),'start')
['A', 'B', 'C', 'D', 'E', 'F']



'''
5 BFS Paths

'''

from queue import deque
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E'],
         'D': ['G'],
         'G': ['D']}


def bfs_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.appendleft((next, path+[next]))

# print(list(bfs_paths(graph, 'A', 'F')))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

print(shortest_path(graph, 'A', 'G'))
#print(shortest_path(graph, 'E', 'D'))
#print(shortest_path(graph, 'A', 'D'))
#print(shortest_path(graph, 'F', 'D'))