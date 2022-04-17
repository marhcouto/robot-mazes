from queue import Queue, LifoQueue
from heap import Heap

from state import RobotState

from maze import simulate


def breadth_first_search(maze, no_moves):
    q = Queue()
    s = set()

    starting_state = RobotState.initial_state(no_moves)

    q.put(starting_state)
    s.add(starting_state)

    while True:
        if q.empty():
            print("Empty queue")
            return None

        cur_state = q.get()
        s.add(cur_state)

        if simulate(maze, cur_state.moves):
            return cur_state.moves

        children = cur_state.generate_all_children()
        for child in children:
            if not (child in s):
                q.put(child)
    return None


def depth_first_search(maze, no_moves):
    q = LifoQueue()
    s = set()

    starting_state = RobotState.initial_state(no_moves)

    q.put(starting_state)
    s.add(starting_state)

    while True:
        if q.empty():
            print("Empty queue")
            return None

        cur_state = q.get()
        s.add(cur_state)

        if simulate(maze, cur_state.moves):
            return cur_state.moves

        children = cur_state.generate_all_children()
        for child in children:
            if not (child in s):
                q.put(child)
    return None


def iterative_deepening_search(maze, no_moves):
    depth = 0
    starting_state = RobotState.initial_state(no_moves)
    while True:
        found = dls(maze, starting_state, depth)
        if found:
            return found
        depth += 1


def dls(maze, node, depth):
    if depth == 0:
        if simulate(maze, node.moves):
            return node
        else:
            return None
    elif depth > 0:
        children = node.generate_all_children()
        for child in children:
            found = dls(maze, child, depth - 1)
            if found:
                return found
    return None


def greedy_search(maze, no_moves, heuristic):
    visited_states = set()
    state_queue = Heap(heuristic)
    state_queue.insert(RobotState.initial_state(no_moves))
    while True:
        current_state = state_queue.pop()
        visited_states.add(current_state)
        if simulate(maze, current_state.moves):
            return current_state
        new_valid_nodes = current_state.generate_all_children()
        for node in new_valid_nodes:
            if not (node in visited_states):
                state_queue.insert(node)


def a_star_search(maze, no_moves, heuristic):
    visited_nodes = {}
    node_queue = Heap(heuristic)
    node_queue.insert(RobotState.initial_state(no_moves))
    iter_num = 0
    while not node_queue.empty():
        iter_num += 1
        cur_node = node_queue.pop()
        visited_nodes[cur_node] = heuristic(cur_node) if not (cur_node.parent in visited_nodes) else visited_nodes[cur_node.parent] + heuristic(cur_node)
        if simulate(maze, cur_node.moves):
            return cur_node
        next_nodes = cur_node.generate_all_children()
        for node in next_nodes:
            if node not in visited_nodes:
                node_queue.insert_with_custom_value(visited_nodes[cur_node] + heuristic(node), node)
