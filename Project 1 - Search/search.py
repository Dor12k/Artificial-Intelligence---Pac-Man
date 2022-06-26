# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
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
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    start = problem.getStartState()
    step  = problem.getStartState()  # update every step

    if not(problem.isGoalState(start)):

        visitedNodes = []
        visitedNodes.append(start)

        # create a stack witch every element is coordinate of state and list of moves
        tracks = util.Stack()
        track  = (start, [])
        tracks.push(track)

        while not (tracks.isEmpty()):

            node, moves = tracks.pop()
            visitedNodes.append(node)

            ways = problem.getSuccessors(node)  # options move on from current position

            for i in ways:
                stepTo = i[0]
                if not stepTo in visitedNodes:
                    step = i[0]
                    direction = i[1]
                    tracks.push((step, moves + [direction]))

            if( problem.isGoalState(step) ):
                break

    return moves + [direction]
    util.raiseNotDefined()



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    step  = problem.getStartState()

    if not problem.isGoalState(start):

        visitedNodes = []
        visitedNodes.append(start)

        # create a queue witch every element is coordinate of state and list of moves
        tracks = util.Queue()
        track = (start, [])
        tracks.push(track)

        while not tracks.isEmpty():

            node, moves = tracks.pop()
            ways = problem.getSuccessors(node)  # options move on from current position

            for i in ways:
                stepTo = i[0]
                if not stepTo in visitedNodes:
                    step = i[0]
                    direction = i[1]
                    visitedNodes.append(stepTo)
                    tracks.push((stepTo, moves + [direction]))

            if problem.isGoalState(node):
                 break
    return moves
    util.raiseNotDefined()



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    step  = problem.getStartState()

    if not (problem.isGoalState(start)):

        visitedNodes = []

        # create a queue witch every element is coordinate of state, list of moves and cost
        tracks = util.PriorityQueue()
        track = (start, [])
        tracks.push(track, 0)

        while not tracks.isEmpty():

            node, moves = tracks.pop()

            if problem.isGoalState(node):
                break

            ways = problem.getSuccessors(node)  # options move on from current position
            for i in ways:

                stepTo = i[0]

                if not stepTo in visitedNodes:
                    step = i[0]
                    direction = i[1]
                    cost = moves + [direction]
                    tracks.push((step, moves + [direction]),  problem.getCostOfActions(cost))

            visitedNodes.append(node)

    return moves
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    start = problem.getStartState()
    step = problem.getStartState()

    if not problem.isGoalState(start):

        visitedNodes = []

        # create a queue witch every element is coordinate of state, list of moves and heuristic
        track = (start, [])
        tracks = util.PriorityQueue()
        tracks.push(track, nullHeuristic(start, problem))

        while not tracks.isEmpty():
            node, moves = tracks.pop()

            if problem.isGoalState(node):
                break

            if node not in visitedNodes:
                ways = problem.getSuccessors(node)

                for i in ways:
                    stepTo = i[0]

                    if stepTo not in visitedNodes:
                        step = i[0]
                        direction = i[1]
                        cost = moves + [direction]
                        heur = problem.getCostOfActions(cost) + heuristic(step, problem)  # f(n) = g(n) + h(n)
                        tracks.push((step, cost), heur)

                visitedNodes.append(node)

    return moves
    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
