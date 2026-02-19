import sys

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    try:
        n = int(line)
        if n <= 0:
            return
            
        gen = fibonacci_generator(n)
        print(",".join(map(str, gen)))
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()