from collections import Counter
import operator
import random
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=True)
parser.add_argument('part', metavar='N', type=str)
args = parser.parse_args()
part_of_program= args.part
filename=args.file

def MergeSort(list):
    n=len(list)
    if n < 2:
        return list
    left = MergeSort(list[:n//2])
    right = MergeSort(list[n//2:n])
    i=j=0;
    res=[]
    while i<len(left) or j<len(right):
        if not i<len(left):
            res.append(right[j]);j=j+1
        elif not j<len(right):
            res.append(left[i]);i=i+1
        elif left[i]<right[j]:
            res.append(left[i]);i=i+1
        else:
            res.append(right[j]);j=j+1
    return res

def QuickSort(list,first,last):
    if first>=last:
        return
    piv =list[random.randint(first,last)]
    i,j=first,last
    while i<=j:
        while list[i] < piv: i = i+1
        while list[j] > piv: j = j-1
        if i <= j:
            list[i], list[j] = list[j], list[i]
            i,j=i+1,j-1
    QuickSort(list,first,j)
    QuickSort(list,i,last)

def Fibonacci(k):
    if k==0 or k==1:
        return 1
    return Fibonacci(k-1)+Fibonacci(k-2)
def generatorFibonacci(k):
    for i in range(k):
        yield Fibonacci(i)

if part_of_program=="wordcounter":
    with open(args.file,"r")as str:
        s= str.read().split()
    m=dict(Counter(s))
    print (m)
    sorted_x = sorted(m.items(), key=operator.itemgetter(1), reverse=True)

    result=""
    for i in range(10):
        result = result+sorted_x[i][0]+" "
    print(result)
#for i in range(len(s)):
#    if m.get(m[s[i]], None) is None:
 #       m[s[i]]= 1; #если уникален, то вставляем новый иначе значение увеличиваем на единицу
  #  else m.get


#"fileWithNumbers" -- Файл с номерами для сортировки
if part_of_program=="quicksort":
    with open(filename,"r") as str:
        strlist = str.read().split(" ")
    x = []
    for i in strlist:
        x.append(int(i))
    y = x.copy();
    QuickSort(x,0,len(x)-1)
    print(x)
if part_of_program == "mergesort":
    with open(filename,"r") as str:
        strlist = str.read().split(" ")
    x = []
    for i in strlist:
        x.append(int(i))
    x= MergeSort(x)
    print(x)

#FibonacciNumber.txt -- имя файла
if part_of_program =="fibonacci":
    with open(filename,"r") as f:
        num = f.read()
    num = int(num)

    co = generatorFibonacci(num)
    res = ""
    for i in co:
        res = res+str(i)+" "
    print(res)
