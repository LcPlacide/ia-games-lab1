from pacman.util import PriorityQueue
from ex01 import path_reconstruction


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.

    These are the functions to interact with the Pacman world:

    >>> state = problem.getStartState()
    >>> state
    (5, 5)

    >>> problem.getSuccessors(state)
    [((5, 4), 'South', 1), ((4, 5), 'West', 1)]

    >>> problem.isGoalState(state)
    False
    """

    # 1. Initialize the frontier as a priority queue
    frontier = PriorityQueue()

    # 2. Push the start state into the frontier with priority 0
    start_state = problem.getStartState()
    frontier.push(start_state, 0)

    # 3. Initialize the explored set with the start state
    explored = {}
    explored[start_state] = (None, None)

    # 4. Set the past cost of the start state to 0
    past_cost = {start_state: 0}

    # 5. While the frontier is not empty
    while not frontier.isEmpty():
        # a. Pop a state from the frontier
        popped_state = frontier.pop()

        # b. If it is a goal state, then stop
        if problem.isGoalState(popped_state):
            goal_state = popped_state
            break

        # c. For each successor of the popped state
        for successor in problem.getSuccessors(popped_state):
            # i. new cost = past cost of the popped state + cost of the action leading to successor
            next_state, action, cost = successor
            popped_cost = past_cost[popped_state]
            new_cost = popped_cost + cost

            # i. If the successor is not in the explored set
            # or new cost is less than the past cost of the successor, then
            if (next_state not in explored.keys()) or (new_cost <= popped_cost):
                # 1. priority = new cost
                priority = new_cost

                # 2. Push or update the successor into the frontier using the priority above
                frontier.push(next_state, priority)

                # 3. Add the successor to the explored set
                explored[next_state] = (popped_state, action)

                # 4. Set the past cost of the successor to new cost
                past_cost[next_state] = new_cost

    return path_reconstruction(start_state, goal_state, explored)

def path_reconstruction(start, goal, explored):
    # *** YOUR CODE HERE *** #
    # 1. Initialize the path as an empty list
    path = []

    # 2. Set the goal state as the current state
    current_state = goal

    # 3. While the current state is not the start state
    while current_state != start:
        # a. Fetch the predecessor and the action of the current state from the explored set
        predecessor, action = explored[current_state]

        # b. Append the action to the path
        path.append(action)

        # c. Set the predecessor as the current state
        current_state = predecessor

    # 4. Reverse the list of actions in the path
    path.reverse()

    return path

if __name__ == '__main__':
    import os
    os.system('python3 -m pacman -a SearchAgent -s uniform_cost_search -l mediumMaze')
    os.system('python3 -m pacman -a SearchAgent -s uniform_cost_search -l mediumMaze -c stay_east')
    os.system('python3 -m pacman -a SearchAgent -s uniform_cost_search -l mediumMaze -c stay_west')
