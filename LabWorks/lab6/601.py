import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = list(map(int, input_data[1:n+1]))
    
    squared_numbers = map(lambda x: x**2, numbers)
    print(sum(squared_numbers))

if __name__ == "__main__":
    solve()