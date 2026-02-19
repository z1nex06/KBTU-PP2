import sys

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i

def main():
    line = sys.stdin.read().strip()
    if not line:
        return
    
    try:
        n = int(line)
        gen = prime_generator(n)
        
        try:
            first = next(gen)
            print(first, end='')
        except StopIteration:
            return

        for prime in gen:
            print(f" {prime}", end='')
        print()
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()