from collections import deque

# Define the possible movements: up, down, left, right
movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(x, y, grid):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != '#'

def bfs_vacuum_cleaner(start, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        # If we find a dirty spot, clean it
        if grid[x][y] == 'D':
            grid[x][y] = 'C'
            print(f"Cleaned: ({x}, {y}) in {steps} steps")

        # Check if all spots are cleaned
        if all(grid[i][j] != 'D' for i in range(rows) for j in range(cols)):
            print("All spots are cleaned")
            return steps

        # Explore the next possible moves
        for dx, dy in movements:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    print("Some spots could not be cleaned")
    return -1

def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()

# Example usage
grid = [
    ['D', 'D', 'D'],
    ['D', '#', 'D'],
    ['D', 'D', 'D']
]

start = (1, 0)  # Starting position of the vacuum cleaner
print("Initial grid:")
print_grid(grid)

steps = bfs_vacuum_cleaner(start, grid)

print("\nFinal grid:")
print_grid(grid)
print(f"Total steps taken: {steps}")
