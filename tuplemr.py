import sys
list1=[1,2,3,"rohan","dyp"]
tuple1=(1,2,3,"rohan","dyp")
print("size of list is: ",sys.getsizeof(list1))
print("size of tuple is: ",sys.getsizeof(tuple1))

import timeit
listtime=timeit.timeit(stmt="[1,2,3,4,5,6]",number=100000)
tupletime=timeit.timeit(stmt="(1,2,3,4,5,6)",number=100000)
print("time take by  list is: ",listtime)
print("time take by tuple is: ",tupletime)


