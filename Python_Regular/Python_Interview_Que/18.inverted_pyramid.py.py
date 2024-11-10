n=int(input("Eneter a number"))
for i in range(n):
    for j in range(i):
        print(end=" ")
    for j in range(0,n-i):
        print("*",end=" ")
    print()