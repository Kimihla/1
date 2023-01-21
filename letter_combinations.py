#функция комбинирующая символы в различных количестве и порядке. Предполагается, что все символы аргумента C различны.
def H(B,C):
    A=list()
    if C==[]:
        A.append(B)
        return A
    else:
        for i in C:
            b=B.copy()
            b.extend(i)
            A.append(b)
            c=C.copy()
            c.remove(i)
            A.extend( H(b,c))
    return A

word=input("Введите слово:    ")
#переводим строку во множество. таким образом удаляются повторяющиеся символы
word=set(word)
#эта функция возвращает список всех размещений символов
h=H([],word)
count=0
#упорядочивает все размещения к одному сочетанию
for i in h:
    count=count+1
    i.sort() #[a,b,c],[a,c,b],[b,c,a], ... --> [a,b,c]
#упорядочивает сам список сочетаний (алфавитный порядок)
h.sort()
i=0
#в цикле удаляются все одинаковые сочетания, кроме одного
while i<count:
    j=i+1
    while j<count:
        if h[i]==h[j]:
            del h[j]
            count=count-1
        else:
            j+=1
    i+=1

k=len(word)+1
#во вложенных циклах упорядочивается список по длине (количеству символов) сочетаний. затем выводтся на консоль
for i in range(k):
    print("===========================\n")
    for j in h:
        if len(j)==i:
            print(j)
    print("===========================\n")