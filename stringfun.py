a="rohan aragade"
print(len(a))           # 1
print(a.capitalize())    # 2
print(a)

a="rohan aragade"
for i in range(0,len(a)):
    print(a[i],end="")


a="rohan aragade"
for i in a:
    print(i,end="")

# FIND FUNCTON    STR.FIND()                      # 3
                                             
j="rohan aragade is student at dypcet"
k="at"                                           
print(j.find(k,0,len(j)-1))

j=input("enter the string:")
k=input("enter the string you want get its index no:")
print(j.find(k,0,len(j)-1))


l="rohan123" 
print(l.isalnum())     # 4
print(l.isdigit())     # 5
print(l.isspace())     # 6

l="123"
print(l.isalnum())
print(l.isdigit())
print(l.isspace())

l=" "
print(l.isalnum())
print(l.isdigit())
print(l.isspace())