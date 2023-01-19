import array
n=int(input ("Введите размер квадрата: n="))
print("")
signal=0
#создание двумерного массива
a=[[0 for i in range(n)] for j in range (n)]

for i in range (0, n):
    print("Числа {}-й строки:".format(i))
    for j in range(0,n):
        temp=int(input("a[{}][{}]=".format(i,j)))
#проверка на неповторяемость введенного числа
        for ii in range(0,i):
            for jj in range(0,n):
                if temp==a[ii][jj]:
                    signal=1
        if signal==0:
            for jj in range(0,j):
                if temp==a[i][jj]:
                    signal=1
        if signal==0:
            a[i][j]=temp
        else:
            print("No")
            break
    if signal==1:
        print("Повторение числа в таблице. Это точно не магический квадрат.")
        break          
#сумма чисел по диагонали
temp=0
s=0
if signal==0:
    for i in range (0, n):
        temp+=a[i][i]
#сумма чисел по другой диагонали
    s=0
    for i in range (0, n):
        s+=a[i][n-i-1]
if s!=temp:
    signal=1
#сумма чисел по каждой строке
else:
    for i in range (0, n):
        s=0
        for j in range(0,n):
            s+=a[i][j]
        if s!=temp:
            signal=1
            break
if signal==0:
#сумма чисел по каждому столбцу
    for j in range (0, n):
        s=0
        for i in range(0,n):
            s+=a[i][j]
        if s!=temp:
            signal=1
            break
if signal==1:
    print("====== Это не квадрат======")
else:
    print("=====Это магический квадрат======")