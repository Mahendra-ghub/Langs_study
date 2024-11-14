Name = input("Enter your name : ")
Age = int(input("Enter your age:"))

yearsto50 = 50-Age

if yearsto50>0:
    print(f"hello {Name}. You will be 50 in {yearsto50} years.")
else:
    print(f"{Name}. You are 50 at {-yearsto50} years ago.")
print("Bye!")