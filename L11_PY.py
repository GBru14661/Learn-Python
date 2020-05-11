'''import csv
try:
    with open(r"D:\Learn Python\GbruCSV.csv","w",newline='') as file:
        csvfile=csv.writer(file,delimiter="\t")
        csvfile=csv.writer(file)
        csvfile.writerow(["few",'Ice',"Aun"])
        csvfile.writerow(["Title","Faro","Bhum"])
except(FileExistsError,FileNotFoundError):
    print("ผิดพลาด")
else:
    print("เขียนไฟล์สพเร็จ")'''

file=csv.reader(open(r"D:\Learn Python\GbruCSV.csv","r"))
for data in file:
    print("{},{},{}".format(data[0],data[1],data[2]))

