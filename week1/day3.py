# loops 
# for loop 
# while loop 
# break continue 

# generate pattern 


# greeting Hello 100 times 

# loop is used to excute a block of code multple times 

# for loop 

# for varible in range():
#     statements 

for i in range(10): # 0-9
    print("Hello")
    print(i)

for i in range(1, 11):
    print(i)
print("------------------")
for i in range(1, 11, 3):
    print(i)

num = int(input("Enter a number : "))
for i in range(1, 11):
    print(num * i)

# iterations  num   i    print 
# 1st         5.    1.    5
# 2nd         5.    2.    10 
# 3rd         5.    3.    15
# 4th
# 5th
# 6th 
# 8th 
# 9th         5.     9.   45
# 10th        5.    10.   50
# 11th        5.    11

# while loop 

# white condition:
#     statements 
print("------------------")

count = 1

while count <=5:
    print(count)
    count += 1
print("------------------")

password = ''
while password != "genAI":
    password = input("Enter password : ")
print("Login Successfull")

for i in range(1,11):
    if i == 5:
        break
    print(i)

for i in range(1,11):
    if i == 5:
        continue
    print(i)

for i in range(3):
    for j in range(3):
        print("*")