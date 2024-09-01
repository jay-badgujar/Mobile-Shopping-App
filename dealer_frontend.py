from dealer_backend import *

d = Dealer()
islogin = False
while islogin != True:
    if d.dealer_login():
        islogin = True
    else:
        islogin = False
isexit = True
while isexit != False:
    print()
    print("|-----------------------------------------------------------------|")
    print("|            Enter 1 For Add New Phone                            |")
    print("|            Enter 2 For Remove Phone                             |")
    print("|            Enter 3 For Add Phone To Sale                        |")
    print("|            Enter 4 For Remove Phone From Sale                   |")
    print("|            Enter 5 For Update Mobile's Price                    |")
    print("|            Enter 6 For Update Mobile's Stock                    |")
    print("|            Enter 7 For Check Mobile Stock's Empty               |")
    print("|            Enter 8 For Check Mobile's Stock                     |")
    print("|            Enter 9 For Check Mobile's Price                     |")
    print("|            Enter 10 For View All The Mobiles                    |")
    print("|            Enter 11 For View Sales Of All Companies Mobiles     |")
    print("|            Enter 12 For View Sale's Mobile                      |")
    print("|            Enter 13 Exit                                        |")
    print("|-----------------------------------------------------------------|")
    print()
    ch = input("Enter Your Choice : ")
    match ch:
        case "1":
            d.addPhone()
        case "2":
            d.removephone()
        case "3":
            d.make1("1")
            d.addtodaydeal()
        case "4":
            d.viewdeal()
            d.removefromdeal()
        case "5":
            d.make1("1")
            ismobile = False
            while ismobile != True:
                cnmae = input("Enter The Company Name : ")
                mnmae = input("Enter The Mobile Name : ")
                if d.checkmobileexists(cnmae, mnmae):
                    ismobile = True
                else:
                    print()
                    print("|--------------------|")
                    print("| Mobile Not Exists! |")
                    print("|--------------------|")
                    print()
                    ismobile = False
            price = d.isfloat("Enter The New Price : ")
            d.updateprice(cnmae, mnmae, price)
        case "6":
            d.make1("1")
            ismobile = False
            while ismobile != True:
                cnmae = input("Enter The Company Name : ")
                mnmae = input("Enter The Mobile Name : ")
                if d.checkmobileexists(cnmae, mnmae):
                    ismobile = True
                else:
                    print()
                    print("|--------------------|")
                    print("| Mobile Not Exists! |")
                    print("|--------------------|")
                    print()
                    ismobile = False
            stock = d.checkdigit("Enter The New Stock : ")
            d.updatestock(cnmae, mnmae, stock)
        case "7":
            d.make1("33")
        case "8":
            ischoice = False
            while ischoice != True:
                print()
                print("|-------------------------------------------------------|")
                print("| Enter 1 For View Mobile's Stock Of All Mobiles        |")
                print("| Enter 2 For View Mobile's Stock Of Particular Mobiles |")
                print("| Enter 3 For Back                                      |")
                print("|-------------------------------------------------------|")
                print()
                ch = input("Enter Your Choice : ")
                match ch:
                    case "1":
                        d.m22()
                    case "2":
                        ismobile = False
                        while ismobile != True:
                            cnmae = input("Enter The Company Name : ")
                            mnmae = input("Enter The Mobile Name : ")
                            if d.checkmobileexists(cnmae, mnmae):
                                ismobile = True
                            else:
                                print()
                                print("|--------------------|")
                                print("| Mobile Not Exists! |")
                                print("|--------------------|")
                                print()
                                ismobile = False
                        print("-------------------------------------------------")
                        print(
                            "The Current Available Stock is : ",
                            d.getstock(cnmae, mnmae),
                        )
                        print("-------------------------------------------------")
                    case "3":
                        ischoice = True
                    case _:
                        print()
                        print("|----------------------------|")
                        print("| Please Enter Valid Choice! |")
                        print("|----------------------------|")
                        print()
                        ischoice = False
        case "9":
            ischoice = False
            while ischoice != True:
                print()
                print("|-------------------------------------------------------|")
                print("| Enter 1 For View Mobile's Price Of All Mobiles        |")
                print("| Enter 2 For View Mobile's Price Of Particular Mobiles |")
                print("| Enter 3 For Back                                      |")
                print("|-------------------------------------------------------|")
                print()
                ch = input("Enter Your Choice : ")
                match ch:
                    case "1":
                        d.m2()
                    case "2":
                        ismobile = False
                        while ismobile != True:
                            cnmae = input("Enter The Company Name : ")
                            mnmae = input("Enter The Mobile Name : ")
                            if d.checkmobileexists(cnmae, mnmae):
                                ismobile = True
                            else:
                                print("|--------------------|")
                                print("| Mobile Not Exists! |")
                                print("|--------------------|")
                                ismobile = False
                        print("--------------------------------------------")
                        print("The Current Price is : ", d.getprice(cnmae, mnmae))
                        print("--------------------------------------------")
                        pass
                    case "3":
                        ischoice = True
                    case _:
                        print()
                        print("|----------------------------|")
                        print("| Please Enter Valid Choice! |")
                        print("|----------------------------|")
                        print()
                        ischoice = False
        case "10":
            ischoice1 = False
            while ischoice1 != True:
                print()
                print("|--------------------------------------------------|")
                print("| Enter 1 For View Mobiles Simply                  |")
                print("| Enter 2 For View Mobiles Sort By Price           |")
                print("| Enter 3 For View Mobiles Sort By Available Stock |")
                print("| Enter 4 For Back                                 |")
                print("|--------------------------------------------------|")
                print()
                ch = input("Enter Your Choice : ")
                match ch:
                    case "1":
                        d.make1("1")
                    case "2":
                        d.make1("3")
                    case "3":
                        d.make1("5")
                    case "4":
                        ischoice1 = True
                    case _:
                        print()
                        print("|----------------------------|")
                        print("| Please Enter Valid Choice! |")
                        print("|----------------------------|")
                        print()
        case "11":
            d.viewsales()
        case "12":
            d.viewdeal()
        case "13":
            isexit = False
        case _:
            print()
            print("|----------------------------|")
            print("| Please Enter Valid Choice! |")
            print("|----------------------------|")
            print()
