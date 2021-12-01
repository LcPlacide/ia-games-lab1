
def manhattan_distance(pos1, pos2):
  return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def euclidian_distance(pos1, pos2):
  return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

def corners_heuristic(state, problem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).

    euclidian_distance: 1445
    manhattan_distance: 1690
    """
    corners = problem.corners  # These are the corner coordinates
    walls = problem.walls  # These are the walls of the maze, as a Grid (game.py)
    current_position = state[0]

    # TODO Compute distances - current position to corners
    distances = [manhattan_distance(current_position, corner) for corner in corners]
    
    # Extract min distance
    min_distance = min(distances)

    return min_distance


if __name__ == '__main__':
    import os
    os.system('python3 -m pacman -a SearchAgent -p CornersSearchProblem -s astar_search -f corners_heuristic -l mediumCorners')
