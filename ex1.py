num=int(input("please enter num of 4 digits:"))
while int(num)<1000 or int(num)>9999:
    print("it's not good\n")
    num=int(input("enter num again: "))
x=num//1000
y=num//100%10
z=num//10%10
t=num%10
print(x+y+z+t)
print(t*1000+z*100+y*10+x)
if x==t and y==z:
    print("it's polindrom")
else:
    print("it's not polindrom")
