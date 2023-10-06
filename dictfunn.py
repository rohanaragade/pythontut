dict1={'Brand':'Toyota','Model':'Fortuner','Year':2009}
x=dict1.copy()
print(x)

i=('firstkey','secondkey','thirdkey')
j=1
dict=dict.fromkeys(i,j)
print(dict)

dict1={'Brand':'Toyota','Model':'Fortuner','Year':2009}
print(dict1.setdefault('Brand','Porsche'))
print(dict1.setdefault('Color','Black'))
print(dict1)

print(dict1.update({'Varient':'Sigma 4'}))
dict1['price']=5000000
print(dict1)