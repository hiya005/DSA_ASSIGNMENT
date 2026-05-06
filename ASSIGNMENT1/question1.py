# Factorial using simple recursion(naive approach)
def fact_naive(num: int) -> int:
    if num <= 1:
        return 1
    else:
        return num * fact_naive(num-1)
    
# Factorial using caching (memoization)
def fact_memo(num:int) -> int:
    global fact_list
    if fact_list[num] != -1: 
        return fact_list[num]
    elif num <= 1: 
        return 1
    else:
        fact_list[num] = num * fact_memo(num-1)
        return fact_list[num]


# Fibonacci using simple recursion (naive approach)
def fibo_naive(num: int) -> int:
    if num <= 1:
        return num
    else:
        return fibo_naive(num-1) + fibo_naive(num-2)
    

# Fibonacci using caching (memoization)
def fibo_memo(num:int) -> int:
    global fibo_list
    if fibo_list[num] != -1: 
        return fibo_list[num]
    elif num <= 1: 
        fibo_list[num] = num
        return num
    else:
        fibo_list[num] = fibo_memo(num-1) + fibo_memo(num-2)
        return fibo_list[num]

# Empty lists to store the results
fact_list = []
fibo_list = []

# Main method
def main():
    global fact_list
    global fibo_list
    
    # Input
    num = int(input("Enter a positive number: "))
    
    # Input Validation
    while (num < 0):
        num = int(input("Error, Enter a positive number: "))
    
    # Initialise lists
    fibo_list = [-1] * (num+1)
    fact_list = [-1] * (num+1)
    
    # Print Factorial and Fibonacci
    print(f"Factorial of {num} using naive approach is {fact_naive(num)}")
    print(f"Factorial of {num} using memoized approach is {fact_memo(num)}")
    print(f"Fibonacci term at {num} using naive approach is {fibo_naive(num)}")
    print(f"Fibonacci term at {num} using memoized approach is {fibo_memo(num)}")

if __name__ == "__main__":
    main()