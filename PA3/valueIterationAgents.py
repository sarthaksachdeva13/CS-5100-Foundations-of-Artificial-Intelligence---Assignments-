# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        printvar = "Value Iteration"
        print printvar + ":"
        iterange = range(self.iterations)
        possiblestates = self.mdp.getStates()
        counter2 = self.values.copy()
        terminalvar = self.mdp.isTerminal
        zerovar = 0
        one = 1
        onevar = (2 - one)
        for i in iterange:  # Iterating over each value
            for s in possiblestates:  # For every state 's' in all possible states in the MDP:
                valforaction = util.Counter()
                valmaxarg = valforaction.argMax()
                terminalvar = self.mdp.isTerminal(s)
                actionvar = self.mdp.getPossibleActions(s) #variable for mdp's possible actions
                if terminalvar:  #If s is a terminal state
                    counter2[s] = zerovar  #Return zero
                else:
                    for a in actionvar:  #Iterating through every possible action
                        total = 0 #taking a counter
                        """For every transition in the list of (nextState, prob) pairs"""
                        for t in self.mdp.getTransitionStatesAndProbs(s,a):
                            secondvar = (self.mdp.getReward(s, a, t[zerovar]) + discount * (self.values[t[zerovar]]))
                            total = total + t[onevar] * secondvar #Bellman Equation for value iteration
                        valforaction[a] = total
                counter2[s] = valforaction[valforaction.argMax()]
            self.values = counter2.copy()

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        zerovar = 0 #let this be the qvalue
        zero = 0 #variable for zero
        onevar = 1 #variable for 1
        disc = self.discount
        """Assigning mdp transition states and probs to a variable """
        mdptransandprobs = self.mdp.getTransitionStatesAndProbs(state,action)
        for t in mdptransandprobs: #going through transitions through the variable
            zerovar = zerovar + t[onevar] * (self.mdp.getReward (state, action, t[zero]) + \
                                             disc * (self.values[t[zero]]))
        return zerovar


        #util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        valueact = util.Counter() #making the value a util counter
        zerovar = 0 #assigning a variable to zero
        terminalvar = self.mdp.isTerminal(state) #let this variable be one where the mdp is a terminal state
        if terminalvar:
            return None  #We return nothing if the state is a terminal state
        lenaction = len(self.mdp.getPossibleActions(state))
        if int(lenaction) == zerovar:
            return None  # Return none if there are no possible actions
        else:
            for a in self.mdp.getPossibleActions(state):
                computervar = self.computeQValueFromValues(state, a)
                valueact[a] = computervar
            return valueact.argMax()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
