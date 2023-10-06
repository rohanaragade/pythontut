r=input("enter your name:")
vowel=0
con=0
for i in range(len(r)):
    if(r[i]!=" "):
        if(r[i]=='a' or r[i]=='e' or r[i]=='i' or r[i]=='o' or r[i]=='u' or r[i]=='A' or r[i]=='E' or r[i]=='O' or r[i]=='I' or r[i]=='U'):
            vowel+=1
        else:
            con+=1
print("vowels are:",vowel)
print("consonent are:",con)