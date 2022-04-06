from queue import Queue, LifoQueue

from state import RobotState



def bfs(no_moves):

    q = Queue()
    s = set()
    num_possible_states = pow(4, no_moves)

    starting_state = RobotState.initial_state(no_moves)

    q.put(starting_state)
    s.add(starting_state)

    while True:

        if q.empty():
            print("Empty queue")
            return 

        cur_state = q.get()

        # Objective Test

        if len(s) >= num_possible_states:
            break

        children = cur_state.generate_all_children()
        for child in children:
            q.put(child)
    
    return None

def dfs(no_moves):

    q = LifoQueue()
    s = set()
    num_possible_states = pow(4, no_moves)

    starting_state = RobotState.initial_state(no_moves)

    q.put(starting_state)
    s.add(starting_state)

    while True:

        if q.empty():
            print("Empty queue")
            return 

        cur_state = q.get()

        # Objective Test

        if len(s) >= num_possible_states:
            break

        children = cur_state.generate_all_children()
        for child in children:
            q.put(child)
    
    return None

