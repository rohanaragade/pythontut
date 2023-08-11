dict={'clg':'dyp','place':'kolhapur','since':1983}
print(dict)
print("length of dict is:",len(dict))

print("remove element is: ",dict.pop('since'))
print(dict)

dict={'clg':'dyp','place':'kolhapur','since':1983}
print("remove element is: ",dict.popitem())
print(dict)

dict={'clg':'dyp','place':'kolhapur','since':1983}
del dict['clg']
print(dict)

dict={'clg':'dyp','place':'kolhapur','since':1983}
print(dict.clear())
print(dict)

# del dict
# print(dict)