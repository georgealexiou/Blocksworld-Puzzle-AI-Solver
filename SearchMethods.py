from FoundationClasses import Node
from FoundationClasses import State
from FoundationClasses import Block

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

		#initialize queue and add Start Node to it
		q = queue.Queue()
		q.put(self.startNode)

		while not q.empty():
			#pops first element from the queue and checks what moves can be made
			currentNode = q.get()
			possibleMoves = currentNode.checkPossibleMoves()

			if(currentNode.state.isEqual(self.finishState)):
				print 'I am equal'
				time = timeit.timeit() - startTime
				self.printResults('Breadth First', currentNode, time)
				quit();

			else:
				for nextNode in possibleMoves:
					if possibleMoves != None:
						q.put(nextNode)

	def DFS(self):
		return 0

	def iterativeDeepening(self):
		return 0

	def aStar(self):
		return 0

	def printResults(self, searchType, currentNode, time):
		print '{} Search Complete'.format(searchType)
		
		print 'Start State:'
		self.startNode.state.printGrid()
		print '\nFinal State:'
		currentNode.state.printGrid()

		#print"\nDepth: {}\nPath Cost: {}\nMoves Performed: {}\nTime Taken: {}".format(currentNode.depth, currentNode.pathCost, currentNode.getPath(), time)

a = Block('A', 0, 0)
b = Block('B', 1, 0)
c = Block('C', 2, 0)
agent = Block('P', 3, 0)
state = State(a, b, c, agent)
node = Node(state, None, None)

agent1 = Block('P', 2, 0)
a1 = Block('A', 0, 0)
b1 = Block('B', 1, 0)
c1 = Block('C', 3, 0)

sm = SearchMethods(node, State(a1, b1, c1, agent1))
sm.BFS()
