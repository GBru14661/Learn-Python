'''
print("=====0000=====")
while True:
    num1=int(input())
    num2=int(input())
    if num1 in range(0,10**9+1):
        if num2 in range(0,10**9+1):
            result=num1+num2
            print(result)
            break
        else:
            print("Input Num 2 Again!")
            continue
    else:
        print("Input Num 1 Again!")
        continue#0000

print("=====0001=====")
while True:
    unit_sc=int(input("Input Unit Score : "))
    if unit_sc not in range(1,31):
        print("Input Unit Score Again!")
        continue
    else:
        while True:
            mid_sc=int(input("Input Midterm Score : "))
            if mid_sc not in range(1,31):
                print("Input Midterm Score Again")
                continue
            else:
                while True:
                    fin_sc=int(input("Input Final Score : "))
                    if fin_sc not in range(1,41):
                        print("Input Final Score Again!")
                        continue
                    else:
                        break
                break
        break
total=unit_sc+mid_sc+fin_sc
if total>=80:
    grade="A"
elif total>=75:
    grade="B+"
elif total>=70:
    grade='B'
elif total>=65:
    grade='C+'
elif total>=60:
    grade='C'
elif total>=55:
    grade='D+'
elif total>=50:
    grade='D'
elif total<50:
    grade='F'
print("Grade : ",grade)#0001

print("=====0002=====")
while True:
    number = int(input())
    if number not in range(1,1001):
        print("Input Number of data again!")
        continue
    else:
        break
data_list=[]
for data in range(number):
        data = int(input())
        if data in range(-2*10**9,2*10**9+1):
            data_list.append(data)
        else:
            print("Input data again!")
print("Min :",min(data_list))
print("Max :",max(data_list))#0002


print("=====0005=====")
from math import*
a,b=input().split()
apow=float(a)**2
bpow=float(b)**2
tc=apow+bpow
c=sqrt(tc)
print("%.6f"%c)#0005

print("=====0008=====")
x1,s=(input()).split()
if x1 not in range(-1000,1001):
    "Value Incorrect"
elif s not in range(-1000,1001):
    "Value Incorrect"
x2=2*int(s)-int(x1)
print(x2)
'''

print("=====0008=====")