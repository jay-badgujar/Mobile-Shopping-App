import os
from dealer_backend import *
import mysql.connector
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class Customer:
    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost", user="root", password="", database="m11"
        )
        self.mycursor = self.con.cursor()

    def getall(self, email):
        sql = "select customer_name,customer_mobileno,customer_address from customer_info where customer_email=%s"
        val = (email,)
        self.mycursor.execute(sql, val)
        data = self.mycursor.fetchone()
        self.cname = data[0]
        self.cmbno = data[1]
        self.caddress = data[2]

    def getremovecartoption(self):
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
                    print("Remove Specific Mobile")
                case "2":
                    print("Remove Specific Mobile Quantity")
                case "3":
                    print("Clear Whole Cart")
                case "4":
                    print("Back")
                    isstart2 = False
                case "5":
                    print("Exit")
                    exit()
                case _:
                    print("Please Enter Valid Choice!")

    def checkpassword(self, password=""):
        ispasword = False
        count = 0
        upper1 = 0
        lower1 = 0
        special1 = 0
        dig1 = 0
        if len(password) >= 8:
            for i in password:
                if i.isupper():
                    count += 1
                    upper1 = 1
                elif i.islower():
                    count += 1
                    lower1 = 1
                elif i.isdigit():
                    count += 1
                    dig1 = 1
                elif (
                    i == "@"
                    or i == "#"
                    or i == "&"
                    or i == "$"
                    or i == "%"
                    or i == "!"
                    or i == "^"
                    or i == "*"
                ):
                    count += 1
                    special1 = 1
            if (
                count >= 4
                and upper1 == 1
                and lower1 == 1
                and dig1 == 1
                and special1 == 1
            ):
                ispasword = True
            else:
                ispasword = False
                print()
                print(
                    "|-----------------------------------------------------------------------|"
                )

                ispasword = False
                if dig1 == 0:
                    print(
                        "| Your Password Doesn't Contains Digit!                                 |"
                    )
                if special1 == 0:
                    print(
                        "| Your Password Doesn't Contains Special Character Just Like @,#,etc..! |"
                    )
                if upper1 == 0:
                    print(
                        "| Your Password Doesn't Contains UpperCase Letter!                      |"
                    )
                if lower1 == 0:
                    print(
                        "| Your Password Doesn't Contains LowerCase Letter!                      |"
                    )
                print(
                    "|-----------------------------------------------------------------------|"
                )
                print()
        else:
            print()
            print("|-----------------------------------------------------|")
            print("| Your Password Length Must Be Greater Or Equal To 8! |")
            print("|-----------------------------------------------------|")
            print()

        return ispasword

    def forgotpass(self, email, newpassc):
        query = "update customer_info set customer_password=%s where customer_email=%s"
        val = (newpassc, email)
        self.mycursor.execute(query, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|--------------------------------|")
            print("| Password Updated SuccessFully! |")
            print("|--------------------------------|")
            print()

    def checkemail(self, email):
        isemail = False
        query = "select * from customer_info where customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isemail = True
        return isemail

        def checkemailpass(self, email, pasc):
            islogin = False
            query = "select * from customer_info where customer_email=%s and customer_password=%s"
            val = (email, pasc)
            self.mycursor.execute(query, val)
            rs = self.mycursor.fetchall()
            for i in rs:
                if i != "":
                    islogin = True
            return islogin

    def existsmobilenumberlogin(self, number, email):
        isnumber = False
        query = "select * from customer_info where customer_mobileno=%s and customer_email=%s"
        val = (number, email)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isnumber = True
        return isnumber

    def existsmobilenumber(self, number):
        isnumber = False
        query = "select * from customer_info where customer_mobileno=%s"
        val = (number,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isnumber = True
        return isnumber

    def customer_signup(self, email):
        issignup = False
        ispasscode = False
        s = """password length must be greater or equal to 8 and
    password must contain one digit,lowercase,uppercase
    and one special symbol"""
        print(s)
        while ispasscode != True:
            passw = input("Enter Your Password : ")
            passw = passw.strip(" ")
            if self.checkpassword(passw) == True:
                ispasscode = True
            else:
                ispasscode = False
        isname = False
        while isname != True:
            name = input("Enter Your Name : ")
            for i in name:
                if i.isalpha() or i == " ":
                    isname = True
                else:
                    print()
                    print("|--------------------------|")
                    print("| Please Enter Valid Name! |")
                    print("|--------------------------|")
                    print()
                    isname = False
                    break
        name = name.strip(" ")
        address = input("Enter Your Address : ")
        ismobile = False
        while ismobile != True:
            mobilenumber = input("Enter Your Mobile Number : ")
            mobilenumber = mobilenumber.strip(" ")
            if len(mobilenumber) == 10:
                if mobilenumber.isdigit():
                    if self.existsmobilenumber(mobilenumber) == False:
                        if (
                            mobilenumber.startswith("9")
                            or mobilenumber.startswith("8")
                            or mobilenumber.startswith("7")
                            or mobilenumber.startswith("6")
                        ):
                            ismobile = True
                        else:
                            ismobile = False
                            print()
                            print("|-----------------------|")
                            print("| Invalid MobileNumber! |")
                            print("|-----------------------|")
                            print()
                    else:
                        print()
                        print("|---------------------------------|")
                        print("| MobileNumber Already Registered |")
                        print("|---------------------------------|")
                        print()
                else:
                    ismobile = False
                    print()
                    print("|-----------------------|")
                    print("| Invalid MobileNumber! |")
                    print("|-----------------------|")
                    print()
            else:
                ismobile = False
                print()
                print("|-----------------------|")
                print("| Invalid MobileNumber! |")
                print("|-----------------------|")
                print()
        query = "INSERT INTO customer_info(customer_name,customer_email,customer_password,customer_address,customer_mobileno) VALUES(%s,%s,%s,%s,%s)"
        val = (name, email, passw, address, mobilenumber)
        self.mycursor.execute(query, val)
        self.con.commit()
        issignup = True
        return issignup

    def customer_login(self, email):
        islogin = False
        ispass = False
        while ispass != True:
            passc = input("Enter Your Password : ")
            if self.checkemailpass(email, passc) == True:
                print()
                print("|--------------------|")
                print("| SuccesFully Login! |")
                print("|--------------------|")
                print()
                ispass = isemail = True
            else:
                ispass = isemail = False
                print("Enter Valid Password!")
                answer = input("Did You Forgot Your Password?")
                if answer.lower() == "yes":
                    isnumber = False
                    while isnumber != True:
                        number = input("Enter Your Registered MobileNumber : ")
                        if self.existsmobilenumberlogin(number, email):
                            isotp = False
                            while isotp != True:
                                genrated_otp = random.randrange(1000, 10000)
                                print("Your OTP Is : ", genrated_otp)
                                otp = input("Enter The OTP : ")
                                if otp.isdigit():
                                    otp = int(otp)
                                    if otp == genrated_otp:
                                        isotp = isnumber = True
                                    else:
                                        isotp = False
                                else:
                                    print()
                                    print("|-------------------------|")
                                    print("| Please Enter Valid OTP! |")
                                    print("|-------------------------|")
                                    print()
                                    isotp = False
                        else:
                            print()
                            print("|----------------------------|")
                            print("| Please Enter Valid Number! |")
                            print("|----------------------------|")
                            print()
                            isnumber = False
                    isnewp = False
                    while isnewp != True:
                        newp = input("Enter Your New Password : ")
                        if self.checkpassword(newp) == True:
                            self.forgotpass(email, newp)
                            print()
                            print("|---------------------|")
                            print("| SuccessFully Login! |")
                            print("|---------------------|")
                            print()
                            isnewp = ispass = isemail = True
                        else:
                            isnewp = ispass = isemail = False
        islogin = True
        return islogin

    def displaycompanymobile(self, company):
        query = "SELECT pbrand_name,pname,pprice FROM phone WHERE pbrand_name=%s"
        val = (company,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            print(i[0] + " - " + i[1])

    def make(self, email, choice):
        file = self.cname + ".txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(f"\nName : {self.cname}" + "\n")
        f.write(157 * "-" + "\n")
        f.write(157 * "-")
        f.write(f"\nAddress : {self.caddress}" + "\n")
        f.write(157 * "-" + "\n")
        f.write(157 * "-")
        f.write(f"\nMobile-Number : {self.cmbno}" + "\n")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "QUANTITY", "TOTAL-AMOUNT"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        if choice == "1":
            query = "select cartid,brandname,mobilename,quantity,price from cart where customer_email=%s"
        elif choice == "2":
            query = "select cartid,brandname,mobilename,quantity,price from cart where customer_email=%s order by price"
        else:
            query = "select cartid,brandname,mobilename,quantity,price from cart where customer_email=%s order by quantity"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                    i[0], i[1], i[2], i[3], i[4]
                )
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)

    def removephonefromcart(self, email, id):
        if self.checkidfromcartemail(email, id):
            query = "DELETE FROM cart WHERE customer_email=%s AND cartid=%s"
            val = (email, id)
            self.mycursor.execute(query, val)
            self.con.commit()
            print()
            print("|-----------------------|")
            print("| Removed SuccessFully! |")
            print("|-----------------------|")
            print()
        else:
            print()
            print("|--------------------|")
            print("| Mobile Not Exists! |")
            print("|--------------------|")
            print()

    def removequantityfromcart(self, email, id, quantity):
        if self.checkidfromcartemail(email, id):
            d = Dealer()
            ok = self.getfromidcart(id, email)
            brandname = ok[0]
            mobilename = ok[1]
            q = self.getquantityfromcart(email, brandname, mobilename)
            if q > quantity:
                q = q - quantity
                price = q * d.getprice(brandname, mobilename)
                self.updatequantityprice(email, brandname, mobilename, q, price)
                print()
                print("|-----------------------|")
                print("| Removed SuccessFully! |")
                print("|-----------------------|")
                print()
            elif q == quantity:
                self.removephonefromcart(email, id)
            else:
                print()
                print("|----------------------|")
                print("| Not Sufficient Stock |")
                print("|----------------------|")
                print()
        else:
            print()
            print("|--------------------|")
            print("| Mobile Not Exists! |")
            print("|--------------------|")
            print()

    def clearwholecart(self, email):
        query = "DELETE FROM cart WHERE customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        self.con.commit()

    def getpricefromcart(self, email, brandname, mobilename):
        query = "SELECT price FROM cart WHERE customer_email=%s AND brandname=%s AND mobilename=%s"
        val = (email, brandname, mobilename)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0]

    def getquantityfromcart(self, email, brandname, mobilename):
        query = "SELECT quantity FROM cart WHERE customer_email=%s AND brandname=%s AND mobilename=%s"
        val = (email, brandname, mobilename)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0]

    def updatequantityprice(self, email, brandnmae, mobilename, quantity, price):
        query = "UPDATE cart SET quantity=%s,price=%s WHERE customer_email=%s AND brandname=%s AND mobilename=%s"
        val = (quantity, price, email, brandnmae, mobilename)
        self.mycursor.execute(query, val)
        self.con.commit()

    def checkalreadyexsistmobilefromcart(self, email, brandname, mobilename):
        isexsits = False
        query = "SELECT brandname,mobilename FROM cart WHERE customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i[0] == brandname and i[1] == mobilename:
                isexsits = True
                break
            else:
                isexsits = False
        return isexsits

    def checkid(self, id):
        isid = False
        query = "SELECT * FROM phone WHERE pid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isid = True
                break
            else:
                isid = False
        return isid

    def checkidfromcart(self, id):
        isid = False
        query = "SELECT * FROM cart WHERE cartid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isid = True
                break
            else:
                isid = False
        return isid

    def checkidfromcartemail(self, email, id):
        isid = False
        query = "SELECT * FROM cart WHERE customer_email=%s AND cartid=%s"
        val = (email, id)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isid = True
                break
            else:
                isid = False
        return isid

    def getfromid(self, id):
        query = "SELECT pbrand_name,pname,pprice FROM phone WHERE pid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0], rs[0][1], rs[0][2]

    def getfromidcart(self, id, email):
        query = "SELECT brandname,mobilename,quantity,price FROM cart WHERE cartid=%s AND customer_email=%s"
        val = (id, email)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0], rs[0][1], rs[0][2]

    def addtocart(self, email, id, quanity):
        d = Dealer()
        if self.checkid(id):
            rs = self.getfromid(id)
            brandname = rs[0]
            mobilename = rs[1]
            if d.getstock(brandname, mobilename) >= quanity:
                if self.checkalreadyexsistmobilefromcart(email, brandname, mobilename):
                    q = self.getquantityfromcart(email, brandname, mobilename)
                    quanity = quanity + q
                    price = quanity * d.getprice(brandname, mobilename)
                    self.updatequantityprice(
                        email, brandname, mobilename, quanity, price
                    )
                    print()
                    print("|-----------------------------|")
                    print("| Added To Cart SuccessFully! |")
                    print("|-----------------------------|")
                    print()
                else:
                    query = "INSERT INTO cart(customer_email,brandname,mobilename,quantity,price) VALUES(%s,%s,%s,%s,%s)"
                    price = quanity * d.getprice(brandname, mobilename)
                    val = (email, brandname, mobilename, quanity, price)
                    self.mycursor.execute(query, val)
                    self.con.commit()
                    print()
                    print("|-----------------------------|")
                    print("| Added To Cart SuccessFully! |")
                    print("|-----------------------------|")
                    print()
                q = d.getstock(brandname, mobilename)
                q = q - quanity
                d.updatestockcust(brandname, mobilename, q)
            else:
                print()
                print("|-------------------------|")
                print("| Stock Is Not Available! |")
                print("|-------------------------|")
                print()
        else:
            print()
            print("|------------------------|")
            print("| Please Enter Valid ID! |")
            print("|------------------------|")
            print()

    def getcompanymobile(self, brandname):
        query = "SELECT pid,pbrand_name,pname FROM phone WHERE pbrand_name=%s"
        val = (brandname,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            print(i[0], " - " + i[1] + " - " + i[2])

    def buy_mobiles(self, id):
        if self.checkid(id):
            amount = self.getfromid(id)[2]
            self.purchasemobile(amount)
            print()
            print("|-------------------------|")
            print("| Purchased SuccessFully! |")
            print("|-------------------------|")
            print()
        else:
            print()
            print("|----------------------------|")
            print("| Please Enter Valid Choice! |")
            print("|----------------------------|")
            print()

    def checkpin(self, inpt):
        isinput = False
        while isinput != True:
            dig = input(inpt)
            if dig.isdigit() and len(dig) == 6:
                isinput = True
            else:
                isinput = False
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
        return dig

    def purchasemobile(self, amount):
        d = Dealer()
        ischoice = False
        while ischoice != True:
            print()
            print("|------------------------------------------|")
            print("|  Enter 1 For Payment Via UPI             |")
            print("|  Enter 2 For Payment Via Credit-Card     |")
            print("|  Enter 3 For Payment Via CashOnDelivery  |")
            print("|------------------------------------------|")
            print()
            ch = input("Enter Your Choice : ")
            match ch:
                case "1":
                    print("Your Total Amount Is : ", amount)
                    d.checkdigit("Enter Your Upi Id : ")
                    self.checkpin("Enter Your Pin : ")
                    print()
                    print("|----------------------|")
                    print("| Payment SuccessFull! |")
                    print("|----------------------|")
                    print()
                    ischoice = True
                case "2":
                    print("Your Total Amount Is : ", amount)
                    d.checkdigit("Enter Your Credit Card Number : ")
                    self.checkpin("Enter Your Pin : ")
                    print()
                    print("|----------------------|")
                    print("| Payment SuccessFull! |")
                    print("|----------------------|")
                    print()
                    ischoice = True
                case "3":
                    print()
                    print(
                        "|--------------------------------------------------------------------------|"
                    )
                    print("Your Total Amount Is : ", amount)
                    print("Your Order Will Deliver On This Address : ", self.caddress)
                    print("Order Placed!")
                    print(
                        "|--------------------------------------------------------------------------|"
                    )
                    print()
                    ischoice = True
                case _:
                    print()
                    print("|----------------------------|")
                    print("| Please Enter Valid Choice! |")
                    print("|----------------------------|")
                    print()

    def create_pdf(self, id, file_path):
        query = "SELECT pbrand_name,pname,pprice,display_type,camer_sensor,camer_mp,battery_cap,processor,antutuscore,refresh_rate,speaker_type,rating FROM phone WHERE pid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        price = str(rs[0][2])
        mp = str(rs[0][5])
        ant = str(rs[0][8])
        bat = str(rs[0][6])
        ref = str(rs[0][9])
        rat = str(rs[0][11])
        s = "Company Name : " + rs[0][0]
        s1 = "Mobile Name : " + rs[0][1]
        s2 = "Price : " + price + " Rupees"
        s3 = "Display : " + rs[0][3]
        s4 = "Camera : " + mp + "MP " + rs[0][4]
        s6 = "Battery : " + bat + " MAH"
        s7 = "Processor : " + rs[0][7]
        s8 = "AntutuScore : " + ant
        s9 = "Refresh-Rate : " + ref + " HZ"
        s10 = "Speaker : " + rs[0][10]
        s11 = "Rating : " + rat
        c = canvas.Canvas(file_path, pagesize=letter)
        c.drawString(
            100, 760, "--------------------------------------------------------------"
        )
        c.drawString(140, 750, s)
        c.drawString(
            100, 740, "--------------------------------------------------------------"
        )
        c.drawString(140, 730, s1)
        c.drawString(
            100, 720, "--------------------------------------------------------------"
        )
        c.drawString(140, 710, s2)
        c.drawString(
            100, 700, "--------------------------------------------------------------"
        )
        c.drawString(140, 690, s3)
        c.drawString(
            100, 680, "--------------------------------------------------------------"
        )
        c.drawString(140, 670, s4)
        c.drawString(
            100, 660, "--------------------------------------------------------------"
        )
        c.drawString(140, 650, s6)
        c.drawString(
            100, 640, "--------------------------------------------------------------"
        )
        c.drawString(140, 630, s7)
        c.drawString(
            100, 620, "--------------------------------------------------------------"
        )
        c.drawString(140, 610, s8)
        c.drawString(
            100, 600, "--------------------------------------------------------------"
        )
        c.drawString(140, 590, s9)
        c.drawString(
            100, 580, "--------------------------------------------------------------"
        )
        c.drawString(140, 570, s10)
        c.drawString(
            100, 560, "--------------------------------------------------------------"
        )
        c.drawString(140, 550, s11)
        c.drawString(
            100, 540, "--------------------------------------------------------------"
        )
        c.save()
        os.startfile(file_path)

    def addinput(self):
        d = Dealer()
        id = d.checkdigit("Enter The Id : ")
        if self.checkid(id):
            rs = self.getfromid(id)
            brandname = rs[0]
            mobilename = rs[1]
            quantity = d.checkdigit("Enter The Quantity : ")
            quantity = int(quantity)
            if d.getstock(brandname, mobilename) >= quantity:
                print("Done")
            else:
                print("Not Done!")
        else:
            print()
            print("|------------------------|")
            print("| Please Enter Valid Id! |")
            print("|------------------------|")
            print()

    def updatecart(self, email, reply=""):
        d = Dealer()
        reply = reply.lower()
        id = d.checkdigit("Enter The Id : ")
        if self.checkidfromcart(id):
            rs = self.getfromidcart(id, email)
            brandname = rs[0]
            mobilename = rs[1]
            quantity = d.checkdigit("Enter The Quantity : ")
            quantity = int(quantity)
            if reply == "add":
                q = self.getquantityfromcart(email, brandname, mobilename)
                quantity = quantity + q
                price = quantity * d.getprice(brandname, mobilename)
                self.updatequantityprice(email, brandname, mobilename, quantity, price)
                print()
                print("|-----------------------------|")
                print("| Added To Cart SuccessFully! |")
                print("|-----------------------------|")
                print()
            elif reply == "remove" or reply == "delete":
                self.getremovecartoption()
            else:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Choice! |")
                print("|----------------------------|")
                print()

        else:
            print()
            print("|------------------------|")
            print("| Please Enter Valid Id! |")
            print("|------------------------|")
            print()

    def giverating(self, id, rat):
        sql = "select rsum,rating,counter from phone where pid=%s"
        val = (id,)
        self.mycursor.execute(sql, val)
        rs = self.mycursor.fetchone()
        s = rs[0] + rat
        insertrating = s / rs[2]
        query2 = "update phone set rsum=%s,rating=%s,counter=counter+1 where pid=%s"
        val = (s, insertrating, id)
        self.mycursor.execute(query2, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|---------------------|")
            print("| Rated SuccessFully! |")
            print("|---------------------|")
            print()

    def buynow(self, email, id):
        d = Dealer()
        if self.checkid(id):
            self.create_pdf(id, "specs.pdf")
            quantity = d.checkdigit("Enter The Quantity : ")
            quantity = int(quantity)
            rs = self.getfromid(id)
            stoc = d.getstock(rs[0], rs[1])
            if stoc >= quantity:
                q = stoc - quantity
                d.updatestockcust(rs[0], rs[1], q)
                bill = quantity * d.getprice(rs[0], rs[1])
                self.addbought(email, id)
                self.purchasemobile(bill)
            else:
                print()
                print("|----------------------|")
                print("| Stock Not Available! |")
                print("|----------------------|")
                print()
        else:
            print()
            print("|------------------------|")
            print("| Please Enter Valid Id! |")
            print("|------------------------|")
            print()

    def addbought(self, email, id):
        query = "insert into boughtphones(customer_email,pid) values(%s,%s)"
        val = (email, id)
        self.mycursor.execute(query, val)
        self.con.commit()

    def checktodaydealid(self, id):
        isid = False
        query = "SELECT * FROM todaydeal WHERE tid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isid = True
                break
            else:
                isid = False
        return isid

    def getfromtid(self, id):
        query = "SELECT pbrand_name,pname,pprice FROM todaydeal WHERE tid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0], rs[0][1], rs[0][2]

    def displaytodaydeal(self, email):
        dealer = Dealer()
        dealer.viewdeal()
        id = dealer.checkdigit("Enter The Id : ")
        if self.checktodaydealid(id):
            quantity = dealer.checkdigit("Enter The Quantity  : ")
            quantity = int(quantity)
            rs = self.getfromtid(id)
            q = dealer.getstock(rs[0], rs[1])
            if q >= quantity:
                q = q - quantity
                dealer.updatestockcust(rs[0], rs[1], q)
                bill = quantity * dealer.getprice(rs[0], rs[1])
                self.addbought(email, id)
                self.purchasemobile(bill)
            else:
                print()
                print("|----------------------|")
                print("| Stock Not Available! |")
                print("|----------------------|")
                print()
        else:
            print()
            print("|------------------------|")
            print("| Please Enter Valid Id! |")
            print("|------------------------|")
            print()

    def getbill(self, email):
        query = "select sum(price) from cart where customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0]

    def cancelorder(self, id):
        query = "delete from boughtphones where pid=%s"
        val = (id,)
        self.mycursor.execute(query, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|------------------------|")
            print("| Canceled SuccessFully! |")
            print("|------------------------|")
            print()

    def viewboughtphones(self, email):
        query = "select pid from boughtphones where customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            ok = self.getfromid(i[0])
            print(i[0], " - ", ok[0], " - ", ok[1], " - ", ok[2])

    def checkemptycart(self, email):
        isempty = True
        query = "select count(*) from cart where customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        count = self.mycursor.fetchone()[0]
        if count >= 1:
            isempty = False
        else:
            isempty = True
        return isempty

    def checkfrombought(self, email):
        isempty = True
        query = "select count(*) from boughtphones where customer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        count = self.mycursor.fetchone()[0]
        if count >= 1:
            isempty = False
        else:
            isempty = True
        return isempty

    def m3(self, name):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "PRICE", "RATING"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        query = (
            "select pid,pbrand_name,pname,pprice,rating from phone where pbrand_name=%s"
        )
        val = (name,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                    i[0], i[1], i[2], i[3], i[4]
                )
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)

    def getantutuscore(self, bname, pname):
        query = "select antutuscore from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getbattery(self, bname, pname):
        query = "select battery_cap from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getmp(self, bname, pname):
        query = "select camer_mp from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getsensor(self, bname, pname):
        query = "select camer_sensor from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getdisplay(self, bname, pname):
        query = "select display_type from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getrefreshrate(self, bname, pname):
        query = "select refresh_rate from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def getspeaker(self, bname, pname):
        query = "select speaker_type from phone where pbrand_name=%s and pname=%s"
        val = (bname, pname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchone()
        return rs[0]

    def comparison(self):
        d = Dealer()
        dis1 = 0
        dis2 = 0
        camera1 = 0
        camera2 = 0
        speaker1 = 0
        speaker2 = 0
        d.make1("1")
        cm1 = input("Enter The Name Of 1st Mobile Company Name : ")
        m1 = input("Enter The Name Of 1st Mobile Name : ")
        if d.checkalereayexistphone(cm1, m1):
            cm2 = input("Enter The Name Of 2nd Mobile Company Name : ")
            m2 = input("Enter The Name Of 2nd Mobile Name : ")
            if d.checkalereayexistphone(cm2, m2):
                if self.getantutuscore(cm1, m1) > self.getantutuscore(cm2, m2):
                    print("For Gaming You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Gaming You Can Pick " + cm2 + " - " + m2)
                if self.getmp(cm1, m1) > self.getmp(cm2, m2):
                    print("For Better Mega Pixels You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Better Mega Pixels You Can Pick " + cm2 + " - " + m2)
                if self.getrefreshrate(cm1, m1) > self.getrefreshrate(cm2, m2):
                    print("For Smooth Experience You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Smooth Experience You Can Pick " + cm2 + " - " + m2)
                if self.getbattery(cm1, m1) > self.getbattery(cm2, m2):
                    print("For Battery Purpose You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Battery Purpose You Can Pick " + cm2 + " - " + m2)
                if self.getdisplay(cm1, m1) == "poled":
                    dis1 = 3
                elif self.getdisplay(cm2, m2) == "poled":
                    dis2 = 3
                elif self.getdisplay(cm1, m1) == "amoled":
                    dis1 = 2
                elif self.getdisplay(cm2, m2) == "amoled":
                    dis2 = 2
                else:
                    dis1 = 1
                    dis2 = 1
                if self.getsensor(cm1, m1) == "sonyimx9":
                    camera1 = 5
                elif self.getsensor(cm2, m2) == "sonyimx9":
                    camera2 = 5
                elif self.getsensor(cm1, m1) == "sonyimx8":
                    camera1 = 4
                elif self.getsensor(cm2, m2) == "sonyimx8":
                    camera2 = 4
                elif self.getsensor(cm1, m1) == "sonyimx7":
                    camera1 = 3
                elif self.getsensor(cm2, m2) == "sonyimx7":
                    camera2 = 3
                elif self.getsensor(cm1, m1) == "samsunghmx2":
                    camera1 = 2
                elif self.getsensor(cm2, m2) == "samsunghmx2":
                    camera2 = 2
                if self.getspeaker(cm1, m1) == "stereo":
                    speaker1 = 1
                elif self.getspeaker(cm2, m2) == "stereo":
                    speaker2 = 1
                if dis1 >= dis2:
                    print("For Display Purpose You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Display Purpose You Can Pick " + cm2 + " - " + m2)
                if camera1 >= camera2:
                    print("For Camera Purpose You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Camera Purpose You Can Pick " + cm2 + " - " + m2)
                if speaker1 >= speaker2:
                    print("For Sound Purpose You Can Pick " + cm1 + " - " + m1)
                else:
                    print("For Sound Purpose You Can Pick " + cm2 + " - " + m2)

    def getBudgetMobile(self, price1, price2):
        game = 0
        batterycap = 0
        cameramp = 0
        dislay1 = 0
        dislay2 = 0
        dislay3 = 0
        sensor1 = 0
        sensor2 = 0
        sensor3 = 0
        sensor4 = 0
        sensor5 = 0
        if price1 > price2:
            query = "select pbrand_name,pname from phone where pprice between %s and %s"
            val = (price2, price1)
            self.mycursor.execute(query, val)
            rs = self.mycursor.fetchall()

            for i in rs:
                bname = i[0]
                mobile_name = i[1]
                if game <= self.getantutuscore(bname, mobile_name):
                    game = self.getantutuscore(bname, mobile_name)
                    gamingmobile = mobile_name

                if batterycap <= self.getbattery(bname, mobile_name):
                    batterycap = self.getbattery(bname, mobile_name)
                    batterymobile = mobile_name

                if cameramp <= self.getmp(bname, mobile_name):
                    cameramp = self.getmp(bname, mobile_name)
                    camerampmobile = mobile_name

                if self.getdisplay(bname, mobile_name) == "poled":
                    dislay1 = 3
                    dismobile1 = mobile_name
                elif self.getdisplay(bname, mobile_name) == "amoled":
                    dislay2 = 2
                    dismobile2 = mobile_name
                elif self.getdisplay(bname, mobile_name) == "lcd":
                    dislay3 = 1
                    dismobile3 = mobile_name
                if self.getsensor(bname, mobile_name) == "sonyimx9":
                    sensor1 = 5
                    camera1 = mobile_name
                elif self.getsensor(bname, mobile_name) == "sonyimx8":
                    sensor2 = 4
                    camera2 = mobile_name
                elif self.getsensor(bname, mobile_name) == "sonyimx7":
                    sensor3 = 3
                    camera3 = mobile_name
                elif self.getsensor(bname, mobile_name) == "samsunghmx2":
                    sensor4 = 2
                    camera4 = mobile_name
                else:
                    sensor5 = 1
                    camera5 = mobile_name
            print("For Gaming Purpose You Can Chose : ", gamingmobile)
            print("For Camera Mega Pixel Purpose You Can Chose : ", camerampmobile)
            print("For Battery Purpose You Can Chose : ", batterymobile)
            if dislay1 > dislay2:
                print("For Display Purpose You Can Chose : ", dismobile1)
            elif dislay2 > dislay3:
                print("For Display Purpose You Can Chose : ", dismobile2)
            else:
                print("For Display Purpose You Can Chose : ", dismobile3)
            if sensor1 > sensor2:
                print("For Camera Quality You Can Chose : ", camera1)
            elif sensor2 > sensor3:
                print("For Camera Quality You Can Chose : ", camera2)
            elif sensor3 > sensor4:
                print("For Camera Quality You Can Chose : ", camera3)
            elif sensor4 > sensor5:
                print("For Camera Quality You Can Chose : ", camera4)
            else:
                print("For Camera Quality You Can Chose : ", camera5)
        else:
            query = "select pbrand_name,pname from phone where pprice between %s and %s"
            val = (price1, price2)
            self.mycursor.execute(query, val)
            r2 = self.mycursor.fetchall()
            for i in r2:
                bname = i[0]
                mobile_name = i[1]
                if game <= self.getantutuscore(bname, mobile_name):
                    game = self.getantutuscore(bname, mobile_name)
                    gamingmobile = mobile_name

                if batterycap <= self.getbattery(bname, mobile_name):
                    batterycap = self.getbattery(bname, mobile_name)
                    batterymobile = mobile_name

                if cameramp <= self.getmp(bname, mobile_name):
                    cameramp = self.getmp(bname, mobile_name)
                    camerampmobile = mobile_name

                if self.getdisplay(bname, mobile_name) == "poled":
                    dislay1 = 3
                    dismobile1 = mobile_name
                elif self.getdisplay(bname, mobile_name) == "amoled":
                    dislay2 = 2
                    dismobile2 = mobile_name
                elif self.getdisplay(bname, mobile_name) == "lcd":
                    dislay3 = 1
                    dismobile3 = mobile_name

                if self.getsensor(bname, mobile_name) == "sonyimx9":
                    sensor1 = 5
                    camera1 = mobile_name
                elif self.getsensor(bname, mobile_name) == "sonyimx8":
                    sensor2 = 4
                    camera2 = mobile_name
                elif self.getsensor(bname, mobile_name) == "sonyimx7":
                    sensor3 = 3
                    camera3 = mobile_name
                elif self.getsensor(bname, mobile_name) == "samsunghmx2":
                    sensor4 = 2
                    camera4 = mobile_name
                else:
                    sensor5 = 1
                    camera5 = mobile_name

            print("For Gaming Purpose You Can Chose : ", gamingmobile)
            print("For Camera Mega Pixel Purpose You Can Chose : ", camerampmobile)
            print("For Battery Purpose You Can Chose : ", batterymobile)
            if dislay1 > dislay2:
                print("For Display Purpose You Can Chose : ", dismobile1)
            elif dislay2 > dislay3:
                print("For Display Purpose You Can Chose : ", dismobile2)
            else:
                print("For Display Purpose You Can Chose : ", dismobile3)
            if sensor1 > sensor2:
                print("For Camera Quality You Can Chose : ", camera1)
            elif sensor2 > sensor3:
                print("For Camera Quality You Can Chose : ", camera2)
            elif sensor3 > sensor4:
                print("For Camera Quality You Can Chose : ", camera3)
            elif sensor4 > sensor5:
                print("For Camera Quality You Can Chose : ", camera4)
            else:
                print("For Camera Quality You Can Chose : ", camera5)

    def make1(self, choice):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "PRICE", "RATING"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        if choice == "1":
            query = "select pid,pbrand_name,pname,pprice,rating from phone"
        elif choice == "33":
            query = (
                "select pid,pbrand_name,pname,pprice,rating from phone where pstock=0"
            )
        elif choice == "3":
            query = (
                "select pid,pbrand_name,pname,pprice,rating from phone order by pprice"
            )
        elif choice == "4":
            query = "select pid,pbrand_name,pname,pprice,rating from phone order by rating desc"
        elif choice == "5":
            query = "select pid,pbrand_name,pname,pprice,rating from phone order by pstock desc"
        self.mycursor.execute(query)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                    i[0], i[1], i[2], i[3], i[4]
                )
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)
