"""months=["Jan","May","Jul","Aug","oct","Dec"]
months.insert(1,"Feb")
months.insert(2,"Mar")
months.insert(3,"Apr")
months.insert(5,"June")
months.insert(8,"Sep")
months.insert(10,"Nov")
print(months)
del months[2]
del months[5]
del months[9]
print(months)"""

"""days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
days.reverse()
print(days)
days.sort()
print(days)
days.pop(1)
days.pop(2)
days.pop(4)
print(days)"""

'''brand_cars=("Toyota","Honda","Benz","BMW","Tesla","Ford","KIA","Volvo")
print(brand_cars.index("Benz",0,8))
print(brand_cars.index("Ford",0,8))
print(brand_cars.index("Volvo",0,8))
print(len(brand_cars))
print("Susuki" in brand_cars)
print("Ferrari" in brand_cars)
print("Ford" in brand_cars)'''

'''months={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
print(months.get(4))
print(months.get(8))
print(months.get(12))
months.pop(5)
months.pop(7)
months.pop(11)
print(months)
print(months.values())'''

'''closefriend={1:("Few","085"),2:("Aun","092"),3:("Ken","082")}
closefriend.setdefault(4,("Stang","088"))
closefriend.setdefault(5,("Title","099"))
print(closefriend)
print(closefriend.values())'''

'''A={12,15,25,10,17,19,20,22}
B={11,9,15,13,20,18,16,17,19}
C={22,20,18,16,28,15,30,26}
print(A&B)
print(A&C)
print(B|C)
print(A|C)
print(A-C)
print(B-A)'''

'''x={"cat",'dog','fish','bird','bee'}
y={'snake','lion','pig','dog','cat'}
print(x.intersection(y))
print(x.difference(y))
print((x.difference(y)).union((y.difference(x))))'''

