import sys

def powers_of_two(n):
    for i in range(n + 1):
        yield 2**i

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    try:
        n = int(line)
        gen = powers_of_two(n)
        
        try:
            first = next(gen)
            print(first, end='')
        except StopIteration:
            return

        for power in gen:
            print(f" {power}", end='')
        print()
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()