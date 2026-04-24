import heapq
from warehouse_map import warehouse

def dijkstra(graph, start):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous

def get_path(previous, end):
    path = []
    while end:
        path.insert(0, end)
        end = previous.get(end)
    return path

distances, previous = dijkstra(warehouse, "Start")
path = get_path(previous, "End")

print("Shortest Distance:", distances["End"])
print("Optimal Path:", " -> ".join(path))
