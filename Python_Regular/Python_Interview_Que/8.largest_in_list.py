'''numbers = [10,20,30,4,50]
largest = numbers[0]

for num in numbers:
    if num>largest:
        largest = num
print(f"the largest number is {largest}")'''

def largest_num(num):
    largest = num[0]
    for i in num:
        if i>largest:
            largest = i
    return largest

num = [10,20,40,70]
largest_value=largest_num(num)
print(f"this is largest {largest_value}")