
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
    def __init__(self, movables, agent, immovables):
        self.agent = agent
        self.immovables = immovables
        self.movables = movables
        self.gridLength = len(self.movables) + 1

    #method that returns true if the positions of the blocks in a state are the same
    def isEqual(self, state):
        #assume that the coordinates are the same and check if they are not
        result = True
        for i in range(0, len(self.movables)):
            if not self.movables[i].isEqual(state.movables[i]):
                result = False

        return result
    
    #method that returns True if a given move cannot be performed
    def isBlocked(self, move):
        if move == 'U' and self.agent.y == 3:
            return True
        elif move == 'D' and self.agent.y == 0:
            return True
        elif move == 'R' and self.agent.x == 3:
            return True
        elif move == 'L' and self.agent.x == 0:
            return True
        else:
            return False

    #method that checks if there is an immovable block in the position the agent is trying to move in
    def isImmovable(self, x, y):
        if not self.immovables is None:
            for imm in self.immovables:
                if imm.x == x and imm.y == y:
                    return True
            
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
        #generate empty grid
        grid = [['-' for i in range(0, self.gridLength)] for i in range(0, self.gridLength)]

        #add movable blocks to the grid
        for m in self.movables:
            grid[self.gridLength - 1 - m.y][m.x] = m.name

        #add agent to the grid
        grid[self.gridLength - 1 - self.agent.y][self.agent.x] = self.agent.name

        #checks if there are immovable blocks and adds them to the grid if they exist
        if not self.immovables is None:
            for immovable in self.immovables:
                grid[self.gridLength - immovable.y][immovable.x] = immovable.name

        #prints grid
        xline = ''
        for y in range(0, self.gridLength):
            for x in range(0, self.gridLength):
                xline = '{} {}'.format(xline, grid[y][x])

            print (xline)
            xline = ''

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

    #method returns the heuristic cost from the current node to a given node
    def getHeuristicEstimate(self, node):
        heuristic = 0

        #calculte Manhattan distance for each node
        for i in range(0, self.state.gridLength - 1):
            heuristic += abs(self.state.movables[i].x - node.state.movables[i].x) + abs(self.state.movables[i].y - node.state.movables[i].y)
        
        if not self.parent is None:
            heuristic = heuristic + self.parent.getHeuristicEstimate(node)
            
        return heuristic

    """
    Method that determines all possible moves from the current node and returns an list of those moves
    The order the moves are checked in and added to the list are:
        1. UP
        2. DOWN
        3. LEFT
        4. RIGHT
    """
    def checkPossibleMoves(self):
        possibleMoves = []

        #create new Node for the move 'UP'
        if not self.state.isBlocked('U'):
        
            #check if there is an immovable object in the position the agent is trying to move in
            if not self.state.isImmovable(self.state.agent.x, self.state.agent.y + 1):
                didSwap = False
                
                #creates new agent and movables array
                uAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y + 1)
                uMovables = []
                
                for m in self.state.movables:
                    uMovables.append(Block(m.name, m.x, m.y))

                #ckecks if a movable block is swapped with the agent
                for i in range(0, len(uMovables)):
                    if uMovables[i].isEqual(uAgent):
                        uMovables[i] = Block(uMovables[i].name, self.state.agent.x, self.state.agent.y)
                        possibleMoves.append(Node(State(uMovables, uAgent, self.state.immovables), self, 'U'))
                        didSwap = True

                if not didSwap:
                    possibleMoves.append(Node(State(uMovables, uAgent, self.state.immovables), self, 'U'))


        if not self.state.isBlocked('D'):
        
            #check if there is an immovable object in the position the agent is trying to move in
            if not self.state.isImmovable(self.state.agent.x, self.state.agent.y - 1):
                didSwap = False
                
                #creates new agent and movables array
                dAgent = Block(self.state.agent.name, self.state.agent.x, self.state.agent.y - 1)
                dMovables = []
                
                for m in self.state.movables:
                    dMovables.append(Block(m.name, m.x, m.y))
        
                #ckecks if a movable block is swapped with the agent
                for i in range(0, len(dMovables)):
                    if dMovables[i].isEqual(dAgent):
                        dMovables[i] = Block(dMovables[i].name, self.state.agent.x, self.state.agent.y)
                        possibleMoves.append(Node(State(dMovables, dAgent, self.state.immovables), self, 'D'))
                        didSwap = True

                if not didSwap:
                    possibleMoves.append(Node(State(dMovables, dAgent, self.state.immovables), self, 'D'))

        if not self.state.isBlocked('L'):

            #check if there is an immovable object in the position the agent is trying to move in
            if not self.state.isImmovable(self.state.agent.x - 1, self.state.agent.y):
                didSwap = False
                
                #creates new agent and movables array
                lAgent = Block(self.state.agent.name, self.state.agent.x - 1, self.state.agent.y)
                lMovables = []
                
                for m in self.state.movables:
                    lMovables.append(Block(m.name, m.x, m.y))
                    
                #ckecks if a movable block is swapped with the agent
                for i in range(0, len(lMovables)):
                    if lMovables[i].isEqual(lAgent):
                        lMovables[i] = Block(lMovables[i].name, self.state.agent.x, self.state.agent.y)
                        possibleMoves.append(Node(State(lMovables, lAgent, self.state.immovables), self, 'L'))
                        didSwap = True

                if not didSwap:
                    possibleMoves.append(Node(State(lMovables, lAgent, self.state.immovables), self, 'L'))

        if not self.state.isBlocked('R'):
        
            #check if there is an immovable object in the position the agent is trying to move in
            if not self.state.isImmovable(self.state.agent.x + 1, self.state.agent.y):
                didSwap = False
                
                #creates new agent and movables array
                rAgent = Block(self.state.agent.name, self.state.agent.x + 1, self.state.agent.y)
                rMovables = []
                
                for m in self.state.movables:
                    rMovables.append(Block(m.name, m.x, m.y))

                #ckecks if a movable block is swapped with the agent
                for i in range(0, len(rMovables)):
                    if rMovables[i].isEqual(rAgent):
                        rMovables[i] = Block(rMovables[i].name, self.state.agent.x, self.state.agent.y)
                        possibleMoves.append(Node(State(rMovables, rAgent, self.state.immovables), self, 'R'))
                        didSwap = True

                if not didSwap:
                    possibleMoves.append(Node(State(rMovables, rAgent, self.state.immovables), self, 'R'))

        return possibleMoves

    #method that returns a list of characters representing the path taken to reach current node
    def getPath(self):
        path = []
        current = self

        if current.previousMove is None:
            path.append('No moves made, already at final state')

        while not current.previousMove is None:
                path.append(current.previousMove)
                current = current.parent

        return path
