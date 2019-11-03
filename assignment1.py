print("Hello World")

def main():
    print("Hello World")
if __name__== "__main__":
    print("Khem")
#asignemnt1.py
"""
x = 20
y = 25
z = x + y
print(z)


x = 20
y = 25
z = x * y
print(z)

print(30 % 7 )

print(5**3)


# assign2.py
#b
fname = "Khem"
lname = "Kadel"

print("My name is " + fname + lname + ".")
#C- Get the first 4 letter of your first name:

print(fname[0:4])
print(fname[:4])
print(fname.capitalize() + " " + lname.capitalize())
print(fname.upper() + " " + lname.upper())
print(fname.lower() + " " + lname.lower())


# d. Work  on the list collection objects:

mylist = [10, 20, 30, 40, 50]
# print(len(mylist))
for x in mylist:
    print(x)
    print(x**2)
mylist.append(60)
print(mylist)
mylist.remove(20)
print(mylist)


# Work on the dictionary objects:
employee_salary = {
    "John": 4500,
    "Paul": 5000,
    "Mary": 6000,
    "Dave": 5500
}
print(employee_salary)
for x, y in employee_salary.items():
    print(x, y)
for x in employee_salary.keys():
    print(x)
for x in employee_salary.values():
    print(x)
for x in employee_salary:
    print(x)
for x in employee_salary:
    print(employee_salary[x])
for x in employee_salary:
    print(x + "'s salary is" + " " + str(employee_salary[x]))

# adding in a dictionary:

employee_salary["Judith"] = 5600
print(employee_salary)


# If/Else statement:
a = 50
b = 100
if b > a:
    print(b)
if a < b:
    print(a)
if a == b:
    print("They are equal")
else:
    print("They are different")


#Loop

fname = "Khem"
for x in fname:
    print(x)

mylist = ["Orange", "Apple", "Mango","Pinnaple", "Pear"]
for x in mylist:
    print(x)


i = 10
while i > -1:
    print(i)
    i -= 1

# Functions:
def add(a, b):

    return a+b

def main():
    a = 30
    b = 20

    addresult = add(a, b)
    print(addresult)


if __name__ == "_main_":
    main()

#
def concat(fname, lname):
    return fname + lname

def main():
    fname = "Khem"
    lname = "Kadel"

    concatresult = concat(fname, lname)
    print(concatresult)

if __name__ == "_main_":
    main()

"""

# Try except block:
def concat(fname, lname):
    return fname + lname

def main():
    fname = "Khem"
    lname = "Kadel"

    concatresult = concat(fname, lname)
    try:
        print(concatresult)
    except:
        print("An Error occurred")


if __name__ == "_main_":
    main()