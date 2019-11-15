class Block:

	def __init__ (self, name, x, y):
		self.name = name
		self.x = x
		self.y = y

	def isEqual(self, block):
		return self == block

	def toString(self):
		return self.name + ': x:' + self.x + ', y:' + self.y

class State:

	def __init__(self, a, b, c, agent):
		self.a = a
		self.b = b
		self.c = c
		self.agent = agent

	def getPositions:
		return [self.x, self.y]


class Node:

	def __init__(self, state, parent, previousMove):
		self.state = state

		if parent != None:
			self.depth = 0
			self.pathCost = 0
			self.previousMove = None
			self.parent = None

		elif: 
			self.depth = parent.depth + 1
			self.pathCost = parent.pathCost + 1
			self.previousMove = previousMove
			self.parent = parent

	def checkPossibleMoves(self):
		possibleMoves = []
		if (!isBlocked('U')):
			newAgent = Block(state.agent.name, state.agent.x, state.agent.y + 1)
			newState = makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'U'))

		if(!isBlocked('D')):
			newAgent = Block(state.agent.name, state.agent.x, state.agent.y - 1)
			newState = makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'D'))

		if(!isBlocked('L')):
			newAgent = Block(state.agent.name, state.agent.x - 1, state.agent.y)
			newState = makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'L'))

		if(!isBlocked('R')):
			newAgent = Block(state.agent.name, state.agent.x + 1, state.agent.y)
			newState = makeMove(newAgent)
			possibleMoves.append(Node(newState, self, 'R'))

		return possibleMoves

	def isBlocked(self, move):
		if move == 'U' && agent.y == 3:
			return False
		elif move == 'D' && agent.y == 0:
			return False
		elif move == 'R' && agent.x == 3:
			return False
		elif move == L && agent.x == 0:
			return False
		else
			return True

	def makeMove(self, newAgent):
		if newAgent.getPositions() == a.getPositions():
			return State(Block('A', state.agent.x, state.agent.y), 
						 Block('B', state.b.x, state.b.y),
						 Block('C', state.c.x, state.c.y),
						 newAgent)

		elif newAgent.getPositions() == b.getPositions():
			return State(Block('A', state.a.x, state.a.y), 
						 Block('B', state.agent.x, state.agent.y),
						 Block('C', state.c.x, state.c.y),
						 newAgent)

		elif newAgent.getPositions() == c.getPositions():
			return State(Block('A', state.a.x, state.a.y), 
						 Block('B', state.b.x, state.b.y),
						 Block('C', state.agent.x, state.agent.y),
						 newAgent)

		else:
			return State(Block('A', state.a.x, state.a.y), 
						 Block('B', state.b.x, state.b.y),
						 Block('C', state.c.x, state.c.y),
						 newAgent)
