import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    numbers = list(map(int, input_data[1:n+1]))
    
    distinct_sorted = sorted(set(numbers))
    print(*(distinct_sorted))

if __name__ == "__main__":
    solve()