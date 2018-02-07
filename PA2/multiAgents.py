# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        printvar = "Reflex agent"
        """Let the successor GameState value be assigned to the following variable"""
        successorval = successorGameState.getScore()
        zerovar = 0  # Declaring a variable with the value zero
        posvar = successorGameState.getGhostStates()[zerovar].getPosition() #using a variable to calculate the \n
                                                                            #manhattan distance
        foodlistvar = successorGameState.getFood().asList() #declaring a variable to calculate manhattan distance to \n
                                                            #the food

        print printvar + ":"

        dtog = manhattanDistance(successorGameState.getPacmanPosition(),posvar) #manhattan distance to ghost
        if dtog > zerovar: #if dtog is more than zero
            successorval = successorval - 10.0 / dtog

        # manhattan distance to ghost
        dtoF = [manhattanDistance(successorGameState.getPacmanPosition(), s) for s in foodlistvar]

        if len(dtoF):
            minvar = min(dtoF)
            successorval = successorval + 10.0 / minvar

        return successorval

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        printvar = "Minimax"
        infvar = '-inf' #declaring a variable for negative infinity
        blankvar = " "
        zerovar = 0 #variable for zero
        onevar = 1 #variable for 1
        legalact = gameState.getLegalActions(zerovar) #We assign legalactions to the gameState
        hs = float(infvar) #we translate the infinity to float in this variable. This is our high score.
        bestact = blankvar
        """For each action in legal actions"""
        print printvar + ":"
        for a in legalact:
            successgen = gameState.generateSuccessor(zerovar, a) #Generating successors to the first state /n
                                                                # with respect to action a
            nextstate = successgen #Let the next state be the variable defined above
            minval = self.MIN_VALUE(nextstate,zerovar,onevar) #We calculate the minimum
            newvalue = minval #making newvalue to be the minvalue
            if newvalue > hs: #if the minvalue is greater than our high score
                hs = newvalue #then assign the newvalue to the high score
                bestact = a #let the best action be a

        return bestact

    def MAX_VALUE(self, gameState, depth, agentIndex):
        winvar = gameState.isWin()
        losevar = gameState.isLose()
        d = self.depth
        zerovar = 0  # variable for zero
        onevar = 1  # variable for 1
        infvar = '-inf' # declaring a variable for negative infinity
        if winvar or losevar or depth == d: #if the gamestate is win or lose or the depth is equal to self.depth
            return self.evaluationFunction(gameState) #return the evaluation function of the gameState
        v = float(infvar)
        legalvar = gameState.getLegalActions(agentIndex)
        for a in legalvar: #for each action in legal actions
            nexstat = gameState.generateSuccessor(agentIndex, a)
            minvar = self.MIN_VALUE(nexstat, depth, zerovar + onevar + 0)
            v = max(v, minvar)
        return v

    def MIN_VALUE(self, gameState, depth, agentIndex):
        winvar = gameState.isWin()
        losevar = gameState.isLose()
        d = self.depth
        zerovar = 0  # variable for zero
        onevar = 1  # variable for 1
        infvar = 'inf'  # declaring a variable for infinity
        if winvar or losevar or depth == d: #if the gamestate is win or lose or the depth is equal to self.depth
            return self.evaluationFunction(gameState) #return the evaluation function of the gameState
        v = float(infvar)
        legalvar = gameState.getLegalActions(agentIndex)
        for a in legalvar: #for each action in legal actions
            nexstat = gameState.generateSuccessor(agentIndex, a)
            ifvar = gameState.getNumAgents() - onevar
            if ifvar == agentIndex: #if the number of agent minus 1 is equal to the agent's index
                maxvalvar = self.MAX_VALUE(nexstat, depth + onevar, zerovar + (1-1))
                v = min(v, maxvalvar) #let the value be the minimum of the value and the self.MAX_VALUE
            else:
                minvalvar = self.MIN_VALUE(nexstat, depth, agentIndex + onevar + 0) #else calculate self.MIN_VALUE
                v = min(v, minvalvar)
        return v

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        zerovar = 0
        onevar = 1
        neginf = '-inf'
        posinf = 'inf'
        negfloat = float(neginf)
        posfloat = float(posinf)
        d = self.depth
        colvar = ":"
        print "Alpha-Beta Pruning" + colvar
        retvariable = self.val(gameState, zerovar + 0 + zerovar, negfloat + (1 - onevar), posfloat, d - onevar)[(2-1)]
        return retvariable

    def MAX_VALUE(self, gameState, agentIndex, alpha, beta, depth):
        neginf = '-inf'
        onevar = 1
        zerovar = 0
        negfloat = float(neginf)
        bestAct = 'Stop'
        for a in gameState.getLegalActions(agentIndex): #for each action in legal moves and successor states
            succvar = gameState.generateSuccessor(agentIndex, a)
            """Let the index + 1 be assigned to a variable indexplusonevar"""
            indexplusonevar = agentIndex + onevar
            score = self.val(succvar, indexplusonevar, alpha, beta, depth) #let score be the value function
            if score[zerovar] > negfloat: #if the score[0] is greater than float(-inf)
                negfloat = score[zerovar] #let float(-inf) be score[0]
                bestAct = a #Let the best action be the action in the legal moves
                if negfloat > beta: #If float(-inf) is greater than beta
                    retvar = (negfloat, bestAct)
                    return retvar #return float(-inf) and the best action
                alphavar = negfloat, alpha
                alpha = max(alphavar) #Let alpha be the max of alpha and float(-inf)
        return (negfloat, bestAct) #return float(-inf) and the best action

    def MIN_VALUE(self, gameState, agentIndex, alpha, beta, depth):
        zerovar = 0
        onevar = 1
        posinf = 'inf'
        posfloat = float(posinf)
        bestAct = 'Stop'
        getnumvar = (gameState.getNumAgents() - onevar)
        """if the agent is the ultimate ghost and the depth is zero"""
        if agentIndex == getnumvar and depth == zerovar:
            for a in  gameState.getLegalActions(agentIndex): #for action in legal moves and successor states
                succvar = gameState.generateSuccessor(agentIndex, a)
                sc = (self.evaluationFunction(succvar), a) #Let this be the score
                if sc[zerovar] < posfloat: #if the score[0] is less than float(inf)
                    bestAct = a #Let the best action be the action in pacman's legal moves
                    posfloat= sc[zerovar] #let float(inf) be score[0]
                    if posfloat< alpha: #if the float(inf) is less than alpha
                        retvar = (posfloat, bestAct)
                        return retvar #return float(inf) and the best action
                    beta = min(beta, posfloat) #beta is the minimum of beta and float(inf)
            retpos = (posfloat, bestAct)
            return retpos
        else: #Recursion continues
            for a in gameState.getLegalActions(agentIndex): #for action in legal moves and successor states
                agentvar = agentIndex + onevar
                succvar2 = gameState.generateSuccessor(agentIndex, a) #generate successors after applying action a
                sc = self.val(succvar2, agentvar, alpha, beta, depth) #Let this be the svore
                if sc[zerovar] < posfloat: #if the score[0] is less than float(inf)
                    bestAct = a #Let the best action be the action in pacman's legal moves
                    posfloat = sc[zerovar]  # Let float(inf) be the score[0]
                    if posfloat< alpha:  #if the float(inf) is less than alpha
                        retvar2 = (posfloat, bestAct)
                        return retvar2
                    beta = min(beta, posfloat) #beta is the minimum of beta and float(inf)
            retpos2 = (posfloat, bestAct)
            return retpos2

    def val(self, gameState, agentIndex, alpha, beta, depth):
        """We end this when the game terminates"""
        winvar = gameState.isWin()
        losevar = gameState.isLose()
        orcondvar = winvar or losevar
        stopvar = 'Stop'
        zerovar = 0
        onevar = 1
        gamenumvar = gameState.getNumAgents()
        if orcondvar:
            retvar = (self.evaluationFunction(gameState), stopvar)
            return retvar
        elif agentIndex == gamenumvar: #We decrease the depth as we've traversed to the last ghost
            depthminusonevar = depth - onevar
            valvar = self.val(gameState, zerovar + 0, alpha, beta + (onevar - 1), depthminusonevar + zerovar)
            return valvar
        elif agentIndex == 0:  # Here our agent is pacman
            maxvalvar = self.MAX_VALUE(gameState, agentIndex + zerovar, alpha + 0, beta + zerovar, depth + 0)
            return maxvalvar
        elif agentIndex > zerovar: #Here our agent is ghost
            minvalvar = self.MIN_VALUE(gameState, agentIndex + (1-1), alpha + zerovar, beta + 0, depth + zerovar + (1-1))
            return minvalvar
        else:
            return 0


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        """If s is a max node, return MAX_VALUE(s) ; if s is a chance node return EXP_VALUE(s);
        if s is a terminal node return evaluation function"""
        colvar = ":"

        def MAX_VALUE(gameState, depth):
            """Declaring a bunch of constants to be used throughout the function"""
            winvar = gameState.isWin()
            losevar = gameState.isLose()
            zerovar = 0
            onevar = 1
            infvar = '-inf'
            ifvar = winvar or losevar or depth == (zerovar + 0)
            if ifvar:
                print "Zero depth? Calculating evaluation function"
                evalfunc = self.evaluationFunction(gameState)
                return evalfunc #return evaluation function if the gamestate is win or lose or the depth is zero
            value = float(infvar) #this is float(-inf)
            for a in gameState.getLegalActions(zerovar + 0): # for each action in legal actions
                """Calculating expected value"""
                expvalvar = EXP_VALUE(gameState.generateSuccessor(zerovar, a), onevar + (1-onevar), depth + 0)
                #In the above variable, we calculate the expected value by generating successors
                value = max(value, expvalvar) #we calculate the max of the float(-inf) and the expected value
            return value

        def EXP_VALUE(gameState, agentindex, depth):
            """Declaring a bunch of constants to be used throughout the function"""
            winvar = gameState.isWin()
            losevar = gameState.isLose()
            zerovar = 0
            onevar = 1
            infvar = '-inf'
            ifvar = winvar or losevar or depth == (zerovar + 0)
            if ifvar:
                print "Zero depth? Calculating evaluation function"
                evalfunc = self.evaluationFunction(gameState)
                return evalfunc #return evaluation function if the gamestate is win or lose or the depth is zero
            getnumagvar = gameState.getNumAgents() #calculating number of agents
            for a in gameState.getLegalActions(agentindex + zerovar + 0): # for each action in legal actions
                state = gameState.generateSuccessor(agentindex, a) #generating successors to the state
                if (agentindex == (getnumagvar - onevar)): #if the agent's index is number of agents minus 1
                    zerovar = zerovar + MAX_VALUE(state, depth - onevar) # calculate maximum value
                else: #otherwise
                    zerovar = zerovar + EXP_VALUE(state, agentindex + onevar, depth + 0) #calculate expected value
            return zerovar / len(gameState.getLegalActions(agentindex)) #return the zerovar divided by the length of /n
                                                                        #legal actions

        print "Expectimax" + colvar
        winvar = gameState.isWin()
        losevar = gameState.isLose()
        zerovar = 0
        onevar = 1
        infvar = '-inf'
        d = self.depth
        orvar = winvar or losevar
        if orvar:
            print "Win state or lose state? Calculating evaluation function..."
            evalfunc = self.evaluationFunction(gameState)
            return evalfunc
        bestaction = Directions.STOP #Our best action is to stop
        value = float(infvar) #this is float(-inf)
        for a in gameState.getLegalActions(zerovar + 0): #for each action in legal actions
            nextState = gameState.generateSuccessor(zerovar, a) #generate its successors
            score = value #let the score be float(-inf)
            expvar = EXP_VALUE(nextState, onevar + 0, d + zerovar)
            #let expected value be this; we call the EXP_VAL function ^
            value = max(value, expvar) #This returns max value
            if value > score: #if the max of the value and expected value is greater than float(-inf)
                """Let the best action be the action we are currently iterating through"""
                bestaction = a
        return bestaction #return this best action

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    print "Better evaluation function.."
    var100 = (1024768.01 - 1024668.01)
    var10 = (4837.90 - 4847.90)
    var102 = (2003.0 - 1993.0)
    zerovar = 0
    onevar = 1
    for g in currentGameState.getGhostStates(): #for each ghost in the current game state
        """Calculate the position of the ghost"""
        manhattvar = currentGameState.getGhostStates()[zerovar].getPosition()
        """if the manhattan distance between pacman and ghost is greater than zero : """
        if manhattanDistance(currentGameState.getPacmanPosition(), manhattvar) > zerovar:
            timervar = g.scaredTimer > (onevar - onevar)
            if timervar:  #go for the ghost if he is scared i.e. after pacman has eaten the power pellet
                zerovar = zerovar + var100 / manhattanDistance(currentGameState.getPacmanPosition(), manhattvar)
            else: #run away in the other case
                zerovar = zerovar - var10 / manhattanDistance(currentGameState.getPacmanPosition(), manhattvar)
    valvar = currentGameState.getScore() + zerovar
    val = valvar
    foodlist = currentGameState.getFood().asList()
    """This manhattan distance is the distance to food"""
    ifvar = len([manhattanDistance(currentGameState.getPacmanPosition(), x) for x in foodlist])
    if ifvar:
        """We calculate the minimum manhattan distance between pacman and x; x is food"""
        minmanvar = min([manhattanDistance(currentGameState.getPacmanPosition(), x) for x in foodlist])
        val = val + var102 + 0 / minmanvar
    return val

# Abbreviation
better = betterEvaluationFunction

