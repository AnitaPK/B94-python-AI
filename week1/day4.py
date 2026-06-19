# function in python 

# file handling

# write file 
# read file 

# a function is a block of code that perform specific task. 

def greeting():
    print("Welcome to python....")

greeting()

def addition():
    print(2+3)

addition()

def greetWithPara(name):
    print("Welcome", name)

greetWithPara("Rahul")

def additionOf2 (n1, n2):
    print(n1+n2)

additionOf2(10,20)

def additionWithReturn(n1,n2):
    return n1+n2

add = additionWithReturn(20,30)
print(add)

# create function for CalculateBill price and quantity 

def CalculateBill(price,quantity):
    return price*quantity

billAmount = CalculateBill(1000,2)
print(billAmount,"for 2 products whose price is 1000")

# create function for loginCheck input username and password 

# if success = "Login Successful"
# in not = "Invalid Credentials"

def loginCheck(username, password):
    if(username == 'admin' and password == 'admin@123'):
        return "Login Successful"
    return "Invalid Credentials"

print(loginCheck("dfgh", "987fgyu"))
print(loginCheck("admin", "admin@123"))

# create function to find largest of given thre number 
def findLargest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b 
    else:
        return c



# not allowed code
# def findlargest(n1,n2,n3):
#     if n1>n2:
#         return n1
#     elif n2>n3:
#         return n2
#     else:
#         return n3
# print(findlargest(10,20,30))  
# print(findlargest(10,30,20))  
# print(findlargest(20,10,30))  
# print(findlargest(20,30,10))  
# print(findlargest(30,20,10))  
# print(findlargest(30,10,20))

print("-----------------")
print(findLargest(10,20,30))  
print(findLargest(10,30,20))  
print(findLargest(20,10,30))  
print(findLargest(20,30,10))  
print(findLargest(30,20,10))  
print(findLargest(30,10,20))

# create function calculateDiscount 

# if Amount > 5000 20%
# if Amount >10000 40%

def calculateDiscount(amount):
    if(amount > 5000 and amount <10000):
        return amount - amount*20/100
    elif(amount > 10000):
        return amount - amount*40/100
    else:
        return amount

print(calculateDiscount(500))
print(calculateDiscount(6000))
print(calculateDiscount(11000))

# create function getOffer() 
# no offer  200 month
# Extra 5GB  1000 3months
# Netflix Subcription  7000 12months 

# regAMT = 

def getoffer(recharge,month):
    if(recharge>7000 and month == 12 ):
        return "congrast u got Free Netflix"  
    elif(recharge>1000 and month == 3):
        return "congrast u got free Extra 5GB "
    else:
        return"No offer 4 u :)"  
   
print(getoffer(10000,12))

# file Handling  allowes us to store data permantly 

# read - > if Exist 
# write -> create new file
# append -> add new data in existing

# file = open("data.txt", "w")
# file.write("Hello b94 ")
# file.close() 

# file1 = open("data.txt" , "r")
# content = file1.read()
# print(content)
# file1.close()


# file2 = open('data.txt', "a")
# file2.write("\nThis is last line....")
# file2.close()

with open("data.txt", "r") as file3:
    print(file3.read())

note = input("Enter note: ")
with open("myNotes.txt", "a") as file4:
    file4.write(note + "\n")
