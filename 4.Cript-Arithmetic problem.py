from itertools import permutations

def solve_crypto_arithmetic():
    # Define the unique characters in the problem
    letters = 'SENDMORY'
    # Create all possible digit permutations
    for perm in permutations('0123456789', len(letters)):
        solution = dict(zip(letters, perm))
        # Check if leading characters are non-zero
        if solution['S'] == '0' or solution['M'] == '0':
            continue
        # Convert the words to their numeric equivalents
        send = int(''.join(solution[c] for c in 'SEND'))
        more = int(''.join(solution[c] for c in 'MORE'))
        money = int(''.join(solution[c] for c in 'MONEY'))
        # Check if the equation is satisfied
        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            print(solution)
            return solution

    print("No solution found")
    return None

# Example usage
solve_crypto_arithmetic()
