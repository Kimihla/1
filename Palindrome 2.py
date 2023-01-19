str=input("Введите вашу строку, пожалуйста.\n\n")
str=str.lower()

tmp=''
count=0
for x in str:
    if x != '.' and x!=','and x != '?' and x!='!'and x != ':' and x!='-' and x!=' ':
        tmp=tmp+x
        count+=1

half_count=count//2+1
s=0
for i in range(0, half_count):
    if tmp[i]!=tmp[-1-i]:
        s+=1
        break

if s==0:
    print("Эта строка есть палиндром")
    
else:
    print("Эта строка не есть палиндром")