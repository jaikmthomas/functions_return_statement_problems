#Write a function called calculation() that takes in 2 integers, a and b, and a sign (which will be a string -- either "+" or "-"). If the sign is "+" return the sum of a and b. Otherwise, if the sign is "-", return a - b.
def calculation(int1,int2,sign):
    if sign == str("+") :
        return int1 + int2
    elif sign == str("-"):
        return int1 - int2

#Create a function called showEmployee() such that it should accept an employee name and salary and print both of them out.
def showEmployee(name,salary):
     print("Employee"+" "+ name+" salary is "+ salary)

