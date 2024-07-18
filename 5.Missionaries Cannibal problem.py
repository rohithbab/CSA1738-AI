from collections import deque

def is_valid_state(missionaries_left, cannibals_left, boat_left):
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left
    if missionaries_left < 0 or missionaries_right < 0 or cannibals_left < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def get_next_states(state):
    missionaries_left, cannibals_left, boat_left = state
    moves = []
    if boat_left:
        new_states = [
            (missionaries_left - 2, cannibals_left, not boat_left),
            (missionaries_left, cannibals_left - 2, not boat_left),
            (missionaries_left - 1, cannibals_left - 1, not boat_left),
            (missionaries_left - 1, cannibals_left, not boat_left),
            (missionaries_left, cannibals_left - 1, not boat_left),
        ]
    else:
        new_states = [
            (missionaries_left + 2, cannibals_left, not boat_left),
            (missionaries_left, cannibals_left + 2, not boat_left),
            (missionaries_left + 1, cannibals_left + 1, not boat_left),
            (missionaries_left + 1, cannibals_left, not boat_left),
            (missionaries_left, cannibals_left + 1, not boat_left),
        ]
    for new_state in new_states:
        if is_valid_state(*new_state):
            moves.append(new_state)
    return moves

def solve_missionaries_cannibals():
    start_state = (3, 3, True)
    goal_state = (0, 0, False)
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        if current_state in visited:
            continue

        visited.add(current_state)
        path.append(current_state)

        if current_state == goal_state:
            return path

        for next_state in get_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path.copy()))

    return None

def print_solution(solution):
    if solution:
        for step in solution:
            missionaries_left, cannibals_left, boat_left = step
            boat_position = "left" if boat_left else "right"
            print(f"Missionaries: {missionaries_left}, Cannibals: {cannibals_left}, Boat: {boat_position}")
    else:
        print("No solution found")

# Example usage
solution = solve_missionaries_cannibals()
print_solution(solution)
