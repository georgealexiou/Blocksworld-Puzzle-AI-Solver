class Block:

    """constructor for block class that initializes
         name - the name of the block
         x - x coordinate of the block
         y - y coordinate of the block
    """
    def __init__ (self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    #method that returns true if x and y coords of two blocks are equal
    def isEqual(self, block):
        if self.x == block.x and self.y == block.y:
            return True
        else:
            return False

    #method that returns a string containing the name of the block with its coordinates
    def toString(self):
        return '{}: {} {}'.format(self.name, self.x, self.y)


class State:

    """constructor for state class that initializes
         a,b,c - blocks that represent the A,B,C blocks in the blocksworld
         agent - blocks that represent the agent in the blocksworld
         immovable - list of immovable blocks
    """
    def __init__(self, a, b, c, agent, immovables):
        self.a = a
        self.b = b
        self.c = c
        self.agent = agent
        self.immovables = immovables

    #returns true if the positions of the blocks in a state are the same
    def isEqual(self, state):
        #check if coordinates of blocks are the same and return true
        if self.a.isEqual(state.a) and self.b.isEqual(state.b) and self.c.isEqual(state.c):
            return True

        #otherwise it return false
        else:
            return False

    """prints a 4x4 grid wherethe blocks are represented with the following symbols:
         - - empty block (does not contain any other blocks)
         A - the a block
         B - the b block
         C - the c block
         P - the agent block
         x - immovable block
    """
    def printGrid(self):
        grid = [['-' for i in range(4)] for i in range(4)]

        grid[3 - self.a.y][self.a.x] = self.a.name
        grid[3 - self.b.y][self.b.x] = self.b.name
        grid[3 - self.c.y][self.c.x] = self.c.name
        grid[3 - self.agent.y][self.agent.x] = self.agent.name

        if not self.immovables is None:
            for x in self.immovables:
                grid[3 - x.y][x.x] = x.name

        for y in range(0, 4):
            print ('{} {} {} {}'.format(grid[y][0], grid[y][1], grid[y][2], grid[y][3]))

        print ('')

class Node:

    """constructor for block class that initializes
         state - the states of all blocks in the blocksworld
         parent - the previous node in the tree
         previousMove - the move that was performed from the parent node to get self
    """
    def __init__(self, state, parent, previousMove):
        self.state = state

        #checks if the parent does not exist and initializes parameters as 0/None
        if parent is None:
            self.depth = 0
            self.previousMove = None
            self.parent = None

        #checks if parent exists and initializes parameters accordingly
        else:
            self.depth = parent.depth + 1
            self.previousMove = previousMove
            self.parent = parent
            print (self.previousMove)

    #method returns the heuristic cost from the current node to a given node
    def getHeuristicEstimate(self, node):
        heuristic = 0

        heuristic += node.state.a.x - self.state.a.x
        heuristic += node.state.a.y - self.state.a.y
        heuristic += node.state.b.x - self.state.a.x
        heuristic += node.state.b.y - self.state.b.y
        heuristic += node.state.c.y - self.state.c.y
        heuristic += self.depth

        return heuristic

    #method that determines all possible moves from the current node and returns an list of those moves
    def checkPossibleMoves(self):
        possibleMoves = []
        if not self.isBlocked('U'):
            newAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y + 1)

            if not self.isImmovable(newAgent):
                newState = self.makeMove(newAgent)
                possibleMoves.append(Node(newState, self, 'U'))

        if not self.isBlocked('D'):
            newAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y - 1)
            
            if not self.isImmovable(newAgent):
                newState = self.makeMove(newAgent)
                possibleMoves.append(Node(newState, self, 'D'))

        if not self.isBlocked('L'):
            newAgent = Block(self.state.agent.name, self.state.agent.x - 1, self.state.agent.y)

            if not self.isImmovable(newAgent):
                newState = self.makeMove(newAgent)
                possibleMoves.append(Node(newState, self, 'L'))

        if not self.isBlocked('R'):
            newAgent = Block(self.state.agent.name, self.state.agent.x + 1, self.state.agent.y)

            if not self.isImmovable(newAgent):
                newState = self.makeMove(newAgent)
                possibleMoves.append(Node(newState, self, 'R'))

        return possibleMoves

    #method that determines if a move can be performed and returns True if it cant and False if it can
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

    #method that checks if there is an immovable block in the position the agent is trying to move in
    def isImmovable(self, agent):
        if not self.state.immovables is None:
            for x in self.state.immovables:
                if agent.isEqual(x):
                    return True
            
        return False
        
    #method that returns a new state based on the position of the new agent from checkPossibleMoves()
    def makeMove(self, newAgent):
        if newAgent.isEqual(self.state.a):
            return State(Block('A', self.state.agent.x, self.state.agent.y),
                         Block('B', self.state.b.x, self.state.b.y),
                         Block('C', self.state.c.x, self.state.c.y),
                         newAgent, self.state.immovables)

        elif newAgent.isEqual(self.state.b):
            return State(Block('A', self.state.a.x, self.state.a.y),
                         Block('B', self.state.agent.x, self.state.agent.y),
                         Block('C', self.state.c.x, self.state.c.y),
                         newAgent,self.state.immovables)

        elif newAgent.isEqual(self.state.c):
            return State(Block('A', self.state.a.x, self.state.a.y),
                         Block('B', self.state.b.x, self.state.b.y),
                         Block('C', self.state.agent.x, self.state.agent.y),
                         newAgent, self.state.immovables)

        else:
            return State(Block('A', self.state.a.x, self.state.a.y),
                         Block('B', self.state.b.x, self.state.b.y),
                         Block('C', self.state.c.x, self.state.c.y),
                         newAgent, self.state.immovables)

    #method that returns a list of characters representing the path taken to reach current node
    def getPath(self):
        path = []
        current = self
        print (self.previousMove)
        print (current.parent.previousMove)

        if current.previousMove is None:
            path.append('No moves made, already at final state')

        while not current.previousMove is None:
                path.append(current.previousMove)
                current = current.parent

        return path



'''
HELPER CODE TO TEST FUNCTIONALITY

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
