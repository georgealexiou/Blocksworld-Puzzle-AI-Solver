from foundation import Node
from foundation import State
from foundation import Block

from searchMethods import SearchMethods

#Initialize Start Node
startMovables = []
startMovables.append(Block('A', 1, 2))
startMovables.append(Block('B', 1, 1))
startMovables.append(Block('C', 1, 0))

startAgent = Block('P', 2,1)
startState = State(startMovables, startAgent, None)

startNode = Node(startState, None, None)

#Initialize Goal State
finMovables = []
finMovables.append(Block('A', 1, 2))
finMovables.append(Block('B', 2, 1))
finMovables.append(Block('C', 1, 0))

finAgent = Block('P', 3,0)

finState = State(finMovables, finAgent, None)
sm = SearchMethods(startNode, finState)

print ('Select Search Method:\n1. DFS\n2. BFS\n3. Iterative Deepening\n4. A*')
inp = int(input())

if inp == 1:
	print('DEPTH FIRST SEARCH')
	sm.DFS()
if inp == 2:
	print('BREADTH FIRST SEARCH')
	sm.BFS()
if inp == 3:
	print('ITERATIVE DEEPENING SEARCH')
	sm.iterativeDeepening()
if inp == 4:
	print('A* SEARCH')
	sm.aStar()
