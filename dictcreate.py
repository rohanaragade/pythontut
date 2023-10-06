dict1={'Brand':'Toyota','Model':'Fortuner','Year':2009}
print(dict1)

print(dict1['Brand'])

x=dict1["Model"]
print(x)

print(dict1.get('Year'))

for i in dict1:
    print(i)

for i in dict1:
    print(dict1[i])

for i in dict1.values():
    print(i)

dict1['Model']='LC'
print(dict1)

for x,y in dict1.items():
    print(x,y)

dict={'age':21,'name':'rohan','height':160}
print(dict)
for j in dict.values():
    print(j)
print(dict.values())
print(dict.keys())
print(dict.items())
