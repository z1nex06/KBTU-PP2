r = input()

for i in r:
    if int(i) % 2 != 0: 
        print("Not valid")
        break
else:
    print("Valid")