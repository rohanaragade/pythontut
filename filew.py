f=open('ro.txt','w')
text=f.write("hello python its rohan")
f.close()

f=open('ro.txt','w')
text=f.write("ro")
f.close()

f=open('ro.txt','a')
text=f.write("\nhello python its rohan\n")
f.close()

with open('ro.txt','a')as f:
  f.write("hello python ")

