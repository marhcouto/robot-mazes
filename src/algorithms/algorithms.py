import math
from queue import Queue, LifoQueue
from time import perf_counter_ns

from algorithms.state import State
from algorithms.algorithm_stats import AlgorithmStats
from algorithms.heap import Heap
from model.game_model import GameModel


def breadth_first_search(game_model: GameModel) -> AlgorithmStats:
    q = Queue()
    s = set()
    nodes_explored = 0
    starting_state = State.initial_state(game_model.no_moves)
    cur_state: State

    q.put(starting_state)
    s.add(starting_state)

    start_time: int = perf_counter_ns()

    while True:
        if q.empty():
            cur_state = None
            break

        nodes_explored += 1

        cur_state = q.get()
        if game_model.simulate(cur_state.moves)[0]:
            break

        children = cur_state.generate_all_children()
        for child in children:
            if not (child in s):
                s.add(child)
                q.put(child)
    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, cur_state)


def depth_first_search(game_model: GameModel, max_depth=math.inf) -> AlgorithmStats:
    q = LifoQueue()
    s = set()
    nodes_explored = 0
    starting_state = State.initial_state(game_model.no_moves)
    cur_state: State

    q.put(starting_state)
    s.add(starting_state)

    start_time: int = perf_counter_ns()

    while True:
        if q.empty():
            cur_state = None
            break

        nodes_explored += 1

        cur_state = q.get()
        if game_model.simulate(cur_state.moves)[0]:
            break
        if cur_state.depth < max_depth:
            children = cur_state.generate_all_children()
            for child in children:
                if not (child in s):
                    q.put(child)
                    s.add(cur_state)

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, cur_state)


def iterative_deepening_search(game_model: GameModel) -> AlgorithmStats:
    depth = 0

    start_time: int = perf_counter_ns()

    nodes_explored = 0

    while True:
        alg_res = depth_first_search(game_model, depth)
        found: State = alg_res.solution_state
        nodes_explored += alg_res.iterations
        if found:
            break
        depth += 1

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, found)


def greedy_search(game_model: GameModel, heuristic):

    nodes_explored: int = 0
    visited_states = set()
    state_queue = Heap(lambda state: heuristic(game_model, state))
    state_queue.insert(State.initial_state(game_model.no_moves))
    current_state: State

    start_time: int = perf_counter_ns()
    while True:
        if state_queue.empty():
            print("Empty queue")
            current_state = None
            break

        nodes_explored += 1
        current_state = state_queue.pop()
        if game_model.simulate(current_state.moves)[0]:
            break
        new_valid_nodes = current_state.generate_all_children()
        for node in new_valid_nodes:
            if not (node in visited_states):
                state_queue.insert(node)
                visited_states.add(node)
    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, current_state)


def a_star_search(game_model: GameModel, heuristic):
    visited_nodes = {}
    node_queue = Heap(lambda state: heuristic(game_model, state))
    node_queue.insert(State.initial_state(game_model.no_moves))
    visited_nodes[State.initial_state(game_model.no_moves)] = heuristic(game_model, State.initial_state(game_model.no_moves))
    cur_node: State
    iter_num = 0

    start_time: int = perf_counter_ns()

    while not node_queue.empty():
        iter_num += 1
        cur_node = node_queue.pop()
        if game_model.simulate(cur_node.moves)[0]:
            break
        next_nodes = cur_node.generate_all_children()
        for node in next_nodes:
            if node not in visited_nodes:
                node_queue.insert_with_custom_value(visited_nodes[cur_node] + heuristic(game_model, node), node)
                visited_nodes[node] = heuristic(game_model, node) if not (node.parent in visited_nodes) else visited_nodes[node.parent] + heuristic(game_model, node)

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, iter_num, cur_node)
