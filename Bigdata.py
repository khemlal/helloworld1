# # def sum_thrice(x,y,z):
# #     sum = x+y+z
# #     if x == y ==z:
# #         sum = sum*3
# #     return sum
# # print(sum_thrice(1,2,3))
# # print(sum_thrice(3,3,3))
# #
# # print(" Hello World")
# #
# # x= 5
# # print(x)
# # print(type(x))
# #
# # y = 4.5
# # print(y)
# # print(type(y))
# # Print statement for single line
# """
# This is sample print statement as an example. (multiline comments)
# """
# z = " Dallas"
# print(z)
# print(type(z))
#
# #bullioan: True or False ( it is case sensative)
# b = True
# print(b)
# print(type(b))
# # Above mentioned are the primitive data type.
# #  Convert one type to other:
# x = 5
# y = 4.5
# f = int(y) # from 4.5 int gets only 4.
# print(f)
# print("Converted values is", f, ".")
# print(float(x))
#
# l= 1234567
# print(str(l))
# s ="12345678"
# print(int(s))
# s ="12345678"+"5" # it is added as a string as concatination  not int.
# print(s)
#
fruits = ["apple","banana","mango"]
# # print("total items in fruits list is", len(fruits))
# # print(fruits.index("apple"))
# # print(fruits[0], fruits[1])
# # print(fruits[0,2])
# # Insert in the adding list.
# # fruits.insert(3,"strawberry")
# # print(fruits[3])
# # pop by the index and remove by the name is.remove
# fruits.pop[0]
#
# #append in the end of the list.
#
# fruits.append("coconut")
# print(fruits)
#
# for i in fruits:
#     print(i)
#
#
# print(fruits[-1])
# for x in fruits:
#     print(x)
# if "kiwi" in fruits:
#     print("Yes print it, I want to eat apple")
# else:
#     print("no kiwi in the list")
# TUPLE EXERCISE:
"""
thistuple = ("apple", "banana", "mango", "mango")
# print(thistuple)
# for x in thistuple:
#     print(x)
# if "apple" in thistuple:
#     print("Apple is there")
# else:
#     print("Apple is not there")
print(thistuple[2])# it has only two method, count and index.
print(thistuple.count("mango"))
print(thistuple.index("mango"))
"""
# students = {
#     "John": 9,
#     "Paul": 10,
#     "Marry":12,
#
# }
# print(students)
# print(students.keys())
# print(students.values())
# print(students.items())
#
# # students.pop("John")
# print(students)
# print(students.get("Marry")) # it is the value of key.
# students["Kyle"]=11
# print(students)
# for i in students: # it print the values of key not value.
#     print(i)
#     print(students[i]) #  it will give the values of the dictionary.
#
#     print(students["John"])
# if"John" in students:
#     print("yes, John is in")
#
#
# # STRING METHODS/FUNCTIONS.
#
# s1= "dallas"
# s2 = "tx"
# s3 = "I live in dallas"
# s4 = "My adddress is 765 John drive arrolton, TX, 87654"
# print(s1.upper())
# print(s1,",", s2)
# print(s1 + s2)
# print(s3.split(" "))
# print(type(s3.split()))
# l= s3.split(" ")# once we do the spilit then we can use it for  for, while loop and others.
# for x in l:
#     print(x)
# print(s3.isalpha())
# # print(s1.isalpha())
# # print(s3.isalphanum())
# # print(s4.isalpha())
# print(s4.replae("my", "your", 3)) # practice the every methods.
#
# x=10
# y=20
# z=x+y
# print(z)
# print(y-x)
# print(y/x)
# print(int("20")*x)
#
# print(34%10)
# print(3**2)
#Conditional turorial: if/else, trure/false
# x=3
# if x%2==0:
#     print("x is divisiable by 2")
# elif x%5 ==0:
#     print("x is divisible by 5")
# else:
#     print("others")
# # testing two files:
#
# x=50
# if x%2==0  and x%5==0:
#     print("x is divisiable by 2")
# elif x%5 ==0: # elif needs condition to test:
#     print("x is divisible by 5")
# else:
#     print("others")
# l=[2,5, 10]
# var =5
# if var in l:
#     print(var, "is in list")
# x=3
#
# print("divisible") if x%2==0 else print("non-divisible"):# know this for compact coding.
# x=9
# if x>10:
#     if x<100:
#         print(x,"in between 10 and 100")
#     else:
#         print(x,"outside 10 and 100")
# else:
#     print(x, "is smaller than 10")

# above mentioned code for Nested if:
# know comparision of string:



## control Loop:
# while and for loop:
# break and continue, # increment the value. # continue does the skip # know the collection:
"""
fruits=["apple","banana", "mango", "coconut"]
for y in fruits:
    if(y=="banana"):
        continue
    print(y)
else:
    print("all fruits printed")
adj =["red",  "big", "tasty"]
fruits=["a[ple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        if y=="banana":
            continue
        print(x, y)
"""


#
# def print_name():
#     print("My name is John")
# def print_address():
#     print("7673 dole bird dallas")
#
# print_name()
# print_address()

# def print_name(emp):
#     print("My name is: name")
# def print_address(addr):
#     print("7673 dole bird dallas")
#
# emp=["John","paul","mary"]
# addr=["dallas, tx", "austin, tx", "hosuton, tx"]
# for x, y in zip(emp, addr):
#     print_name(x)
#     print_address(y)

# learn this it is good to know., we can pass the whole list object. in this case for loop does not work.
# print("hello world")
# first_name= ("Khem", "Johh")
# last_name =("kadel", "Roobert")


# def calculate(a, b): # we can have the defult vaule or we can override.
#     return(a+b)
# x=10
# y=30
# result =calculate(x,y)
# print(result)


# def print_kids(*kids)
#     print(kids[0])
# print_kids("john", "Paul","mary") # know this for parameter.

#Function: know this in details:

def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def subtract(a,b):

    def main():
        x=30
        y=10

addresult = add(x,y)
multiplyresult = multiply(x,y)
subtractresult = subtract(x,y)
divideresult = divide(x,y)
printvalues(addresult,subtractresult,multiplyresult,divideresult)

if __name__ == "__main__": main()
