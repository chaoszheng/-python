import heapq
import math

graph={
	"A":{"B":5,"C":1},
	"B":{"A":5,"C":2,"D":1},
	"C":{"A":1,"B":2,"D":4,"E":8},
	"D":{"B":1,"C":4,"E":3,"F":6},
	"E":{"C":8,"D":3},
	"F":{"D":6}
}

def init_distance(graph):
	for item in graph:
		distance[item]=math.inf
	return distance

def BFS(graph,s):
	pqueue=[]
	heapq.heappush(pqueue,(0,s))
	seen=set()
	seen.add(s)
	parent={s:None}
	distance=init_distance(graph)
	distance[s]=0

	while pqueue:
		pair=heapq.pushpop(pqueue)
		dist=pair[0]
		vertex=pair[1]
		seen.add(vertex)
		nodes=graph[vertex].keys()
		
		for item in nodes:
			if item not in seen:
				heapq.heappush(pqueue,())
				seen.add(item)
				parent[item]=vertex
		print(vertex)
	return parent

def DFS(graph,s):
	stack=[]
	stack.append(s)
	seen=set()
	seen.add(s)
	while stack:
		vertex=stack.pop()
		nodes=graph[vertex]
		for item in nodes:
			if item not in seen:
				stack.append(item)
				seen.add(item)
		print(vertex)

parent=BFS(graph,"A")
print(parent)

# DFS(graph,"A")