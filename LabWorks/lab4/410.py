import sys

def limited_cycle(elements, n):
    for _ in range(n):
        for item in elements:
            yield item

def main():
    input_data = sys.stdin.read().splitlines()
    if len(input_data) < 2:
        return
    
    elements = input_data[0].split()
    try:
        n = int(input_data[1].strip())
        
        gen = limited_cycle(elements, n)
        
        try:
            first = next(gen)
            print(first, end='')
        except StopIteration:
            return

        for item in gen:
            print(f" {item}", end='')
        print()
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()