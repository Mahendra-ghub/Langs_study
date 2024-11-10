num = []
names = []
list = ["ram", 123, 456,789,"suresh","raju"]
for i in list:
    if type(i)== str:
        names.append(i)
    if type(i)==int:
        num.append(i)
print("seperation of names:",names,)
print("seperation of numbers:",num)



