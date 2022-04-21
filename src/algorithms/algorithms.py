from queue import Queue, LifoQueue
from time import perf_counter_ns

from algorithms.state import State
from algorithms.algorithm_stats import AlgorithmStats
from algorithms.heap import Heap
from model.game_model import GameModel
from model.sample_mazes import SAMPLE_MAZE



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
            print("Empty queue")
            return None

        nodes_explored += 1

        cur_state = q.get()
        s.add(cur_state)

        if game_model.simulate(None, cur_state.moves):
            break

        children = cur_state.generate_all_children()
        for child in children:
            if not (child in s):
                q.put(child)

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, cur_state)


def depth_first_search(game_model: GameModel, max_depth = 100) -> AlgorithmStats:
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
            print("Empty queue")
            return None

        nodes_explored += 1

        cur_state = q.get()
        if len(cur_state.build_state_history()):
            s.add(cur_state)
            if game_model.simulate(None, cur_state.moves):
                break
            children = cur_state.generate_all_children()
            for child in children:
                if not (child in s):
                    q.put(child)
        else:
            cur_state = None
            break

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    return AlgorithmStats(time, nodes_explored, cur_state)


def iterative_deepening_search(game_model: GameModel) -> AlgorithmStats:
    depth = 0
    starting_state = State.initial_state(game_model.no_moves)

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
    state_queue = Heap(heuristic)
    state_queue.insert(State.initial_state(game_model.no_moves))
    current_state: State

    start_time: int = perf_counter_ns()
    while True:
        if state_queue.empty():
            print("Empty queue")
            return None

        nodes_explored += 1
        current_state = state_queue.pop()
        visited_states.add(current_state)
        if game_model.simulate(None, current_state.moves):
            break
        new_valid_nodes = current_state.generate_all_children()
        for node in new_valid_nodes:
            if not (node in visited_states):
                state_queue.insert(node)

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    history = [state for state in map(lambda x: x.moves, current_state.build_state_history())]
    return AlgorithmStats(time, nodes_explored, history)


def a_star_search(game_model: GameModel, heuristic):
    visited_nodes = {}
    node_queue = Heap(heuristic)
    node_queue.insert(State.initial_state(game_model.no_moves))
    cur_node: State
    iter_num = 0

    start_time: int = perf_counter_ns()

    while not node_queue.empty():
        iter_num += 1
        cur_node = node_queue.pop()
        visited_nodes[cur_node] = heuristic(cur_node) if not (cur_node.parent in visited_nodes) else visited_nodes[cur_node.parent] + heuristic(cur_node)
        if game_model.simulate(None, cur_node.moves):
            break
        next_nodes = cur_node.generate_all_children()
        for node in next_nodes:
            if node not in visited_nodes:
                node_queue.insert_with_custom_value(visited_nodes[cur_node] + heuristic(node), node)

    end_time: int = perf_counter_ns()
    time: float = (end_time - start_time) / 1000000
    history = [state for state in map(lambda x: x.moves, cur_node.build_state_history())]
    return AlgorithmStats(time, iter_num, history)
