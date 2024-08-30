import random

def initialize_population(pop_size, max_moves):
    return [[random.choice(['U', 'D', 'L', 'R']) for _ in range(max_moves)] for _ in range(pop_size)]

def evaluate_individual(grid, individual, start, goal, nrows, ncols):
    current = start
    for move in individual:
        if move == 'U' and not current.walls[0] and current.r > 0:
            current = grid[current.r - 1][current.c]
        elif move == 'D' and not current.walls[2] and current.r < nrows - 1:
            current = grid[current.r + 1][current.c]
        elif move == 'L' and not current.walls[3] and current.c > 0:
            current = grid[current.r][current.c - 1]
        elif move == 'R' and not current.walls[1] and current.c < ncols - 1:
            current = grid[current.r][current.c + 1]
        if current == goal:
            break
    distance_to_goal = abs(goal.r - current.r) + abs(goal.c - current.c)
    return 1 / (1 + distance_to_goal)

def select_parents(population, fitnesses, num_parents):
    parents = random.choices(population, weights=fitnesses, k=num_parents)
    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(['U', 'D', 'L', 'R'])

def run_genetic_algorithm(grid, start, goal, nrows , ncols, pop_size=100, max_moves=100,
                          num_generations=100, mutation_rate=0.01):
    population = initialize_population(pop_size, max_moves)
    for generation in range(num_generations):
        fitnesses = [evaluate_individual(grid, individual, start, goal, nrows, ncols) for individual in population]
        if max(fitnesses) == 1.0:
            break
        next_population = []
        for _ in range(pop_size // 2):
            parents = select_parents(population, fitnesses, 2)
            child1, child2 = crossover(parents[0], parents[1])
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_population.extend([child1, child2])
        population = next_population
    best_individual = max(population, key=lambda ind: evaluate_individual(grid, ind, start, goal , nrows, ncols))
    return best_individual
