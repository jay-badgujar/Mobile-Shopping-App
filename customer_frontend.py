from customer_backend import *


def checkemail(email):
    con = mysql.connector.connect(
        host="localhost", user="root", password="", database="m11"
    )
    mycursor = con.cursor()
    isemail = False
    query = "select * from customer_info where customer_email=%s"
    val = (email,)
    mycursor.execute(query, val)
    rs = mycursor.fetchall()
    for i in rs:
        if i != "":
            isemail = True
    return isemail


def getcompanyoption():
    isstart2 = True
    while isstart2 != False:
        print()
        print("|--------------------------------------------|")
        print("|  Enter 1 For View Apple Company Mobiles    |")
        print("|  Enter 2 For View Samsung Company Mobiles  |")
        print("|  Enter 3 For View OnePlus Company Mobiles  |")
        print("|  Enter 4 For View Oppo Company Mobiles     |")
        print("|  Enter 5 For View Vivo Company Mobiles     |")
        print("|  Enter 6 For View Redmi Company Mobiles    |")
        print("|  Enter 7 For View Realme Company Mobiles   |")
        print("|  Enter 8 For Back                          |")
        print("|  Enter 9 For Exit                          |")
        print("|--------------------------------------------|")
        print()
        ch3 = input("Enter Your Choice : ")
        match ch3:
            case "1":
                customer.m3("apple")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "2":
                customer.m3("samsung")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "3":
                customer.m3("oneplus")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "4":
                customer.m3("oppo")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "5":
                customer.m3("vivo")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "6":
                customer.m3("redmi")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "7":
                customer.m3("realme")
                choiceask = input("Do You Want To Add To Cart?")
                choiceask = choiceask.lower()
                if choiceask == "yes":
                    id = dealer.checkalphadig("Enter The Id :")
                    quan = dealer.checkalphadig("Enter The Quantity :")
                    quan = int(quan)
                    customer.addtocart(email, id, quan)
            case "8":
                isstart2 = False
            case "9":
                exit()
            case _:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Choice! |")
                print("|----------------------------|")
                print()


def viewcompanyoption():
    isstart2 = True
    while isstart2 != False:
        print()
        print("|--------------------------------------------|")
        print("|  Enter 1 For View Apple Company Mobiles    |")
        print("|  Enter 2 For View Samsung Company Mobiles  |")
        print("|  Enter 3 For View OnePlus Company Mobiles  |")
        print("|  Enter 4 For View Oppo Company Mobiles     |")
        print("|  Enter 5 For View Vivo Company Mobiles     |")
        print("|  Enter 6 For View Redmi Company Mobiles    |")
        print("|  Enter 7 For View Realme Company Mobiles   |")
        print("|  Enter 8 For Back                          |")
        print("|  Enter 9 For Exit                          |")
        print("|--------------------------------------------|")
        print()
        ch3 = input("Enter Your Choice : ")
        match ch3:
            case "1":
                customer.m3("apple")
            case "2":
                customer.m3("samsung")
            case "3":
                customer.m3("oneplus")
            case "4":
                customer.m3("oppo")
            case "5":
                customer.m3("vivo")
            case "6":
                customer.m3("Redmi")
            case "7":
                customer.m3("Realme")
            case "8":
                isstart2 = False
            case "9":
                print("Exit")
                exit()
            case _:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Choice! |")
                print("|----------------------------|")
                print()


def getviewmobileoption():
    isstart2 = True
    while isstart2 != False:
        print()
        print("|----------------------------------------------|")
        print("|  Enter 1 For View Mobiles Simply             |")
        print("|  Enter 2 For View Specific Company Mobiles   |")
        print("|  Enter 3 For View Mobiles Sorted By Price    |")
        print("|  Enter 4 For View Mobiles Sorted By Ratings  |")
        print("|  Enter 5 For Back                            |")
        print("|  Enter 6 For Exit                            |")
        print("|----------------------------------------------|")
        print()
        ch3 = input("Enter Your Choice : ")
        match ch3:
            case "1":
                customer.make1("1")
            case "2":
                viewcompanyoption()
            case "3":
                customer.make1("3")
            case "4":
                customer.make1("4")
            case "5":
                isstart2 = False
            case "6":
                print("Exit")
                exit()
            case _:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Choice! |")
                print("|----------------------------|")
                print()


def getviewcartoption():
    if customer.checkemptycart(email) == False:
        isstart2 = True
        while isstart2 != False:
            print()
            print("|----------------------------------------------|")
            print("|  Enter 1 For View Mobiles Simply             |")
            print("|  Enter 2 For View Mobiles Sorted By Price    |")
            print("|  Enter 3 For View Mobiles Sorted By Ratings  |")
            print("|  Enter 4 For Back                            |")
            print("|  Enter 5 For Exit                            |")
            print("|----------------------------------------------|")
            print()
            ch3 = input("Enter Your Choice : ")
            match ch3:
                case "1":
                    customer.make(email, "1")
                case "2":
                    customer.make(email, "2")
                case "3":
                    customer.make(email, "3")
                case "4":
                    isstart2 = False
                case "5":
                    exit()
                case _:
                    print()
                    print("|----------------------------|")
                    print("| Please Enter Valid Choice! |")
                    print("|----------------------------|")
                    print()
    else:
        print()
        print("|----------------|")
        print("| Cart Is Empty! |")
        print("|----------------|")
        print()


def getremovecartoption():
    if customer.checkemptycart(email) == False:
        isstart2 = True
        while isstart2 != False:
            print()
            print("|--------------------------------------------------------------|")
            print("|  Enter 1 For Remove Specific Mobile From Your Cart           |")
            print("|  Enter 2 For Remove Specific Mobile Quantity From Your Cart  |")
            print("|  Enter 3 For Clear Whole Your Cart                           |")
            print("|  Enter 4 For Back                                            |")
            print("|  Enter 5 For Exit                                            |")
            print("|--------------------------------------------------------------|")
            print()
            ch3 = input("Enter Your Choice : ")
            match ch3:
                case "1":
                    customer.make(email, "1")
                    id = dealer.checkdigit("Enter The Id : ")
                    id = int(id)
                    if customer.checkidfromcart(id):
                        customer.removephonefromcart(email, id)
                    else:
                        print()
                        print("|------------------------|")
                        print("| Please Enter Valid Id! |")
                        print("|------------------------|")
                        print()

                case "2":
                    customer.make(email, "1")
                    id = dealer.checkdigit("Enter The Id : ")
                    if customer.checkidfromcart(id):
                        quantity = dealer.checkdigit("Enter The Quantity : ")
                        quantity = int(quantity)
                        customer.removequantityfromcart(email, id, quantity)
                    else:
                        print()
                        print("|------------------------|")
                        print("| Please Enter Valid Id! |")
                        print("|------------------------|")
                        print()
                case "3":
                    customer.make(email, "1")
                    customer.clearwholecart(email)
                    print()
                    print("|----------------------------|")
                    print("| Cleared Cart SuccessFully! |")
                    print("|----------------------------|")
                    print()
                case "4":
                    isstart2 = False
                case "5":
                    exit()
                case _:
                    print()
                    print("|----------------------------|")
                    print("| Please Enter Valid Choice! |")
                    print("|----------------------------|")
                    print()
    else:
        print()
        print("|----------------|")
        print("| Cart Is Empty! |")
        print("|----------------|")
        print()


customer = Customer()
dealer = Dealer()
isstart = True
while isstart != False:
    print()
    print("|-----------------------|")
    print("|  Enter 1 For Sign-Up  |")
    print("|  Enter 2 For Login    |")
    print("|  Enter 3 For Exit     |")
    print("|-----------------------|")
    print()
    ch1 = input("Enter Your Choice : ")
    match ch1:
        case "1":
            isemail = False
            while isemail != True:
                email = input("Enter Your E-mail ID : ")
                if checkemail(email) == False:
                    if (
                        email.endswith("@gmail.com")
                        or email.endswith("@yahoo.com")
                        or email.endswith("@icloud.com")
                        or email.endswith("@outlook.com")
                    ):
                        isemail = True
                    else:
                        isemail = False
                        print()
                        print("|------------------------------|")
                        print("| Your E-mail ID is Not Valid! |")
                        print("|------------------------------|")
                        print()
                else:
                    isemail = False
                    print()
                    print("|------------------------------|")
                    print("| E-mail ID Is Already Exists! |")
                    print("|------------------------------|")
                    print()
            if customer.customer_signup(email):
                print()
                print("|------------------------|")
                print("| Sign-Up SuccessFullly! |")
                print("|------------------------|")
                print()
                isstart = False
        case "2":
            isemail = False
            while isemail != True:
                email = input("Enter Your E-mail : ")
                if checkemail(email) == True:
                    if customer.customer_login(email):
                        isemail = True
                        isstart = False
                else:
                    print()
                    print("|---------------------------|")
                    print("| Please Enter Valid Email! |")
                    print("|---------------------------|")
                    print()
        case "3":
            exit()
        case _:
            print()
            print("|----------------------------|")
            print("| Please Enter Valid Choice! |")
            print("|----------------------------|")
            print()
isstart = True
customer.getall(email)
while isstart != False:
    print()
    print("|---------------------------------|")
    print("|  Enter 1 For Buy Direct Mobile  |")
    print("|  Enter 2 For Today's Deal       |")
    print("|  Enter 3 For Comparison         |")
    print("|  Enter 4 For Consulting         |")
    print("|  Enter 5 For Give The Rating    |")
    print("|  Enter 6 For Exit               |")
    print("|---------------------------------|")
    print()
    ch1 = input("Enter Your Choice : ")
    match ch1:
        case "1":
            isstart1 = True
            while isstart1 != False:
                print()
                print("|--------------------------------------------|")
                print("|  Enter 1 For See All The Mobiles           |")
                print("|  Enter 2 For Buy Mobile Right Now          |")
                print("|  Enter 3 For Cancel The Order              |")
                print("|  Enter 4 For Add Mobile To Your Cart       |")
                print("|  Enter 5 For Remove Mobile From Your Cart  |")
                print("|  Enter 6 For View Your Cart                |")
                print("|  Enter 7 For Update The Cart               |")
                print("|  Enter 8 For Buy The Cart                  |")
                print("|  Enter 9 For Back                          |")
                print("|  Enter 10 For Exit                         |")
                print("|--------------------------------------------|")
                print()
                ch2 = input("Enter Your Choice : ")
                match ch2:
                    case "1":
                        getviewmobileoption()
                    case "2":
                        customer.make1("1")
                        id = dealer.checkdigit("Enter The Id :")
                        customer.buynow(email, id)
                    case "3":
                        if customer.checkfrombought(email) == False:
                            customer.viewboughtphones(email)
                            id = dealer.checkdigit("Enter The Id : ")
                            if customer.checkid(id):
                                customer.cancelorder(id)
                            else:
                                print()
                                print("|------------------------|")
                                print("| Please Enter Valid Id! |")
                                print("|------------------------|")
                                print()
                        else:
                            print()
                            print("|-----------------------------------|")
                            print("| You Have Not Purchased Any Phone! |")
                            print("|-----------------------------------|")
                            print()
                    case "4":
                        getcompanyoption()
                    case "5":
                        getremovecartoption()
                    case "6":
                        getviewcartoption()
                    case "7":
                        if customer.checkemptycart(email) == False:
                            choiceask = dealer.checkalpha(
                                "Do You Want To Add Quantity Or Remove ?"
                            )
                            customer.make(email, "1")
                            customer.updatecart(email, choiceask)
                        else:
                            print()
                            print("|----------------|")
                            print("| Cart Is Empty! |")
                            print("|----------------|")
                            print()
                    case "8":
                        if customer.checkemptycart(email) == False:
                            print("Your Total Bill Is : ", customer.getbill(email))
                            choiceask = dealer.checkalpha("Do You Want To Buy It ?")
                            choiceask = choiceask.lower()
                            if choiceask == "yes":
                                customer.purchasemobile(customer.getbill(email))
                                customer.clearwholecart(email)
                        else:
                            print()
                            print("|----------------|")
                            print("| Cart Is Empty! |")
                            print("|----------------|")
                            print()
                    case "9":
                        isstart1 = False
                    case "10":
                        exit()
                    case _:
                        print()
                        print("|----------------------------|")
                        print("| Please Enter Valid Choice! |")
                        print("|----------------------------|")
                        print()
        case "2":
            customer.displaytodaydeal(email)
        case "3":
            customer.comparison()
        case "4":
            first = dealer.checkdigit("Enter Starting Price : ")
            last = dealer.checkdigit("Enter Ending Price : ")
            first = int(first)
            last = int(last)
            customer.getBudgetMobile(first, last)
        case "5":
            customer.make1("1")
            id = dealer.checkdigit("Enter The Id : ")
            if customer.checkid(id):
                israte = False
                while israte != True:
                    rating = dealer.isfloat("Enter The Rating : ")
                    rating = float(rating)
                    if rating <= 5 and rating > 0:
                        israte = True
                    else:
                        israte = False
                customer.giverating(id, rating)
            else:
                print()
                print("|------------------------|")
                print("| Please Enter Valid Id! |")
                print("|------------------------|")
                print()
        case "6":
            exit()
        case _:
            print()
            print("|----------------------------|")
            print("| Please Enter Valid Choice! |")
            print("|----------------------------|")
            print()
