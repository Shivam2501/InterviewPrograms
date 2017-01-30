
# coding: utf-8

# In[38]:

import numpy as np


# In[39]:

class Graph:  
    def __init__(self, V):
        self.vertices = V #number of vertices
        self.adjacent = {} #adjacency list
        self.nodes = set()
        
    def addNode(self, parentNode, childNode):
        self.adjacent.setdefault(int(parentNode),list()).append(int(childNode))
        self.adjacent[int(parentNode)] = list(set(self.adjacent[int(parentNode)]))
        self.nodes.add(int(parentNode))
        self.nodes.add(int(childNode))


# In[40]:

#input n=n[0] and m=n[1]
count = input() 
n = count.split()

#create a graph object of n vertices
g = Graph(int(n[0]))

#read all the edges and add it to the graph
for edge in range(int(n[1])):
    nodes = input()
    vertices = nodes.split()
    g.addNode(vertices[0], vertices[1])


# In[41]:

for i in range(1,g.vertices+1):
    if i not in g.adjacent:
        g.adjacent.setdefault(i,list())
    if i not in g.nodes:
        g.nodes.add(i)


# In[42]:

def dfs(vertex, visited, result, duplicate, flag):
    visited[vertex] = True
    
    duplicate.append(vertex)
    for vertices in g.adjacent[vertex]:
        if vertices in duplicate:
            flag[0] = 0
        if not visited[vertices]:
            dfs(vertices, visited, result, duplicate, flag)
    
    result.append(vertex)


# In[43]:

result = []

#mark all the vertices as unvisited
visited = {}
for i in g.nodes:
    visited[i] = False

g.nodes = list(g.nodes)
g.nodes.sort()

flag = [1]
for i in reversed(g.nodes):
    if not visited[i]:
        duplicate = []
        dfs(i, visited, result, duplicate, flag)
  
result = list(reversed(result)) 
if flag[0]:
    print(result)
else:
    print("Sandro fails.")

