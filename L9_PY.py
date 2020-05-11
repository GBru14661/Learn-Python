try:
    a=int(input("Inta = "))
    b = int(input("Intb = "))
    cza=a/b
except (ValueError,ZeroDivisionError):
    print('That not int or zerodivision error')
finally:
    print('good')
    print(cza)
