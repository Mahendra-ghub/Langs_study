exp = -1
total = 0
maxexp = 0
minexp = 0

while exp!=0:
    exp = int(input("Eneter a expenditure: "))
    if exp==0:
        break
    total = total + exp
    if exp > maxexp:
        maxexp =exp
    if exp<minexp:
        minexp = exp
print(f"toatal expenditure is {total}")
print(f"maxexp is {maxexp}")
print(f"min exp is {minexp}")