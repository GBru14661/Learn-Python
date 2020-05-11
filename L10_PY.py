'''header="{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format("รหัสนักเรียน","คะแนนระหว่างภาค","คะแนนกลางภาค","คะแนนปลายภาค","คะแนนรวท","ผลการเรียนที่ได้")
file=open(r"D:\Learn Python\Score.txt","a",encoding="utf-8")
file.write(header)
j=1
student=int(input("จำนวนนักเรียน ",))
while j<=student:
    print("นักเรียนคนที่ %d"%j)
    unit=float(input("คะแนนระหว่างภาค "))
    mid=float(input("คะแนนกลางภาค "))
    fin=float(input("คะแนนปลายภาค "))
    total=unit+mid+fin
    if total<50:
        grade="0"
    elif total<60:
        grade="1"
    elif total<70:
        grade="2"
    elif total<80:
        grade="3"
    else:
        grade="4"
    print("คะแนนรวมคือ ",total,"ได้เกรด ",grade)
    file.write("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format(student,unit,mid,fin,total,grade))

    j+=1
file.close()'''

file=open(r"D:\Learn Python\Score.txt")
data=file.read()
print(data)
file.close()