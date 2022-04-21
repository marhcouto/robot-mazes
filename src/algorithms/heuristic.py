def manhattan_distance(game_model, state):
    return abs(final_pos.row - game_model.maze.final_robot_pos.row) + abs(final_pos.column - game_model.maze.final_robot_pos.column)
