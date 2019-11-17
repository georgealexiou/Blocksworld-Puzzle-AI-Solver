from foundation import Node
from foundation import State
from foundation import Block

import timeit
import queue

class SearchMethods:

	def __init__(self, startNode, finishState):
		self.startNode = startNode
		self.finishState = finishState
		self.path = []


	def BFS(self):
		path = []
		startTime = timeit.timeit()

		#initialize queue and dictionary and add Start Node to it
		q = queue.Queue()
		q.put(self.startNode)

		visited = {self.startNode: True}

		while not q.empty():
			#pops first element from the queue and checks what moves can be made
			currentNode = q.get()
			currentNode.state.printGrid()
			possibleMoves = currentNode.checkPossibleMoves()

			if(currentNode.state.isEqual(self.finishState)):
				time = timeit.timeit() - startTime
				self.printResults('Breadth First', currentNode, visited, time)
				quit();

			else:
				for nextNode in possibleMoves:
					if possibleMoves != None:
						q.put(nextNode)
						visited[nextNode] = True

	def DFS(self):
		return 0

	def iterativeDeepening(self):
		return 0

	def aStar(self):
		return 0

	def printResults(self, searchType, currentNode, visited, time):
		print ('{} Search Complete'.format(searchType))
		
		print ('Start State:')
		self.startNode.state.printGrid()
		print ('\nFinal State:')
		currentNode.state.printGrid()

		print ('\nDepth: {}\nHeuristic Estimate: {}\nMoves Performed: {}\nAmount visited: {}\nTime Taken: {}'.format(currentNode.depth, self.startNode.getHeuristicEstimate(currentNode), currentNode.getPath(), len(visited), time))

a = Block('A', 0, 0)
b = Block('B', 1, 0)
c = Block('C', 2, 0)
agent = Block('P', 3, 0)

immovables = []
immovables.append(Block('X', 3, 3))
immovables.append(Block('X', 3, 2))
immovables.append(Block('X', 3, 1))

state = State(a, b, c, agent, None)
node = Node(state, None, None)

node.state.printGrid()
list = node.checkPossibleMoves()

for e in list:
    e.state.printGrid()

"""
agent1 = Block('P', 3, 3)
a1 = Block('A', 1, 0)
b1 = Block('B', 2, 0)
c1 = Block('C', 3, 0)

sm = SearchMethods(node, State(a1, b1, c1, agent1))
sm.BFS()
"""
