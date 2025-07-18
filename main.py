def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def sumFact(n):
    sum=0
    for i in range(1,n+1):
        sum+=fact(i)
    return sum

number=int(input("enter a number:"))
print("factoril:",fact(number),"sum:",sumFact(number))