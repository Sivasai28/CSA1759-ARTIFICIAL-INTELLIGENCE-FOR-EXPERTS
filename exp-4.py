from itertools import permutations

def solve_cryptarithm():
    # The unique letters in the problem
    letters = "SENDMORY"
    
    # Generate all permutations of the digits 0-9 for the 8 letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        
        # Ensure that 'S' and 'M' are not zero, as they are leading digits
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        
        # Compute SEND, MORE, and MONEY based on the mapping
        send = 1000 * mapping['S'] + 100 * mapping['E'] + 10 * mapping['N'] + mapping['D']
        more = 1000 * mapping['M'] + 100 * mapping['O'] + 10 * mapping['R'] + mapping['E']
        money = 10000 * mapping['M'] + 1000 * mapping['O'] + 100 * mapping['N'] + 10 * mapping['E'] + mapping['Y']
        
        # Check if the equation SEND + MORE = MONEY holds
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            print("Mapping:", mapping)
            return

    print("No solution found.")

# Call the function
solve_cryptarithm()
