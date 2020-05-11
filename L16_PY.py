'''from L15_PY import*
i=1
goods_lst=[]
while i<=3:
    goods=float(input("Input Your Cost of Goods_%d : "%i))
    goods_lst.append(goods)
    i+=1
print("Summary Goods :",goods_lst)
print("Total goods is :",sum(goods_lst))
total=sum(goods_lst)
a=goods_lst[0]
b=goods_lst[1]
c=goods_lst[2]
if total>5000:
    print("Discount 15% = ",(15*total)/100)
    print("Total Price is",cost5000up(a,b,c))
elif total>=2500:
    print("Discount 10% = ", (10 * total) / 100)
    print("Total Price is", cost2500up(a, b, c))
elif total>=1500:
    print("Discount 5% = ", (5 * total) / 100)
    print("Total Price is", cost1500up(a, b, c))
else:
    print("No Discount")
    print("Total Price is",total)'''

import time
child=int(input("Input Number of children : "))
adult=int(input("Input Number of adult : "))
tt_ch=child*159
tt_ad=adult*199
print("Summary Price")
print("Children =",child)
print("Adult =",adult)
print("Total price of children =",tt_ch)
print("Total price of adult =",tt_ad)
print(time.strftime("%a,%d %b %Y %H:%M:%S",time.gmtime()))
