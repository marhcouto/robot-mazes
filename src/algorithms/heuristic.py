from model.game_model import Direction
from queue import Queue


def manhattan_distance(game_model, state):
    #return abs(final_pos.row - game_model.maze.final_robot_pos.row) + abs(final_pos.column - game_model.maze.final_robot_pos.column)
    return None


def generate_neighbour_positions(maze, cur_robot_pos):
    neigh = []
    for direction in Direction:
        if maze.can_move(cur_robot_pos, direction):
            neigh.append(cur_robot_pos.move(direction))
    return neigh


def maze_bfs(maze):
    q = Queue()
    s = set()
    starting_state = (maze.init_robot_pos, None)
    cur_state = starting_state

    q.put(starting_state)
    s.add(starting_state)

    while not q.empty():
        cur_state = q.get()
        s.add(cur_state)
        if cur_state[0] == maze.final_robot_pos:
            break

        children = generate_neighbour_positions(maze, cur_state[0])
        children = [child for child in map(lambda child_pos: (child_pos, cur_state), children)]
        for child in children:
            if not (child in s):
                q.put(child)

    path = []
    while cur_state[1]:
        path.append(cur_state[0])
        cur_state = cur_state[1]
    path.append(cur_state[0])
    path.reverse()
    return path


def shortest_path_heuristic(game_model, state):
    for position in maze_bfs(game_model.maze):
        print(position)