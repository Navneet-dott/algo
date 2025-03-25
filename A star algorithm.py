import heapq

# Graph representation as an adjacency list
graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'C': 1, 'E': 7},
    'C': {'A': 1, 'B': 1, 'D': 5, 'E': 4},
    'D': {'C': 5},
    'E': {'B': 7, 'C': 4, 'F': 5},
    'F': {'E': 5}
}

# Heuristic values (estimated distances to 'D')
heuristic = {'A': 6, 'B': 5, 'C': 3, 'D': 0, 'E': 2, 'F': 4}

def astar(graph, start, goal):
    open_list = []  # Priority queue
    heapq.heappush(open_list, (0, start))  # (f-score, node)
    
    came_from = {}  # Track path
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    while open_list:
        _, current = heapq.heappop(open_list)  # Node with lowest f-score
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse path order

        for neighbor, cost in graph[current].items():
            temp_g_score = g_score[current] + cost

            if temp_g_score < g_score[neighbor]:  # Found a better path
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

# Run A* on the graph
start, goal = 'A', 'D'
shortest_path = astar(graph, start, goal)

print("Shortest path:", shortest_path)

