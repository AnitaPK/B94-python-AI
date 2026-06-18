# * * *
# * * *
# * * *

for i in range(3):
    print("* * *")

for i in range(3):
    line = ''
    for j in range(3):
        line += ' *'
    print(line)

# *
# * *
# * * * 

for i in range(1,4):
    print("* " * i)

# 1. create a program for sum of numbers 
# eg number is 123456 means range(1,7)

# 2. Restorent Order System 
# Input Number of orders 
# Loop should ask : Food Name and price 
# Display total bill

# 3. E-Commerce Cart 
# Input : How many Products?
# Loop should  ask Product Name and price 
# Calculate total cart Amount

# 4. ATM Retry System 
# Allow user maximum 3 attempts.
# Correct PIN:   1234 
# Display: Access Granded OR Card Blocked

# 5. a. Count digits in given number 
#    b. Reverse a given number

num = int(input("Enter number"))

count = 0 

while num >0 :
    count += 1
    num = num // 10
print("length of number ", count)

1234
123 

reverse = 0    
while num >0 :
    digit = num % 10 
    reverse = reverse*10 + digit
    num = num // 10     1
print(reverse)