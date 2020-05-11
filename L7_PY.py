while True:
    z=input("Y=Enter Program N=Close Program : ")
    if z=="N":
        print("Program End")
        break
    elif z=="Y":
        stu = int(input("NUMBER OF STUDENTS : "))
        unit=int(input("Enter Number of Unit : "))
        for i in range(1,stu+1):
            score=[]
            print("Student ", i)
            for a in range(1,unit+1):
                n=int(input("Enter Score %d = "%a))
                score.append(n)
                total=sum(score)
            if total>=80:
                print("Total Score Student",i,"is",total,"You are Grade 4")
            elif total>=70:
                print("Total Score Student",i,"is",total,"You are Grade 3")
            elif total>=60:
                print("Total Score Student",i,"is",total,"You are Grade 2")
            elif total>=50:
                print("Total Score Student",i,"is",total,"You are Grade 1")
            else:
                print("Total Score Student",i,"is",total,"You are Grade 0")
            print()