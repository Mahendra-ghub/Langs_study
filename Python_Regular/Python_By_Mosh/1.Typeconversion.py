Birth_Year = input("Year born: ")
age = 2024 - int(Birth_Year)
print(age)

#single line commment
print('Python for "Beginners"')
print("python's for Beginers:")
print('''Python is 
      for all Beginners''')

#index management
course = ("Python Beginners")
print(course[1])
print(course[-1])
print(course[0:3])
print(course[1:-1])

#string cancetination
first = "john"
last = "smith"
print(f"{first} {last} is a coder")

#string methods
course = ("Python Beginners")
print(len(course))

#methods --belongs to specific object called methods
course = ("Python Beginners")
print(course.upper()) #upper specific to strings here where as len and print not specific to single things like int str;
print(course.lower())
print(course.find('P')) #prints index of that index if no givven letter displays -1, This are case sensitive
print(course.replace("Beginners", "Absolute Beginners"))
print("Python" in course) #find word in string using in operator, the dif of find  and in is---find gives index num, where in gives boolean value

#arthametic operations
x = 10
x += 20    #+=is argumented assgnment opeartor
print(x)

#paranthesis>Expenential>Divison>multiplication>sub>addition
x = (2+3)-3**5
print(x)

#math functions
x = 9.5
print(round(x))  #1-4 is last number and .5 above next number

#math module same like method works on numbers
import math
x = 2.9
print(math.ceil(x))
print(math.floor(x))

#if statement
is_hot = True
is_cold = True
if is_hot:
    print("Take plenty of water")
elif is_cold:
    print("wear winter waer")
else:
    print("its a good day")
print("bye!")

#Downpayment question
has_credit_good = True
Price = 100000
if has_credit_good:
    down_payment = 0.1 * Price
else:
    down_payment = 0.2* Price
print(f"The downpayment:{down_payment}")

#logical operator and, or
has_good_credit = True
has_salary = True
if has_good_credit and has_salary:
    print("Eligible to loan")
    print("Congrats")
print("visit again")

has_good_credit = True  #or operator
has_salary = False
if has_good_credit or has_salary:
    print("Eligible to loan")
    print("Congrats")
print("welcome")

has_good_credit = True  #not operator
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("eligible to loan")
print("thnk you")

#> ,==, < opeartors
temperature = 20
if temperature > 20:
    print("it's hot day")
elif temperature == 20:
    print("it's moderate day")
else:
    print("it's cold day")
print("enjoy day")

#weight converter
weight = int(input("weight is:"))
unit = input(str("K for kilos and L for pounds:"))
if unit.upper() == "K":
    converter = weight * 0.45
    print(f"Your weight is {converter} kilos.")
else:
    converter = weight/0.45
    print(f"Your weight is {converter} pounds.")

#while loop
i = 1
while i<=5:
    print('*' * i)
    i = i+1
print('Done!')

#guess game
secret_number = 10
guess_limit = 3
guess_count = 1
while guess_count<=guess_limit:
    guess = int(input("Enter a guess:"))
    guess_count = guess_count+1
    if guess == secret_number:
        print("congraculation your guess is correct!")
        break
else:
    print("sorry your guess limit exceed! you failed to guess")

#car game
command = ""
started = False
while command != 'quit':
    command = str(input(">").lower())
    if command == 'start':
        if not started:
            print("car is already started")
        print("you are ready to go.")
    elif command == 'stop':
        if started:
            print("car is already stopped")
        print("car has stopped!")
    elif command == 'help':
        print(''' start for start car
              stop for stop car
              help for hrlping
              quit to exit
              ''')
    else:
        print("game over")
print("close!")

#for loop iterate each character in string
for item in "python":    #string loop
    print(item)
for item in ["Mani", "Taj","upi"]:    #list loop
    print(item)
for item in range(10):    #range fun
    print(item)
for item in range(5,10,2):
    print(item)

#list looping
prices = [10,20,30]
total = 0
for i in prices:
    total = total+i
print(total)

#nested loops to create x and y axis:
for x in range(5):          #1st iteration 0
    for y in range(5):      #1st iteration 0 and print(0,0)and then next iteration 1 and then print (0,1),(0,2)(0,3)(0,4) then moves to 1st x axis again
        print(f"{x},{y}")   #2nd nested x axis 1 and then 1st iteration of y (1,0)(1,1)(1,2)(1,3)(1,4)
                            
#nested problm
for x in range(4):
    for y in range(2):
        for z in range(1):
            print(f"{x}{y}{z}")

#nested loop problem
numbers = [5,2,2,5]
for i in numbers:
    output =""
    for z in range(i):
        output += 'x'
    print(output)

#lists
names = ["mahi","mani","taj","kissan"]
print(names[0])
print(names[-1])

#largest number in list
numbers = [10,2,5,38]
max_num = numbers[0]
for i in numbers:
    if i > max_num:
        max_num = i
        print(max_num)

#2D matrix                  outer squarebarckets and inide that another brackets
matrix = [
    [1,3,5],
    [2,4,7],
    [3,7,9]
]
print(matrix[0][1])
matrix[0][2]=2
print(matrix[0][2])

#2d print using loop
matrix = [
    [1,3,5],
    [2,4,7],
    [3,7,9]
]
for i in matrix:
    for j in i:
        print(j)

#list methods/functions
numbers =  [2,5,2,7,8]
numbers.append(10)  #add at last
numbers.insert(0,20) #insert at specific positin
numbers.remove(5)  #remove at any index
#numbers.clear()   #remove all
numbers.pop()  #remve last item
print(10 in numbers)
print(numbers.count(5))
numbers.sort()  #sort numbers
numbers.reverse() #reverse numbers
number2= numbers.copy() #copy of original list
print(numbers)
print(number2)

#remove duplicates in  list
numbers = [2,3,5,2,6,7,6]
unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)

#tuples ordered unchangable allow duplicates
numbers = (1,2,3,4)
numbers.index(1)       #index,count is available in list
print(numbers)

#unpacked numbers
coordinates = (1,4,5,6)
x,y,z,w = coordinates
print(x,y,z,w)
