total_sum = 0
num = int(input("enter a number"))

for i in range(1,num+1):
    result = num * i
    total_sum = total_sum+result
print(total_sum)