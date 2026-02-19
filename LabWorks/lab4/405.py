import sys

def countdown_generator(n):
    for i in range(n, -1, -1):
        yield i

def main():
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        n = int(line.strip())
        for num in countdown_generator(n):
            print(num)
    except ValueError:
        pass

if __name__ == "__main__":
    main()