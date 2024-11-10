num = [1,2,3,4,5,6,7,8]
num.reverse()
count=[]
even = []

for i in num:
    if i%2==0:
        count.append(i)
    else:
        even.append(i)
print(count)
print(even)