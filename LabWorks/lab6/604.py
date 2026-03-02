import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    b = list(map(int, input_data[n+1:2*n+1]))
    
    dot_product = sum(x * y for x, y in zip(a, b))
    print(dot_product)

if __name__ == "__main__":
    solve()