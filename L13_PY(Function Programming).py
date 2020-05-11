while True:
    op_cl=input("Start Program 1=Find Volume or 2=Money or 3=BMI or close=close program Input: ")
    if op_cl=="close":
        break
    elif op_cl=="1":
        def pyramid():
            base_area=float(input("Input Base Area : "))
            height = float(input("Input Height : "))
            volume=(1/3)*base_area*height
            print("Volume of Pyramid is {}".format(volume))
        def cylinder():
            pi=3.14159265
            r=float(input("Input Radius : "))
            height = float(input("Input Height : "))
            volume=pi*r**2*height
            print("Volume of Pyramid is {}".format(volume))
        def cone():
            pi=3.14159265
            r=float(input("Input Radius : "))
            height = float(input("Input Height : "))
            volume=(1/3)*pi*r**2*height
            print("Volume of Pyramid is {}".format(volume))
        while True:
            i=input("S=Start E=End Input: ")
            if i=="E":
                break
            elif i=="S":
                while True:
                    select=input("""
                    Pyramid
                    Cylinder
                    Cone
                    E=End
                    What volume do you want to find : """)
                    if select=="Pyramid":
                        pyramid()
                    elif select=="Cylinder":
                        cylinder()
                    elif select=="Cone":
                        cone()
                    elif select=="E":
                        break
                    else:
                        print("Input Type of Volume again!")
                        continue
            else:
                print("Input menu again!")
                continue
    elif op_cl == "2":
        def Brunei():
            money=baht/25
            print("%.2f Thai Baht = %.2f Brunei Dollar"%(baht,money))
        def Cambodia():
            money=baht*127
            print("%.2f Thai Baht = %.2f Cambodian Riel"%(baht,money))
        def Indonesia():
            money=(1000*baht)/3
            print("%.2f Thai Baht = %.2f Indonesian Rupiah"%(baht,money))
        def Laos():
            money=(1000*baht)/4
            print("%.2f Thai Baht = %.2f Lao Kip"%(baht,money))
        def Malaysia():
            money=baht/10
            print("%.2f Thai Baht = %.2f Malaysian Ringgit"%(baht,money))
        def Myanmar():
            money=baht*26
            print("%.2f Thai Baht = %.2f Myanmar Kyat"%(baht,money))
        def Philippine():
            money=baht*1.40
            print("%.2f Thai Baht = %.2f Philippine Peso"%(baht,money))
        def Singapore():
            money=baht/25
            print("%.2f Thai Baht = %.2f Singapore Dollar"%(baht,money))
        def Vietnam():
            money=baht*652
            print("%.2f Thai Baht = %.2f Vietnamese Dong"%(baht,money))
        while True:
            i=input("Start=S End=E Input:")
            if i =="E":
                break
            elif i =="S":
                while True:
                    country=input("Input contry you want money : ")
                    baht=float(input("Input Thai Baht : "))
                    if country=="Brunei":
                        Brunei()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Cambodia":
                        Cambodia()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Indonesia":
                        Indonesia()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Lao":
                        Laos()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Malaysia":
                        Malaysia()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Myanmar":
                        Myanmar()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Philippine":
                        Philippine()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Singapore":
                        Singapore()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
                    elif country=="Vietnam":
                        Vietnam()
                        cont=input("Continue? Y or N : ")
                        if cont=="N":
                            break
                        elif cont=="Y":
                            continue
    elif op_cl == "3":
        def man_BMI():
            if bmi<19:
                print("You are thin!")
            elif bmi<25:
                print("You are Slender")
            elif bmi<30:
                print("You are Fat")
            elif bmi>=30:
                print("You are Dangerous Fat!")
        def woman_BMI():
            if bmi<18:
                print("You are thin!")
            elif bmi<24:
                print("You are Slender")
            elif bmi<30:
                print("You are Fat")
            elif bmi>=30:
                print("You are Dangerous Fat!")
        gender=input("Input your Gender Male or Female : ")
        weight=float(input("Input Your Weight : "))
        height=float(input("input Your Height : "))
        bmi=weight/(height/100)**2
        print(bmi)
        if gender=="Male":
            man_BMI()
            continue
        elif gender=="Female":
            woman_BMI()
            continue