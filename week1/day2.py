# Conditions & Loops

# make the decisions 
# if , if-else, elif , nested if  

# if condition:
#     statement

# age =int(input("Enter age : "))
age =19
if age >= 18:
    print("You can vote")
else:
    print("You cant vote")

# check age >18 and nationality="indian" for driving liences 
age = 20; nationality = "Indian"
if(age > 18 and nationality == "Indian"):
    print("allowed for driving liences")
else:
    print("Not allowed")

# marks < 40 fail F
# marks >40 and Marks <60. pass C
# marks> 60 and marks <75 second class B
# marks >75 and marks <100 first class A

marks = int(input("Enter marks"))
if(marks >= 0 and marks <=100):
    if(marks < 40):
        print("Fail")
    elif(marks >40 and marks <60):
        print("Pass Grade C")
    elif (marks> 60 and marks <75) :
        print("Pass with second class Grade B")
    else :
        print("Pass with First class Grade A")
else:
    print("Invalid")




# 1. find even or odd 
num1 = int(input("Enter number to check odd or even"))
if(num1 % 2 == 0):
    print("Even Number")
else:
    print("Odd Number")

# 2. find largest of given two numbers 

n1 = int(input("Enter first number"))
n2 = int(input("Enter first number"))
if(n1 > n2):
    print("first number is greater")
else:
    print("second number is greater")

# 3. login validation take username and password from user compare 
# with "admin" as user name and "admin@123" as password 

uName = input("enter Name")
password = input("Enter password")
if(uName == "admin" and password = "admin@123"):
    print("Logged in successfully")
else:
    print("Invalid credentials")

# 4. check divisible by 5
num2 = int(input("Enter to chech divisible by 5"))
if(num2 % 5 == 0):
    print("Divisible by 5")

5. check leap Year

year = int(input("Enter year to check leap year"))
if(year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

6. Electricity Bill Discount if Bill is greater than 5000 apply 10% discount 




7. Pizza Billing System 
pizza type : 1. veg pizza = $200 
              2. nonveg  = $500
if quantity  is greater than 5 add discount 10%

find 
Total Bill 
Discount 
Final Bill

8. Movie Ticket pricing 
by age 

condition 
1. Below 12 --> $100
2. 12-59 --> $200
3. 60+ $150 

Display ticket price 

9. Cab Fare calculation 
input distance 
condition 0-5km --> $100 
          6-10km --> $200
          above 10km -> $300
output calculate fare

10. Food delivery app discount 
Order Amount 
Membership(yes / no )

condition 
    1. Member + order > 1000
        20%
    2. Member + order > 500 
        10%
    3. Non-Member + order > 2000
        5%
    4. otherwise
       no discount