exp = []
stopped = False

while not stopped:
    num = int(input("Enter a expenditure (stop when 0):"))
    if num != 0:
        exp.append(num)
    else:
        stopped = True
print(f"the expenditure List is {sorted(exp)}")
print(f"Length of exp:{len(exp)}")

print(f"total expenses: {sum(exp)}")
print(f"add sum extra expenses:{exp.extend([12,34,56])}")
print(f"extended total expenses:{exp}")
print(f"sorted one: {sorted(exp)}")
