import cProfile
import re


pancakeStackBeta = [1, 2, 3, 4, 5]  # Dummy stack to test functions don't explode

pancakeStack0 = [1, 3, 5, 2, 4, 6]
pancakeStack1 = [8, 2, 1, 7, 5, 4, 6, 3, 9, 10]
pancakeStack2 = [9, 5, 2, 8, 4, 1, 10, 6, 7, 3]
pancakeStack3 = [2, 8, 10, 5, 7, 3, 4, 6, 1, 9]
pancakeStack4 = [3, 6, 8, 10, 7, 1, 5, 4, 2, 9]
pancakeStack5 = [6, 9, 4, 8, 1, 3, 2, 7, 10, 5]
pancakeStack6 = [8, 5, 10, 6, 2, 9, 3, 4, 1, 7]
pancakeStack7 = [8, 1, 10, 5, 3, 7, 4, 9, 2, 6]

# Class of Pancake that consists of the
# stack: the current state
# actions: action used to the state
# parent: the state that was used to get to the current statetempState in the pancake class that is to act as the parent
# # pancake.
class Pancake:
    def __init__(self, stack, action, parent):
        self.stack = stack      # Current list/state of the pancakeStack
        self.action = action    # Int for the action used to get to this current pancake
        self.parent = parent    # Node pointing to the parent of the current pancake,
        self.cost = 0           # This will be used for the heuristic

        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0




# Part 1
# Return a list of numbers 2 through n where n is the size of the pancake stack. Actions are flip the first or last pancake
# Inputs (int list):
#   panList: the initial list of pancakes
# Output:
#   actions (int list): list that can be done on the list of pancakes, ranging from 2...n, n being panList's length
def possibleActions(panList):
    actions = []
    for i in range(2, len(panList) + 1):
        actions.append(i)
    return actions

# Part 2
# Flips the pancakes at the given action location and returns a list of the pancakes, does not modify the original list
# Inputs:
#   panList (int list): List of the pancakes in unsorted order
#   n (int): the action to be taken on the pancake stack, what pancake will be flipped
# Outputs:
#   dummyPanList (int list): list of the current order of pancakes after there was a flip action

def result(panList, n):
    # Dummy array to prevent the base array from being modified
    dummyPanList = panList[:]
    # Dummy array to invert and then re-add to other array
    holderPancakeList = []
    for x in range(n):
        holderPancakeList.append(dummyPanList[x])
    holderPancakeList.reverse()

    for y in range(n):
        dummyPanList[y] = holderPancakeList[y]
    return dummyPanList


# Part 3
# Gives all the possible states a pancake can be in after 1 action is taken, this is done running
# result against all the outputs of possible actions
# Inputs:
#   pancakeList (int list): list of pancakes in their current order provided
# Outputs:
#   pancakeExpanded (list of int lists): a list containing all the lists from one action taken on the list of pancakes
def expand(pancakeList):  # Make it so that it starts at 0 instead of 1, len-1 or something. n = 1 does nothing
    pancakeActions = possibleActions(pancakeList)
    pancakeExpanded = []

    for action in pancakeActions:
        pancakeExpanded.append(result(pancakeList, action))

    return pancakeExpanded

# Part 3 also
# A node based approach to expanding the possible amount of possible outcomes of pancakes, similar to part 3 but
# returns a list of nodes.
# Inputs:
#   pancakeList (int list): list of pancakes in their current order provided
# Outputs:
# pancakeExpanded (node list): list of nodes of states that point back to the parent, that being pancakeList
# These nods contains the state of the list, action done on the parent to get to this state and parent of the node
def expandNode(pancakeList):  # pancakeList is a Pancake Node instead, and the returned expanded also returns nodes
    pancakeActions = possibleActions(pancakeList.stack)
    pancakeExpanded = []

    for action in pancakeActions:
        if action != pancakeList.action:
            pancakeExpanded.append(Pancake(result(pancakeList.stack, action), action, pancakeList))

    return pancakeExpanded


# Exact same as expandNode but instead packcake.action returning an int of a single action an array of actions is returned instead
# This is used only in breadthFirstSearch as a way to reduce runtime by tying all the actions to a single node
# instead of having to climb back to parent
# Inputs:
#   pancakeList (int list): list of pancakes in their current order provided
# Outputs:
# pancakeExpanded (node list): list of nodes of states that point back to the parent, that being pancakeList
# These nods contains the state of the list, actions done to get to this state from initial and parent of the node
def expandNode2(pancakeList):  # pancakeList is a Pancake Node instead, and the returned expanded also returns nodes
    pancakeActions = possibleActions(pancakeList.stack)
    pancakeExpanded = []


    for action in pancakeActions:
        if action != pancakeList.action:
            tempArray = []
            if pancakeList.action is not None:
                tempArray = tempArray + pancakeList.action
            tempArray.append(action)
            pancakeExpanded.append(Pancake(result(pancakeList.stack, action), tempArray, pancakeList))

    return pancakeExpanded



# Redacted methods but left for the purpose of my reference
"""
# Part 4
def iterativeDeepeningSearch(initialState, goalState, runningCount):
    # dummyVariables
    dummypanList = []  # List safe to modify
    optimalSolution = []  # List of the list of changes
    for i in range(len(initialState)):  # Sets the dummy list = to intialState
        dummypanList.append(initialState[i])

    for x in range(len(dummypanList)):  # Goes down the list all possible pancake flips
        if (dummypanList == goalState):  # This is wrong, you gotta check each value 1 by 1 to make sure of it
            optimalSolution = dummypanList
        result(dummypanList, x)  # Does a flip of size n

        iterativeDeepeningSearch(dummypanList, goalState, runningCount + 1)

    return optimalSolution
"""
"""
def iterativeDeepeningSearch(initialState, goalState, runningCount):    #Goes infinite atm but should work when that is fixed
    optimalSolution = []                                                # List of the list of changes
    rows = expand(initialState)
    for i in range(len(rows)):
        runningCount = runningCount+1
        optimalSolution.append(i)
        if[i] == goalState:
            return optimalSolution
        iterativeDeepeningSearch(initialState, goalState, runningCount)
        optimalSolution.pop()

    return optimalSolution
    """
"""
def iterativeDeepeningSearch(initialState, goalState, runningCount):
    while tempState.stack != goalState:     #tempState.stack isn't being modified
        print(tempState.stack)
        if tempState.depth < 2*len(initialState):
            pancakeList = expandNode(tempState) + pancakeList
            tempState = pancakeList[0]
            pancakeList.pop(0)
        else:
            tempState = pancakeList[0]
"""
# Part 4
# Implementation of iterative search. This is done so making a tempState in the pancake class that is to act as the parent
# pancake. In the loop it goes for until the tempState reaches the goal state.
# Check the current depth, adds the current action to the stack and goes deeper, it reaches it the end it pops off
# Must generate the entire tree, except checked states, to ensure that the optimal solution is found
# and goes down the next path.
# Inputs:
#   initialState (int list): the initial state of pancakes that s going to be sorted
#   goalState (int list): the ordered list of pancakes that is being searched for
# Outputs:
#   actionlist (int list): The list of actions to take inorder to achieve the goal state
def iterativeDeepeningSearch(initialState, goalState):
    tempState = Pancake(initialState, None, None)
    pancakeList = expandNode(tempState)
    maxdepth = len(initialState)
    optimal = tempState


    checked = []
    loop = True
    while loop:
        for stack in pancakeList:
            if (stack not in checked) and (stack.depth < maxdepth):     # Makes sure that there is no double checking and that the search is not too deep
                checked.append(stack)
                tempState = stack
                if tempState.stack == goalState:
                    optimal = tempState
                    maxdepth = tempState.depth
                    # break
                if tempState.depth < maxdepth:
                    pancakeList = expandNode(tempState) + pancakeList
                    break
                print(len(pancakeList))                 # Size of the pancakeList, used as a means to measure memory
                loop = False


    actionList = []
    while optimal.parent is not None:
        actionList.insert(0, optimal.action)
        optimal = optimal.parent

    print(actionList)
    return actionList



# Part 5
# Implementation of breadthFirstSearch. This is done so by tempState in the pancake class that is to act as the parent
# pancake. Each iteration of the loop expands the current states and then appends them to the back of the list and
# then pops the value that was expanded.
# When the goal value is found it climbs the parent nodes of the states and builds and returns the action list
# Inputs:
#   initialState (int list): the initial state of pancakes that s going to be sorted
#   goalState (int list): the ordered list of pancakes that is being searched for
# Outputs:
#   actionlist (int list): The list of actions to take inorder to achieve the goal state
def breadthFirstSearch(initialState, goalState):
    tempState = Pancake(initialState, None, None)                   # Declares a temp Pancake value that is of the initial state
    pancakeList = [tempState]                                       # A list of pancakes that initially only contains the temp state
    #print(pancakeList)
    checked = []
    while tempState.stack != goalState:                             # Checks if the initial state is the correct answers

        searchNextArray = []                                         # A list of searched values and used to prevent double searching
        for pancakeLooper in pancakeList:                           # pancakeLooper is a dummy pancake value to check after an expansion of the list
            #print(pancakeLooper.stack)
            if pancakeLooper.stack not in checked:                  # Checks if pancakeLooper's value is apart of checked, if it is skip and move on to the next
                tempState = pancakeLooper
                if tempState.stack == goalState:                    # If the goal is found it ends both loops, since its breadth first the first solution is optimal
                    print(len(pancakeList))                         # Size of the pancakeList, used as a way to measure memory
                    break
                holderArray = expandNode2(tempState)                # Temp array to hold the expanansion of tempState
                searchNextArray = searchNextArray + holderArray     # Adds the expanded nodes to the searchNextArray
                checked.append(pancakeLooper.stack)
                #checked.sort()                                     # Used to debug to ensure no duplicate values in checked
        pancakeList = list(set(searchNextArray))                    # Essentially ensures there is no duplicate values in pancakeList
    print(tempState.action)
    return tempState.action

# Part 6

# Helper function that takes pancake and returns the sorted cost
def sortFunc(pancake):
    return pancake.cost

# Implementation of aStar. In this function a value is assigned to each state and sorted.
# The state with the lowest cost then is chosen and expanded.
# The process repeats until the solution is found with the cost of 0 function is found.
# Inputs:
#   initialState (int list): the initial state of pancakes that s going to be sorted
#   goalState (int list): the ordered list of pancakes that is being searched for
#   heuristic (function): the heuristic function that will determines how the cost will be determined
# Outputs:
#   actionlist (int list): The list of actions to take inorder to achieve the goal state
def aStar(initialState, goalState, heuristic):
    tempState = heuristic(Pancake(initialState, None, None))
    pancakeList = []
    while tempState.stack != goalState:
        tempList = []
        for pancake in expandNode(tempState):
            tempList.append(heuristic(pancake))

        if tempState.depth < len(initialState):
            pancakeList = pancakeList + tempList
            pancakeList.sort(key=sortFunc)

            tempState = pancakeList[0]
            pancakeList.pop(0)
        else:
            tempState = pancakeList[0]
    print(len(pancakeList))                     # Size of the pancakeList, used as a way to measure memory
    actionList = []
    while tempState.parent is not None:
        actionList.insert(0, tempState.action)
        tempState = tempState.parent
    print(actionList)
    return actionList

# Heuristic cost of A* search
def heuristic(pancake):
    if pancake.parent is not None:
        pancake.cost += pancake.parent.cost

    i = 0
    while i < len(pancake.stack) - 2:
        if abs(pancake.stack[i] - pancake.stack[i + 1]) != 1:
            pancake.cost += 1
        i += 1
    return pancake

# Uniform cost of used in the A* search
def uniform(pancake):
    return pancake

def sevenPointOne():
    cProfile.run('iterativeDeepeningSearch(pancakeStack0, [1, 2, 3, 4, 5, 6])')
    cProfile.run('breadthFirstSearch(pancakeStack0, [1, 2, 3, 4, 5, 6])')
    cProfile.run('aStar(pancakeStack0, [1, 2, 3, 4, 5, 6], uniform)')

def sevenPointTwo():
    cProfile.run('aStar(pancakeStack0, [1, 2, 3, 4, 5, 6], uniform)')
    cProfile.run('aStar(pancakeStack0, [1, 2, 3, 4, 5, 6], heuristic)')

def sevenPointThreeAStar():
    cProfile.run('aStar(pancakeStack2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')
    cProfile.run('aStar(pancakeStack3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')
    cProfile.run('aStar(pancakeStack4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')
    cProfile.run('aStar(pancakeStack5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')
    cProfile.run('aStar(pancakeStack6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')
    cProfile.run('aStar(pancakeStack7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic)')

def sevenPointThreeBreadth():
    cProfile.run('breadthFirstSearch(pancakeStack1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')
    cProfile.run('breadthFirstSearch(pancakeStack7, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])')



if __name__ == '__main__':
    # Various Tests to ensure the methods work on simple issues
    #-----------------------------------------------------------------
    # print(pancakeStackBeta)                                    # Original Stack
    # print(result(pancakeStackBeta, 2))                        # Prints what the flip looks like
    # print(pancakeStackBeta)                                   # Ensures the original is not modified
    # print(expand(pancakeStackBeta))                            # Prints all possible flips of pancakeStackBeta
    # print(expandNode(Pancake(pancakeStackBeta, None, None)))  # Test to see that the the nodes point correctly
    # print(iterativeDeepeningSearch([3, 2, 1], [1, 2, 3]))       # Prints the actions needed to flip a simple stack
    # print(breadthFirstSearch(pancakeStack0, [1, 2, 3, 4, 5, 6]))
    # print(aStar(pancakeStack0, [1, 2, 3, 4, 5, 6], uniform))
    # print(aStar(pancakeStack0, [1, 2, 3, 4, 5, 6], heuristic))
    # print(aStar(pancakeStack1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], heuristic))
    # print(breadthFirstSearch(pancakeStack1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    #-----------------------------------------------------------------

    # 7.1
    sevenPointOne()    # Works fine
    # 7.2
    sevenPointTwo()     # Heuristic isn't fully optimal but fast

    # 7.3
    sevenPointThreeAStar()      # Does not compute stack-6 and stack-7 in reasonable time/at all potentially
    sevenPointThreeBreadth()    # Awful runtime, stack-1 took 28 minutes and gets stack-2 after a few hours