x = int(input("enter first digit:"))
y = int(input("enter second digit:"))

temp = x
x = y
y = temp

print("print x after swapping:{}".format(x))
print("print y after swapping:{}".format(y))