dict={}
while(True):
    v=input("enter the id & name separted by comma or q for break:")
    if v=='q':
        break

id, name = dict.split(' , ')
dict.update({'id':'name'})

for i,j in dict.items():
    print(i,j)

