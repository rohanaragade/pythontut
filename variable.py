x=4 # global variabl

def add():
    y=9   # local variable
    global x       
    x=5        # local variable
    print('y=',y)  
    print('x=',x)

add()
print('x=',x)
# print(y)
