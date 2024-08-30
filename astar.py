import heapq

def initialize_astar(graph, start, goal):
    open_set = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    return open_set, came_from, cost_so_far

def step_astar(graph, open_set, came_from, cost_so_far, goal):
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    if open_set:
        curr_cost, curr_node = heapq.heappop(open_set)
        if curr_node == goal:
            return curr_node
        for neighbor in graph[curr_node]:
            new_cost = cost_so_far[curr_node] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_set, (priority, neighbor))
                came_from[neighbor] = curr_node
        return curr_node
    return None

def rebuild_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    path.reverse()
    return path
