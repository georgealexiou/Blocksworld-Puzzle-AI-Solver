from foundation import Node
from foundation import State
from foundation import Block

from random import shuffle
import timeit
import queue


class SearchMethods:

    def __init__(self, startNode, finishState):
        self.startNode = startNode
        self.finishState = finishState
        self.path = []


    def BFS(self):
        path = []

        #initialize queue and dictionary and add Start Node to it
        q = queue.Queue()
        q.put(self.startNode)

        visited = {self.startNode: True}

        while not q.empty():
            #pops first element from the queue and checks what moves can be made
            currentNode = q.get()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Breadth First', currentNode, visited)
                break

            else:
                possibleMoves = currentNode.checkPossibleMoves()
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        q.put(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")

    def DFS(self):
        path = []
        
        #initializes stack and dictionary and add Start Node to it
        s = []
        s.append(self.startNode)
        
        visited = {self.startNode: True}
        
        while len(s) > 0:
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")
            
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Depth First', currentNode, visited)
                break
                
            else:
                possibleMoves = currentNode.checkPossibleMoves()
                shuffle(possibleMoves)
                print("Expanding...")
                for nextNode in possibleMoves:
                    if not possibleMoves is None:
                        s.append(nextNode)
                        visited[nextNode] = True
                        nextNode.state.printGrid()
                        print("")
                        

    def iterativeDeepening(self):
        maxDepth = 0

        #initializes stack and dictionary and add Start Node to it
        s = []
        s.append(self.startNode)

        visited = {self.startNode: True}

        while len(s) != 0:
            currentNode = s.pop()
            print("Visiting:")
            currentNode.state.printGrid()
            print("")

            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('Iterative Deepening', currentNode, visited)
                break

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

            if not s:
                s.append(self.startNode)
                maxDepth = maxDepth + 1



    def aStar(self):
        path = []
        
        #iitializes a priority queue and dictionary and add Start Node to it
        pq = PriorityQueue()
        pq.put(0, self.startNode)
        visited = {self.startNode: True}
        
        while not pq.isEmpty():
            currentNode = pq.pop()

            print("Visiting:")
            currentNode.state.printGrid()
            print("")
        
        
            if(currentNode.state.isEqual(self.finishState)):
                self.printResults('A*', currentNode, visited)
                break
                
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


    def printResults(self, searchType, currentNode, visited):
        print ('{} Search Complete'.format(searchType))
        
        print ('Start State:')
        self.startNode.state.printGrid()
        print ('\nFinal State:')
        currentNode.state.printGrid()

        if not currentNode.parent is None:
            print ('\nDepth: {}\nHeuristic Estimate: {}\nMoves Performed: {}\nAmount visited: {}'.format(currentNode.depth, self.startNode.getHeuristicEstimate(currentNode), currentNode.getPath(), len(visited)))

class PriorityQueue():

    def __init__(self):
        self.pq = []

    def put(self, priority, item):
        self.pq.append((priority, item))

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

    def isEmpty(self):
        return len(self.pq) == 0