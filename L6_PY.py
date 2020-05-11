money=int(input("Input Money : "))
if money>=30000:
    if money>=35000:
        print("Galaxy S10+")
    else:
        print("Galaxy S10")
elif money>=20000:
    if money>=25000:
        print("Galaxy S9")
    else:
        print("Galaxy S9+")
else:
    print("Galaxy A9")