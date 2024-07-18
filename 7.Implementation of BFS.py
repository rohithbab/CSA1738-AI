from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the start node

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            print(node, end=' ')  # Print the node or process it as needed
            visited.add(node)  # Mark the node as visited

            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    start_node = 'A'
    print("BFS traversal starting from node", start_node, ":")
    bfs(graph, start_node)
