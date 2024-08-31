import maze


def minimax(grid, current_cat, current_robot, goal, depth, alpha, beta, maximizing_player, visited_positions):
    if depth == 0 or current_cat == goal or current_robot == goal:
        return enhanced_evaluate_state(grid, current_cat, current_robot, goal), None

    if maximizing_player:  # Robot's turn
        max_eval = float('-inf')
        best_move = None
        for neighbor in current_robot.create_neighbors(grid):
            if valid_move(current_robot, neighbor, grid) and neighbor not in visited_positions:
                visited_positions.add(neighbor)
                eval, _ = minimax(grid, current_cat, neighbor, goal, depth - 1, alpha, beta, False, visited_positions)
                visited_positions.remove(neighbor)
                if eval > max_eval:
                    max_eval = eval
                    best_move = neighbor
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval, best_move
    else:  # Cat's turn
        min_eval = float('inf')
        best_move = None
        for neighbor in current_cat.create_neighbors(grid):
            if valid_move(current_cat, neighbor, grid) and neighbor not in visited_positions:
                visited_positions.add(neighbor)
                eval, _ = minimax(grid, neighbor, current_robot, goal, depth - 1, alpha, beta, True, visited_positions)
                visited_positions.remove(neighbor)
                if eval < min_eval:
                    min_eval = eval
                    best_move = neighbor
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval, best_move

def enhanced_evaluate_state(grid, current_cat, current_robot, goal):
    # Base evaluation: difference in distance to the goal
    cat_distance = len(maze.bfs(grid, current_cat, goal))
    robot_distance = len(maze.bfs(grid, current_robot, goal))
    
    if current_cat == goal:
        return float('-inf')
    elif current_robot == goal:
        return float('inf')
    
    # Additional evaluation criteria
    evaluation = robot_distance - cat_distance
    
    # Penalize proximity to dead ends
    cat_dead_end_penalty = len([n for n in current_cat.create_neighbors(grid) if not valid_move(current_cat, n, grid)])
    robot_dead_end_penalty = len([n for n in current_robot.create_neighbors(grid) if not valid_move(current_robot, n, grid)])
    
    evaluation -= (cat_dead_end_penalty - robot_dead_end_penalty) * 10
    
    # Distance between Cat and Robot (to avoid unnecessary conflicts)
    distance_between_agents = len(maze.bfs(grid, current_cat, current_robot))
    evaluation += distance_between_agents
    
    return evaluation
def valid_move(current, neighbor, grid):
    if neighbor.r < 0 or neighbor.c < 0 or neighbor.r >= maze.nrows or neighbor.c >= maze.ncols:
        return False
    if (current.walls[0] == False and neighbor == grid[current.r - 1][current.c]) or \
       (current.walls[1] == False and neighbor == grid[current.r][current.c + 1]) or \
       (current.walls[2] == False and neighbor == grid[current.r + 1][current.c]) or \
       (current.walls[3] == False and neighbor == grid[current.r][current.c - 1]):
        return True
    return False

def evaluate_state(grid, current_cat, current_robot, goal):
    cat_distance = len(maze.bfs(grid, current_cat, goal))
    robot_distance = len(maze.bfs(grid, current_robot, goal))
    if current_cat == goal:
        return float('-inf')
    elif current_robot == goal:
        return float('inf')
    return robot_distance - cat_distance

# def get_best_move(grid, current_cat, current_robot, goal, depth, maximizing_player, previous_positions):
#     best_move = None
#     best_eval = float('-inf') if maximizing_player else float('inf')
#     for neighbor in (current_robot.create_neighbors(grid) if maximizing_player else current_cat.create_neighbors(grid)):
#         if valid_move(current_robot if maximizing_player else current_cat, neighbor, grid) and (neighbor.r, neighbor.c) not in previous_positions:
#             eval = minimax(grid, current_cat if maximizing_player else neighbor, neighbor if maximizing_player else current_robot, goal, depth, float('-inf'), float('inf'), not maximizing_player, previous_positions.copy())
#             if (maximizing_player and eval > best_eval) or (not maximizing_player and eval < best_eval):
#                 best_eval = eval
#                 best_move = neighbor
#     return best_move