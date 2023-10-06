a=int(input("enter a:"))
if a%2==0:
    print("no is even")
else: 
    print("no id odd")

age=int(input("enter age:"))
if age>18:
    print("you can vote")
elif age>15 and age<18:
    print("you canot vote")
else:
    print("you are too small")