import numpy as numpy

class Block:

	def __init__ (self, name, x, y):
		self.name = name
		self.x = x
		self.y = y

	def isEqual(self, block):
		return self.x == block.x and self.y == block.y

	def toString(self):
		return self.name + ': x:' + self.x + ', y:' + self.y


class State:

	def __init__(self, a, b, c, agent):
		self.a = a
		self.b = b
		self.c = c
		self.agent = agent

	def getPositions(self):
		return [self.x, self.y]

	def isEqual(self, state):
		#checks if the positions of the blocks are the same and returns true
		if self.a.isEqual(state.a) and self.b.isEqual(state.b) and self.c.isEqual(state.c):
			print 'a: {} {}, {} {}'.format(state.a.x, state.a.y, self.a.x, self.a.y)
			print 'b: {} {}, {} {}'.format(state.b.x, state.b.y, self.a.x, self.b.y)
			print 'c: {} {}, {} {}'.format(state.c.x, state.c.y, self.a.x, self.c.y)
		   	return True

		#otherwise it returns false
		else:
			return False

	def printGrid(self):
		grid = [['x' for i in range(4)] for i in range(4)]

		grid[3 - self.a.y][self.a.x] = self.a.name
		grid[3 - self.b.y][self.b.x] = self.b.name
		grid[3 - self.c.y][self.c.x] = self.c.name
		grid[3 - self.agent.y][self.agent.x] = self.agent.name

		for y in range(0, 4):
			print '{} {} {} {}'.format(grid[y][0], grid[y][1], grid[y][2], grid[y][3])

		print ''

class Node:

	def __init__(self, state, parent, previousMove):
		self.state = state

		if parent == None:
			self.depth = 0
			self.pathCost = 0
			self.previousMove = None
			self.parent = None
		else: 
			self.depth = parent.depth + 1
			self.pathCost = parent.pathCost + 1
			self.previousMove = previousMove
			self.parent = parent

	def getHeuristicEstimate(self, node):
		heuristic = 0

		heuristic += node.state.a.x - self.state.a.x
		heuristic += node.state.a.y - self.state.a.y
		heuristic += node.state.b.x - self.state.a.x
		heuristic += node.state.b.y - self.state.b.y
		heuristic += node.state.c.y - self.state.c.y
		heuristic += self.depth

		return heuristic

	def checkPossibleMoves(self):
		possibleMoves = []
		if not self.isBlocked('U'):
			newAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y + 1)
			newState = self.makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'U'))

		if not self.isBlocked('D'):
			newAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y - 1)
			newState = self.makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'D'))

		if not self.isBlocked('L'):
			newAgent = Block(self.state.agent.name, self.state.agent.x - 1, self.state.agent.y)
			newState = self.makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'L'))

		if not self.isBlocked('R'):
			newAgent = Block(self.state.agent.name, self.state.agent.x + 1, self.state.agent.y)
			newState = self.makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'R'))

		return possibleMoves

	def isBlocked(self, move):
		if move == 'U' and self.state.agent.y == 3:
			return True
		elif move == 'D' and self.state.agent.y == 0:
			return True
		elif move == 'R' and self.state.agent.x == 3:
			return True
		elif move == 'L' and self.state.agent.x == 0:
			return True
		else:
			return False

	def makeMove(self, newAgent):
		if newAgent.isEqual(self.state.a):
			return State(Block('A', self.state.agent.x, self.state.agent.y), 
						 Block('B', self.state.b.x, self.state.b.y),
						 Block('C', self.state.c.x, self.state.c.y),
						 newAgent)

		elif newAgent.isEqual(self.state.b):
			return State(Block('A', self.state.a.x, self.state.a.y), 
						 Block('B', self.state.agent.x, self.state.agent.y),
						 Block('C', self.state.c.x, self.state.c.y),
						 newAgent)

		elif newAgent.isEqual(self.state.c):
			return State(Block('A', self.state.a.x, self.state.a.y), 
						 Block('B', self.state.b.x, self.state.b.y),
						 Block('C', self.state.agent.x, self.state.agent.y),
						 newAgent)

		else:
			return State(Block('A', self.state.a.x, self.state.a.y), 
						 Block('B', self.state.b.x, self.state.b.y),
						 Block('C', self.state.c.x, self.state.c.y),
						 newAgent)

	def getPath(self):
		path = []
		current = self
		while current.parent != None:
			path.append(current.previousMove)

		if(current.parent == None):
			path.append('No moves made, already at final state')

		return path

'''
a = Block('A', 0, 0)
b = Block('B', 1, 0)
c = Block('C', 2, 0)
agent = Block('P', 3, 0)
state = State(a, b, c, agent)
node = Node(state, None, None)

print 'Start Node:'
node.state.printGrid()

print '\nCheck Moves'
moves = node.checkPossibleMoves()
for move in moves:
	print move.previousMove
	move.state.printGrid()
'''
