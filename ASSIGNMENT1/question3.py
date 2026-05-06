# Function to solve Tower of hanoi
def solve_hanoi(disks, start, helper, end):
    if disks == 1:
        print(f"Move disk 1 from {start} to {end}")
        return 1
    
    # Move top disks-1 to helper
    moves_first = solve_hanoi(disks - 1, start, end, helper)
    
    # Move largest disk to destination
    print(f"Move disk {disks} from {start} to {end}")
    
    # Move disks-1 from helper to destination
    moves_second = solve_hanoi(disks - 1, helper, start, end)
    
    return moves_first + 1 + moves_second

# Time: O(2^n) → Each call makes two recursive calls
# Space: O(n) → Recursion depth equals number of disks

# main method
def run():
    disks = 3
    print(f"Steps for {disks} disks:")
    total = solve_hanoi(disks, 'A', 'B', 'C')
    print(f"Total moves required: {total}")


if __name__ == "__main__":
    run()