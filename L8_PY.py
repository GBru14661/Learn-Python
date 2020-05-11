'''num1=int(input("Input Number 1 : "))
num2=int(input("Input Number 2 : "))
if num1>num2:
    print("Number 1 > Number 2")
else:
    print("Number 1 <= Number 2")'''

'''i=1
costlist=[]
while i<=3:
    cost=float(input("สินค้า %d ราคา : "%i))
    costlist.append(cost)
    i+=1
print(costlist)
print("Tatal Cost is %f"%sum(costlist))
print("Good Bye !!")'''

'''cost=float(input("Cost of Car is "))
installments=int(input("The number (12,24,36,48,60) of months to be paid in installments : "))
pay=cost/installments
if installments==12:
    paymont=pay+((1/100)*cost)
    print("Total Cost is",paymont)
elif installments==24:
    paymont=pay+((1.5/100)*cost)
    print("Total Cost is",paymont)
elif installments==36:
    paymont=pay+((2.5/100)*cost)
    print("Total Cost is",paymont)
elif installments==48:
    paymont=pay+((3.5/100)*cost)
    print("Total Cost is",paymont)
elif installments==60:
    paymont=pay+((4.5/100)*cost)
    print("Total Cost is",paymont)
else:
    print("Input Month Again")'''

'''while True:
    i=input("Continuos = C | End = E   Input : ")
    if i=="E":
        print("Close Program")
        break
    elif i=="C":
        people = int(input("Number of people you will pay for : "))
        people_list = {}
        for a in range(1, people + 1):
            net_pay={}
            total_cost=[]
            number = input("Enter People %d : " % a)
            network = input("""             Dtac
                    AIS
                    True
                    Input your Network : """)
            pay = input("""    What cost you want to pay 
                    50, 100, 300, 500, 1000 Baht
                        Input your Cost : """)
            net_pay.setdefault(network,pay)
            people_list.setdefault(number,net_pay)
            total_cost.append(pay)

        print(people_list)
        print(net_pay.values())'''

i=1
num_lst=[]
while i<=6:
    num=int(input("Enter Number 1-6 : "))
    if num>6: # Don't input same number
        continue
    elif num<1:
        continue
    else:
        num_lst.append(num)
        i+=1
a=sum(num_lst)
D=a//4






