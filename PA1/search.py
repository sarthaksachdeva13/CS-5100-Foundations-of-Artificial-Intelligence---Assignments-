# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #First, we start with an empty stack as a fringe. We use the stack data structure from util.py
    fringeDFS =  util.Stack()
    algovar = "DFS"
    startingstate = problem.getStartState()#Initialising the starting state for pacman
    emptylist1=[] #declaring list1
    emptylist2 = [] #declaring list2
    pushv = (startingstate, emptylist1, emptylist2)
    print algovar
    fringeDFS.push(pushv) #Push the starting state into the fringe
    while not fringeDFS.isEmpty(): #While the stack is not empty, execute the following commands
        vertex , action , explored = fringeDFS.pop() #pop the vertex from the fringe after it has been explored
        goal = problem.isGoalState(vertex) #let the goal state be the variable 'goal'
        #We use the predefined isGoalState method for the problem
        if goal: #if goal is true, i.e. if the current vertex is a goal state
            print "Actions are :"
            return action #return action
        """Now initialising a 'successor' variable to generate successors of the vertex in consideration"""
        successor = problem.getSuccessors(vertex) #declared

        namevar = "Sarthak Sachdeva AI Spring 2017"

        """for each child of the vertex, it's direction of movement and the steps taken"""
        for children, directionofmovement, allsteps in successor:
            if not children in explored: #if the child is not in explored
                actdir = action +[directionofmovement] #this is the action plus the direction of pacman's movement
                expver = explored + [vertex] #updating the explored set by adding a vertex to it
                pushvar = (children, actdir, expver) #creating a variable 'pushvar' with the child and the above \n
                                                    #two variables
                fringeDFS.push(pushvar) #pushing this to the fringe

    return emptylist1 #returning the list
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #First, we start with an empty queue as a fringe. We use the queue data structure from util.py
    fringeBFS = util.Queue()
    algovar = "BFS"
    startingstate = problem.getStartState()#Initialising starting state for pacman
    emptylist = [] #declaring an emptylist
    exploredset = []  #making an empty list to push into the queue
    print algovar
    pushv = (startingstate, emptylist) #creating a push variable to push into the queue
    fringeBFS.push(pushv) #pushing starting state and the empty list into the fringe queue
    while not fringeBFS.isEmpty(): #while the queue is not empty, execute the following commands
        vertex, actions = fringeBFS.pop()#pop the vertex from the fringe
        goal = problem.isGoalState(vertex) #let the goal state be the variable 'goal'
        while not vertex in exploredset: #while the current vertex is not in the explored set
            """append the vertex to the explored set"""
            exploredset.append(vertex)
            if goal: #if goal is true, i.e. if the current vertex is a goal state
                print "Actions are :"
                return actions #return actions
            """Now initialising a 'successor' variable to generate successors of the vertex in consideration"""
            successor = problem.getSuccessors(vertex)
            namevar = "Sarthak Sachdeva AI Spring 2017"
            """for each child of the vertex, it's direction of movement and the steps taken"""
            for child, directionofmovement, allsteps in successor:
                actdir = actions +[directionofmovement]  #this is the action plus the direction of pacman's movement
                pushvar = (child, actdir) #creating a variable 'pushvar' with the child and the above variable
                fringeBFS.push(pushvar) #pushing this to the fringe

    return emptylist #returning the list

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    """First, we start with a priority queue as a fringe. We use the priority queue data structure from util.py"""
    algovar = "UCS"
    fringeUCS = util.PriorityQueue()
    startingstate = problem.getStartState() # Initialising starting state for pacman
    emptylist = [] #declaring an emptylist
    exploredset = [] #making an empty list to push into the queue
    zerovar = 0 #creating a variable 0 for the path cost
    print algovar
    pushv1 = (startingstate, emptylist) #creating a push variable to push into the queue
    fringeUCS.push(pushv1, zerovar) #pushing starting state and the empty list into the fringe priority queue
    while not fringeUCS.isEmpty(): #while the queue is not empty, execute the following commands
        vertex, actions = fringeUCS.pop() #pop the vertex from the fringe
        goal = problem.isGoalState(vertex) #let the goal state be the variable 'goal'
        while not vertex in exploredset: #while the current vertex is not in the explored set
            """append the vertex to the explored set"""
            exploredset.append(vertex)
            if goal: #if goal is true, i.e. if the current vertex is a goal state
                print "Actions are :"
                return actions
            successor = problem.getSuccessors(vertex)
            namevar = "Sarthak Sachdeva AI Spring 2017"
            """for each child of the vertex, it's direction of movement and the steps taken"""
            for child, directionofmovement, allsteps in successor:
                actdir = actions + [directionofmovement] #this is the action plus the direction of pacman's movement
                costactdir = problem.getCostOfActions(actdir) #Using the getCostOfActions function
                """So in the above costactdir variable, the getcostofactions calculates the cost of the actions
                taken to reach the goal state"""
                pushvar = (child, actdir) #creating a pushvar variable with the child and the actdir
                fringeUCS.push(pushvar, costactdir) #pushing the pushvar and the costactdir values into the fringe

    return emptylist #returning the list

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """First, we start with a priority queue as a fringe. We use the priority queue data structure from util.py"""
    fringeastar = util.PriorityQueue()
    algovar = "A*"
    startingstate = problem.getStartState() # Initialising starting state for pacman
    exploredset = [] #making an empty list to push into the queue
    emptylist = [] #declaring an empty list variable
    print algovar
    pushv1 = (startingstate, emptylist) #creating a variable pushv1 that contains the starting state and the emptylist
    """The following variable is for the heuristics of the problem"""
    heurstartstatevar = heuristic(startingstate, problem)
    fringeastar.push(pushv1,heurstartstatevar) #pushing the starting state and the heuristic values into the fringe
    while not fringeastar.isEmpty(): #while the queue is not empty, execute the following commands
        vertex, actions = fringeastar.pop() #pop the vertex from the fringe
        while vertex not in exploredset: #while the current vertex is not in the explored set
            """append the vertex to the explored set"""
            exploredset.append(vertex)
            goal = problem.isGoalState(vertex) #let the goal state be the variable 'goal'
            if goal:#if goal is true, i.e. if the current vertex is a goal state
                print "Actions are :"
                return actions
            """Now initialising a 'successor' variable to generate successors of the vertex in consideration"""
            successor = problem.getSuccessors(vertex)
            namevar = "Sarthak Sachdeva AI Spring 2017"
            """for each child of the vertex, it's direction of movement and the cost"""
            for child, directionofmovement, cost in successor:
                actdir = actions + [directionofmovement] #this is the action plus the direction of pacman's movement
                """We now calculate the total cost of the action and the direction"""
                getcost = problem.getCostOfActions(actdir)
                """Calculating heuristics of the child node"""
                heurchild = heuristic(child, problem)
                answer = getcost + heurchild #maintaining a score by adding cost and the heuristics
                """The above is basically f(n)= g(n) + h(n)"""
                pushvar = (child,actdir) #creating a push variable with child and the actdir variable
                fringeastar.push(pushvar, answer) #pushing the pushvar and the score into the queue

    return emptylist  #returning the list


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
