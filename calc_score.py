def calculate_score(blocks_accessed, optimal_path_length, time_elapsed, level):
    # Define base scores and penalties for each level
    base_scores = {'easy': 100, 'medium': 400, 'hard': 900}
    time_limits = {'easy': 15, 'medium': 25, 'hard': 40}
    block_penalties = {'easy': 0, 'medium': 1, 'hard': 2}
    time_penalties = {'easy': 0, 'medium': 1, 'hard': 2}

    base_score = base_scores[level]
    time_limit = time_limits[level]
    block_penalty = block_penalties[level]
    time_penalty = time_penalties[level]

    # Calculate excess blocks accessed
    excess_blocks = max(0, blocks_accessed - optimal_path_length)
    
    # Calculate time penalty
    excess_time = max(0, time_elapsed - time_limit)
    
    # Calculate final score with penalties
    score = base_score - (excess_blocks * block_penalty) - (excess_time * time_penalty)
    return max(score, 0)  # Ensure score is not negative
