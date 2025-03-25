import heapq

def dijkstra(graph, start):
    # Initialize priority queue
    queue = []
    heapq.heappush(queue, (0, start))  # (cost, node)
    
    # Initialize distances
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Track paths
    previous_nodes = {node: None for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

# Graph representation
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'E': 3},
    'C': {'A': 2, 'B': 1, 'D': 5, 'E': 8},
    'D': {'C': 5, 'F': 6},
    'E': {'B': 3, 'C': 8, 'F': 6},
    'F': {'D': 6, 'E': 6}
}

# Running Dijkstra’s Algorithm
start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

# Print shortest path to each node
for node, distance in distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")
