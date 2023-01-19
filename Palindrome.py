str=input("Введите вашу строку, пожалуйста.\n\n")
str=str.lower()
str=str.replace(" ","")
str=str.replace(".","")
str=str.replace(",","")
str=str.replace(":","")
str=str.replace(";","")
str=str.replace("-","")
str=str.replace("!","")
str=str.replace("?","")
mirror_str=str[::-1]
if mirror_str==str:
    print("Эта строка есть палиндром")
else:
    print("Эта строка не есть палиндром")