from pacman.util import Queue


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.

    These are the functions to interact with the Pacman world:

    >>> state = problem.getStartState()
    >>> state
    (5, 5)

    >>> problem.getSuccessors(state)
    [((5, 4), 'South', 1), ((4, 5), 'West', 1)]

    >>> problem.isGoalState(state)
    False
    """

    # *** YOUR CODE HERE *** #
    # Explored set
    explored = {}

    # 1. Initialize the frontier as a FIFO queue
    frontier = Queue()

    # 2. Push the start state into the frontier
    start_state = problem.getStartState()
    frontier.push(start_state)

    # 3. Initialize the explored set with the start state 
    explored[start_state] = (None, None)
    
    # 4. While the frontier is not empty
    while not frontier.isEmpty():

        # a. Pop a state from the frontier
        popped_state = frontier.pop()

        # b. If it is a goal state, then stop
        if problem.isGoalState(popped_state):
            goal_state = popped_state
            break

        # c. For each successor of the popped state
        for successor in problem.getSuccessors(popped_state):
            # i. If the successor is not in the explored set, then
            if successor[0] not in explored.keys():
                # Push the successor into the frontier
                frontier.push(successor[0])
                #print(f"{len(frontier.list)} | push: {popped_state} -> {successor[0]}")

                # Add the successor to the explored set
                action = successor[1]
                state = successor[0]
                explored[state] = (popped_state, action)

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
    os.system('python3 -m pacman -a SearchAgent -s breadth_first_search -l tinyMaze')
    os.system('python3 -m pacman -a SearchAgent -s breadth_first_search -l mediumMaze')
    os.system('python3 -m pacman -a SearchAgent -s breadth_first_search -l bigMaze -z 0.5')
