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