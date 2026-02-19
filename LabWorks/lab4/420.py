import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n_commands = int(input_data[0])
    
    g = 0  # global
    n = 0  # nonlocal для inner
    
    idx = 1
    for _ in range(n_commands):
        scope = input_data[idx]
        val = int(input_data[idx + 1])
        
        if scope == 'global':
            g += val
        elif scope == 'nonlocal':
            n += val
        # case 'local' игнорируем, так как он не влияет на результат
        
        idx += 2
        
    print(f"{g} {n}")

if __name__ == "__main__":
    solve()