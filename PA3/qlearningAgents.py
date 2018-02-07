# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        """Init function"""
        self.qvalues = util.Counter() #Assigning util.Counter to qvalues

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        """Get Qvalue function"""

        return self.qvalues[(state,action)] #returns the qvalues


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        printvar = "Computing value from QValues" + ":"
        print printvar
        qvallist = [] #let this be an empty list
        legalactvar = self.getLegalActions(state) #Let legal actions in a state be assigned to this variable
        lenlegalact = len(self.getLegalActions(state)) #Length of the legalact variable defined above
        zerovarint = 0 #just a variable for zero
        zerovarfloat = (2.56-2.56) #variable for 0.0 (i.e. float value for 0)

        for a in legalactvar: #for each legal action in the state
            qvalvar = self.getQValue(state,a)
            qvallist.append(qvalvar) #append the qvalues in the list
        if lenlegalact == zerovarint: #if the length of the legal actions is zero
            return zerovarfloat #return zero (the float one)
        else:
            return max(qvallist) #Otherwise return the maximum from that list


    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        printvar = "Computing action from qvalues" + " "
        maxact = None #Variable for None
        qvalmaxzero = 0 #Again, a variable for zero
        legalact = self.getLegalActions(state) #Let legal actions in a state be assigned to this variable
        for a in legalact:  #for each legal action in the state
            qvalvar = self.getQValue(state, a) #let the qvalues be assigned to this
            """If any of the above qvalues is greater than zero, or the maximum action is None :"""
            if qvalvar > qvalmaxzero or maxact is None:
                qvalmaxzero = qvalvar #update the qvalue to be the value that's greater than zero
                maxact = a
                """Let the max action, which was none before, now be the action for which these conditions hold true"""
        return maxact #Return this action

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        """GetAction function"""
        epsilonvar = self.epsilon #Variable for self.epsilon
        utilepsvar = util.flipCoin(epsilonvar) #simulating a binary variable with probability epsilon
        randvar = random.choice(legalActions) #choosing an element from the legalactions list uniformly at random
        qvalactvar = self.computeActionFromQValues(state)

        if utilepsvar: #if the util.flipcoin value is true
            return randvar #return the random element
        else:
            return qvalactvar #otherwise compute action from qvalues of the state

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        # Using instance variables self.alpha and self.discount to compute q values :
        # Q(s, a) = Q(s, a) + alpha * (reward + gamma * Q (s' , a) - Q(s, a))

        # Here self.alpha is the learning rate and self.discount is the discount rate(gamma)

        # (reward + gamma * Q ( sprime , a)) is the learned value
        # Q(s, a) is the old value


        printvar = "update function"
        print "Calling the " + printvar + "..."
        one = 1 #Variable for 1
        zerovar = (one - 1)
        onevar = (2 - one)
        alpha = self.alpha #creating a variable for alpha
        discount = self.discount #creating a variable for discount
        getqvalvar = self.getQValue(state, action) #get Qvalue
        legalactvar = self.getLegalActions(nextState) #get legal actions for the next state
        lenlegalact = len(legalactvar) #Length of the legalact variable

        if lenlegalact == zerovar: #If the length of the legalactions is zero
            val = reward #let the value be the reward
        else:
            """Calculate the max Qval for each legal action """
            qvalnextstate = [self.getQValue(nextState, a) for a in legalactvar]
            maxvar = max(qvalnextstate)
            val = reward + (discount * maxvar) #Otherwise let the value be the reward plus discount times maxvar
        self.qvalues[(state, action)] = (onevar - alpha) * getqvalvar + alpha * val

    def getPolicy(self, state):
        """Getting policy"""
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        """Getting value"""
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"


        qvalues = self.featExtractor.getFeatures(state, action) * (self.weights) # Makes qvalues the sum of extracted feature values and weights
        return qvalues

        #util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"

        # Using q value iteration based on transition
        # transition = (reward + gamma * Q (sprime , a) - Q(s, a))
        # (reward + gamma * Q ( sprime , a) is the learned value
        # Q(s, a) is the old value

        transition = (reward + self.discount * self.computeValueFromQValues(nextState)) - self.getQValue(state, action)

        for i in self.featExtractor.getFeatures(state, action): #Traversing through each feature in the vector

            self.weights[i] = self.weights[i] + self.alpha * transition * self.featExtractor.getFeatures(state, action)[i] #Updating weights

        #util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
