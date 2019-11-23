from foundation import Node
from foundation import State
from foundation import Block

from searchMethods import SearchMethods

#Initialize Start Node
startMovables = []
startMovables.append(Block('A', 1, 0))
startMovables.append(Block('B', 1, 1))
startMovables.append(Block('C', 1, 2))

startAgent = Block('P', 2,1)
startState = State(startMovables, startAgent, None)

startNode = Node(startState, None, None)

#Initialize Goal State
finMovables = []
finMovables.append(Block('A', 1, 0))
finMovables.append(Block('B', 2, 1))
finMovables.append(Block('C', 1, 2))

finAgent = Block('P', 1,1)

finState = State(finMovables, finAgent, None)

sm = SearchMethods(startNode, finState)
sm.DFS()