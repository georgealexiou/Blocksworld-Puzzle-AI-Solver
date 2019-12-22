from foundation import Node
from foundation import State
from foundation import Block

from random import shuffle
import timeit
import queue


"""
SearchMethod object containing the four search methods used in our solution,
Breadth First Search, Depth First Search, Iterative Deepening Search and A* Search.
"""
class SearchMethods:

    #constructor for searchMethods class that takes startNode and finishState
    def __init__(self, startNode, finishState):
        self.startNode = startNode
        self.finishState = finishState
        self.path = []


    #method that performs Breadth First Search to find a solution in our search tree
    def BFS(self):
        path = []

        #initialize queue and dictionary of visited nodes and add Start Node to them
        q = queue.Queue()
        q.put(self.startNode)

        visited = {self.startNode: True}

        #iterate while the queue is not empty
        while not q.empty():
            #pops first element from the queue and prints it
            currentNode = q.get()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            #check if current node is the solution
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Breadth First', currentNode, visited)
                break

            #if it is not the solution we expand its chidren nodes and add them to the queue
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        q.put(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")

    #method that performs Depth First Search to find a solution in our search tree
    def DFS(self):
        path = []
        
        #initializes stack and dictionary of visited nodes and add Start Node to them
        s = []
        s.append(self.startNode)
        
        visited = {self.startNode: True}
        
        #iterate while the stack is not empty
        while len(s) > 0:
            #pops last element from the stack and prints it
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")
            
            #check if current node is the solution
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Depth First', currentNode, visited)
                break
                 
            #if it is not the solution we expand its chidren nodes, shuffle them and add them to the stack
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                
                #shuffling nodes
                shuffle(possibleMoves)
                
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        s.append(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")
                    
                    
    #method that performs Iterative Deepening Search to find a solution in our search tree
    def iterativeDeepening(self):
        #initialize maxDepth = 0
        maxDepth = 0

        #initializes stack and dictionary of visited nodes and add Start Node to them
        s = []
        s.append(self.startNode)

        visited = {self.startNode: True}

        #iterate while the stack is not empty
        while len(s) != 0:
            #pops last element from the stack and prints it
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            #check if current node is the solution
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Iterative Deepening', currentNode, visited)
                break

            #if it is not the solution and the node depth is less than the maxDepth
            #we expand its chidren nodes, shuffle them and add them to the stack
            elif currentNode.depth < maxDepth:
                possibleMoves = currentNode.checkPossibleMoves()
                shuffle(possibleMoves)
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        s.append(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")
            
            #otherwise if stack is empty we increment maxDepth by 1
            #and add the currentNode to the stack
            if not s:
                s.append(currentNode)
                maxDepth = maxDepth + 1

    #method that performs A* Search to find a solution in our search tree
    def aStar(self):
        path = []
        
        #iitializes a priority queue and dictionary of visited nodes and add Start Node to them
        pq = PriorityQueue()
        pq.put(0, self.startNode)
        
        visited = {self.startNode: True}
        
        #iterate while the priority queue is not empty
        while not pq.isEmpty():
            currentNode = pq.pop()

            print("Visiting:")
            currentNode.state.printGrid()
            print("")
        
            #check if current node is the solution
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('A*', currentNode, visited)
                break
            
            #if it is not the solution we expand its chidren nodes and add them to the priority queue
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        print("")

                        pq.put(nextNode.getHeuristicEstimate(Node(self.finishState, None, None)), nextNode)
                        visited[nextNode] = True

                        print('cost: {}'.format(nextNode.getHeuristicEstimate(Node(self.finishState, None, None))))
                        nextNode.state.printGrid()


    #method that prints the results of the search when a search is complete
    def printResults(self, searchType, currentNode, visited):
        print ('{} Search Complete'.format(searchType))
        
        print ('Start State:')
        self.startNode.state.printGrid()
        print ('\nFinal State:')
        currentNode.state.printGrid()

        if not currentNode.parent is None:
            print ('\nDepth: {}\nHeuristic Estimate: {}\nMoves Performed: {}\nAmount visited: {}'.format(currentNode.depth, self.startNode.getHeuristicEstimate(currentNode), currentNode.getPath(), len(visited)))

"""
The PriorityQueue object is a custom priority queue used for storing and returning
expanded nodes in the correct order when running A* Search
"""
class PriorityQueue():

    #constructor that takes no arguments and initializes an empty list
    def __init__(self):
        self.pq = []

    #method that adds element to the list in the form of a tuple (priority, item)
    def put(self, priority, item):
        self.pq.append((priority, item))

    #method that returns the element with the lowest priority
    def pop(self):
        min = self.pq[0][0]
        elemPos = 0
        for i in range(len(self.pq)):
            if min > self.pq[i][0]:
                min = self.pq[i][0]
                elemPos = i

        elem = self.pq[elemPos]
        self.pq.pop(elemPos)
        return elem[1]

    #method that returns true if the list is empty
    def isEmpty(self):
        return len(self.pq) == 0

