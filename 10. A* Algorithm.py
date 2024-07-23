import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Heuristic cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return f"Node(position: {self.position}, f: {self.f})"

def heuristic(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])  # Manhattan distance

def a_star(grid, start, goal):
    start_node = Node(start)
    goal_node = Node(goal)

    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [
            (0, -1),  # Up
            (0, 1),   # Down
            (-1, 0),  # Left
            (1, 0)    # Right
        ]

        for new_position in neighbors:
            node_position = (
                current_node.position[0] + new_position[0],
                current_node.position[1] + new_position[1]
            )

            if (node_position[0] < 0 or node_position[0] >= len(grid) or
                node_position[1] < 0 or node_position[1] >= len(grid[0])):
                continue

            if grid[node_position[0]][node_position[1]] != 0:
                continue

            neighbor = Node(node_position, current_node)

            if neighbor.position in closed_list:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal_node.position)
            neighbor.f = neighbor.g + neighbor.h

            if any(open_node.position == neighbor.position and open_node.f < neighbor.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor)

    return None

def print_grid(grid, path):
    for position in path:
        grid[position[0]][position[1]] = 'P'

    for row in grid:
        print(' '.join(str(cell) for cell in row))

if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0]
    ]
    start = (0, 0)
    goal = (4, 4)

    path = a_star(grid, start, goal)
    if path:
        print("Path found:", path)
        print_grid(grid, path)
    else:
        print("No path found")
