import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    words = input_data[1:n+1]
    
    result = [f"{i}:{word}" for i, word in enumerate(words)]
    print(" ".join(result))

if __name__ == "__main__":
    solve()