def manhattan_distance(final_robot_pos, final_pos):
    return abs(final_pos.row - final_robot_pos.row) + abs(final_pos.column - final_robot_pos.column)
