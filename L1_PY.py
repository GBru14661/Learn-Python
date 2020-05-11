name_f=input("from NAME: ")
address_f=input("from ADDRESS: ")
zipcode_f=input("from ZIP CODE: ")
name_t=input("to NAME: ")
address_t=input("to ADDRESS: ")
zipcode_t=input("to ZIP CODE: ")
pname="Name"
paddress="Address"
pzipcode="Zip code"
pto="TO"

print("Form")
print(pname.rjust(5)+' '+name_f)
print(paddress.rjust(8)+' '+address_f)
print(pzipcode.rjust(9)+' '+zipcode_f)
print()
print(pto.center(20))
print(pname.center(22)+' '+name_t)
print(paddress.center(22)+' '+address_t)
print(pzipcode.center(22)+' '+zipcode_t)
