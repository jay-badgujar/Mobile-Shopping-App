import os
from tkinter import filedialog
import tkinter as tk
import mysql.connector
import random
import matplotlib.pyplot as plt
import numpy as np


class Dealer:
    def __init__(self) -> None:
        self.con = mysql.connector.connect(
            host="localhost", user="root", password="", database="m11"
        )
        self.mycursor = self.con.cursor()

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
            ispasword = False
        return ispasword

    def forgotpass(self, email, newpassc):
        query = "update d_info set dealer_password=%s where dealer_email=%s"
        val = (newpassc, email)
        self.mycursor.execute(query, val)
        self.con.commit()

    def checkemail(self, email):
        isemail = False
        query = "select * from d_info where dealer_email=%s"
        val = (email,)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                isemail = True
        return isemail

    def checkemailpass(self, email, pasc):
        islogin = False
        query = "select * from d_info where dealer_email=%s and dealer_password=%s"
        val = (email, pasc)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                islogin = True
        return islogin

    def dealer_login(self):
        dealer_email = "dealer@gmail.com"
        dealer_mobileno = "7123456789"
        islogin = False
        isemail = False
        while isemail != True:
            email = input("Enter Your E-mail : ")
            if email == dealer_email:
                ispass = False
                while ispass != True:
                    passc = input("Enter Your Password : ")
                    if self.checkemailpass(email, passc):
                        print()
                        print("|---------------------|")
                        print("| Login SuccessFully! |")
                        print("|---------------------|")
                        print()
                        ispass = isemail = True
                    else:
                        ispass = isemail = False
                        print()
                        print("|------------------------------|")
                        print("| Please Enter Valid Password! |")
                        print("|------------------------------|")
                        print()
                        answer = input("Did You Forgot Your Password?")
                        if answer.lower() == "yes":
                            isnumber = False
                            while isnumber != True:
                                number = input("Enter Your Registered MobileNumber : ")
                                if dealer_mobileno == number:
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
                                    print("| Login SuccessFully! |")
                                    print("|---------------------|")
                                    print()
                                    isnewp = ispass = isemail = True
                                else:
                                    isnewp = ispass = isemail = False
            else:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid E-Mail! |")
                print("|----------------------------|")
                print()
        islogin = True
        return islogin

    def checkalpha(self, inpt):
        isinput = False
        while isinput != True:
            alph = input(inpt)
            if alph.isalpha():
                isinput = True
            else:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
                isinput = False
        return alph

    def checkdigit(self, inpt):
        isinput = False
        while isinput != True:
            dig = input(inpt)
            if dig.isdigit():
                isinput = True
            else:
                isinput = False
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
        return dig

    def checkalphadig(self, inpt):
        isinput = False
        while isinput != True:
            digalph = input(inpt)
            if digalph.isalnum():
                isinput = True
            else:
                isinput = False
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
        return digalph

    def checkalphadigcomp(self, inpt):
        isinput = False
        while isinput != True:
            digalph = input(inpt)
            count1 = count2 = 0
            for i in digalph:
                if i.isdigit():
                    count1 = 1
                elif i.isalpha():
                    count2 = 1
                else:
                    count1 = count2 = 0
            if count1 == 1 and count2 == 1:
                isinput = True
            else:
                isinput = False
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
        return digalph

    def isfloat(self, statement):
        isnumber = False
        while isnumber != True:
            number = input(statement)
            count = 0
            count1 = 0
            for i in number:
                if i.isdigit():
                    count += 1
                elif i == "." and count > 0:
                    count1 += 1
            if count == len(number) - 1 and count1 == 1:
                isnumber = True
            elif count == len(number) and count1 == 0:
                isnumber = True
            else:
                print()
                print("|----------------------------|")
                print("| Please Enter Valid Detail! |")
                print("|----------------------------|")
                print()
                isnumber = False
        return number

    def checkmobileexists(self, brandname, mobilename):
        ismobile = False
        query = "select * from phone where pbrand_name=%s and pname=%s"
        val = (brandname, mobilename)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        for i in rs:
            if i != "":
                ismobile = True
        return ismobile

    def addPhone(self):
        isexists = False
        while isexists != True:
            isbrand = False
            while isbrand != True:
                print(
                    "Brands Available Are : Apple,Samsung,OnePlus,Oppo,Vivo,Redmi,Realme"
                )
                brand_name = self.checkalpha("Enter The Brand Name : ")
                brand_name = brand_name.lower()
                if (
                    brand_name == "apple"
                    or brand_name == "samsung"
                    or brand_name == "oneplus"
                    or brand_name == "vivo"
                    or brand_name == "oppo"
                    or brand_name == "redmi"
                    or brand_name == "realme"
                ):
                    isbrand = True
                else:
                    print()
                    print("|--------------------------------|")
                    print("| Please Enter Valid Brand Name! |")
                    print("|--------------------------------|")
                    print()
                    isbrand = False
            mobile_name = self.checkalphadigcomp("Enter The Mobile Name : ")
            if self.checkmobileexists(brand_name, mobile_name):
                print()
                print("|------------------------|")
                print("| Mobile Already Exists! |")
                print("|------------------------|")
                print()
                isexists = False
            else:
                isexists = True
        mobile_price = self.isfloat("Enter The Mobile Price : ")
        mobile_stock = self.checkdigit("Enter The Mobile Stock : ")
        mobile_display = self.checkalpha("Enter The Mobile Display Type : ")
        mobile_csensor = self.checkalphadigcomp("Enter The Mobile Camera Sensor : ")
        mobile_cmp = self.checkdigit("Enter The Mobile Camera Mega-Pixels : ")
        mobile_battery = self.checkdigit("Enter The Mobile Battery Capacity : ")
        mobile_processor = self.checkalphadigcomp("Enter The Mobile Processor Name : ")
        mobile_antutu = self.checkdigit("Enter The Mobile Antutu-Score : ")
        mobile_refreshrate = self.checkdigit("Enter The Mobile Refresh-Rate : ")
        mobile_speaker = self.checkalpha("Enter The Mobile Speaker Type : ")
        rating = 0
        count = 0
        brand_name = brand_name.lower()
        mobile_name = mobile_name.lower()
        mobile_display = mobile_display.lower()
        mobile_csensor = mobile_csensor.lower()
        mobile_processor = mobile_processor.lower()
        mobile_speaker = mobile_speaker.lower()
        query = "INSERT INTO phone(pbrand_name,pname,pprice,pstock,display_type,camer_sensor,camer_mp,battery_cap,processor,antutuscore,refresh_rate,speaker_type,rsum,rating,counter)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (
            brand_name,
            mobile_name,
            mobile_price,
            mobile_stock,
            mobile_display,
            mobile_csensor,
            mobile_cmp,
            mobile_battery,
            mobile_processor,
            mobile_antutu,
            mobile_refreshrate,
            mobile_speaker,
            0,
            rating,
            count,
        )
        self.mycursor.execute(query, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|------------------------|")
            print("| Inserted SuccessFully! |")
            print("|------------------------|")
            print()

    def removephone(self):
        iscompany = False
        while iscompany != True:
            company_name = self.checkalpha("Enter Company Name : ")
            mobile_name = self.checkalphadigcomp("Enter Mobile Name : ")
            company_name = company_name.lower()
            mobile_name = mobile_name.lower()
            if self.checkmobileexists(company_name, mobile_name):
                iscompany = True
            else:
                print()
                print("|--------------------|")
                print("| Mobile Not Exists! |")
                print("|--------------------|")
                print()
                iscompany = False
        query = "DELETE FROM phone WHERE pbrand_name=%s AND pname=%s"
        val = (company_name, mobile_name)
        self.mycursor.execute(query, val)
        self.con.commit()
        # cust.removephonefromcart()
        # cust.cancelorder()
        # self.removefromdeal()
        if self.mycursor.rowcount > 0:
            print()
            print("|-----------------------|")
            print("| Deleted SuccessFully! |")
            print("|-----------------------|")
            print()

    def addtodaydeal(self):
        company_name = input("Enter Company Name : ")
        mobile_name = input("Enter Mobile Name : ")
        company_name = company_name.lower()
        mobile_name = mobile_name.lower()
        if self.checkmobileexists(company_name, mobile_name):
            print("Current Price is : ", self.getprice(company_name, mobile_name))
            newprice = self.isfloat("Enter New Price : ")
            price = self.getprice(company_name, mobile_name)
            query = "INSERT INTO todaydeal(pbrand_name,pname,pprice,oprice) VALUES(%s,%s,%s,%s)"
            val = (company_name, mobile_name, newprice, price)
            self.mycursor.execute(query, val)
            self.con.commit()
            self.updateprice(company_name, mobile_name, newprice)
            if self.mycursor.rowcount > 0:
                print()
                print("|------------------------|")
                print("| Inserted SuccessFully! |")
                print("|------------------------|")
                print()
        else:
            print()
            print("|--------------------|")
            print("| Mobile Not Exists! |")
            print("|--------------------|")
            print()

    def removefromdeal(self):
        company_name = input("Enter Company Name : ")
        mobile_name = input("Enter Mobile Name : ")
        company_name = company_name.lower()
        mobile_name = mobile_name.lower()
        if self.checkmobileexists(company_name, mobile_name):
            query = "select oprice from todaydeal where pbrand_name=%s and pname=%s"
            val = (company_name, mobile_name)
            self.mycursor.execute(query, val)
            rs = self.mycursor.fetchone()
            oprice = rs[0]
            query = "DELETE FROM todaydeal WHERE pbrand_name=%s AND pname=%s"
            val = (company_name, mobile_name)
            self.mycursor.execute(query, val)
            self.con.commit()
            self.updateprice(company_name, mobile_name, oprice)
            if self.mycursor.rowcount > 0:
                print()
                print("|-----------------------|")
                print("| Deleted SuccessFully! |")
                print("|-----------------------|")
                print()
        else:
            print()
            print("|--------------------|")
            print("| Mobile Not Exists! |")
            print("|--------------------|")
            print()

    def updateprice(self, brand_name="", mobile_name="", price=0):
        brand_name = brand_name.lower()
        mobile_name = mobile_name.lower()
        query = "UPDATE phone SET pprice=%s WHERE pbrand_name=%s AND pname=%s"
        val = (price, brand_name, mobile_name)
        self.mycursor.execute(query, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|-----------------------------|")
            print("| Updated Price SuccessFully! |")
            print("|-----------------------------|")
            print()

    def updatestock(self, brand_name="", mobile_name="", stock=0):
        brand_name = brand_name.lower()
        mobile_name = mobile_name.lower()
        query = "UPDATE phone SET pstock=%s WHERE pbrand_name=%s AND pname=%s"
        val = (stock, brand_name, mobile_name)
        self.mycursor.execute(query, val)
        self.con.commit()
        if self.mycursor.rowcount > 0:
            print()
            print("|-----------------------------|")
            print("| Updated Stock SuccessFully! |")
            print("|-----------------------------|")
            print()

    def updatestockcust(self, brand_name="", mobile_name="", stock=0):
        brand_name = brand_name.lower()
        mobile_name = mobile_name.lower()
        query = "UPDATE phone SET pstock=%s WHERE pbrand_name=%s AND pname=%s"
        val = (stock, brand_name, mobile_name)
        self.mycursor.execute(query, val)
        self.con.commit()

    def checkalereayexistphone(self, brandname, mobilename):
        isexsits = False
        query = "SELECT pbrand_name,pname FROM phone"
        self.mycursor.execute(
            query,
        )
        rs = self.mycursor.fetchall()
        for i in rs:
            if i[0] == brandname and i[1] == mobilename:
                isexsits = True
                break
            else:
                isexsits = False
        return isexsits

    def getstock(self, bname="", mname=""):
        bname = bname.lower()
        mname = mname.lower()
        query = "SELECT pstock FROM phone WHERE pbrand_name=%s AND pname=%s"
        val = (bname, mname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0]

    def getprice(self, bname, mname):
        bname = bname.lower()
        mname = mname.lower()
        query = "SELECT pprice FROM phone WHERE pbrand_name=%s AND pname=%s"
        val = (bname, mname)
        self.mycursor.execute(query, val)
        rs = self.mycursor.fetchall()
        return rs[0][0]

    # def viewbyallstock(self):
    #     query = "SELECT pbrand_name,pname,pstock FROM phone"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0] + " - " + i[1] + " - ", i[2])

    # def viewbyallprice(self):
    #     query = "SELECT pbrand_name,pname,pprice FROM phone"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0] + " - " + i[1] + " - ", i[2])

    # def viewmobiles(self):
    #     query = "SELECT pid,pbrand_name,pname FROM phone"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0], " - ", i[1], " - " + i[2])

    # def viewmobilessortbyprice(self):
    #     query = "SELECT pid,pbrand_name,pname,pprice FROM phone ORDER BY pprice"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0], " - " + i[1] + " - ", i[2], " - ", i[3])

    # def viewmobilessortbyratings(self):
    #     query = "SELECT pid,pbrand_name,pname,pprice,rating FROM phone ORDER BY rating"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0], " - " + i[1] + " - ", i[2], " - ", i[3], " - ", i[4])

    # def viewmobilessortbystock(self):
    #     query = "SELECT pbrand_name,pname,pstock FROM phone ORDER BY pstock DESC"
    #     self.mycursor.execute(query)
    #     rs = self.mycursor.fetchall()
    #     for i in rs:
    #         print(i[0] + " - " + i[1] + " - ", i[2])

    def viewsales(self):
        query = "SELECT pbrand_name,totalsale FROM sales"
        self.mycursor.execute(query)
        rs = self.mycursor.fetchall()
        cname = []
        sale = []
        for i in rs:
            cname.append(i[0])
            sale.append(i[1])
        plt.pie(sale, labels=cname, autopct="%.1f%%")
        plt.legend(title="Companies", loc="upper left", bbox_to_anchor=(1, 0.5))
        plt.show()

    def make1(self, choice):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "PRICE", "STOCK", "RATING"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        if choice == "1":
            query = "select pid,pbrand_name,pname,pprice,pstock,rating from phone"
        elif choice == "33":
            query = "select pid,pbrand_name,pname,pprice,pstock,rating from phone where pstock=0"
        elif choice == "3":
            query = "select pid,pbrand_name,pname,pprice,pstock,rating from phone order by pprice"
        elif choice == "4":
            query = "select pid,pbrand_name,pname,pprice,pstock,rating from phone order by rating desc"
        elif choice == "5":
            query = "select pid,pbrand_name,pname,pprice,pstock,rating from phone order by pstock desc"
        self.mycursor.execute(query)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                    i[0], i[1], i[2], i[3], i[4], i[5]
                )
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)

    def m2(self):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "PRICE"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        query = "select pid,pbrand_name,pname,pprice from phone"
        self.mycursor.execute(query)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25}\n".format(i[0], i[1], i[2], i[3])
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)

    def m22(self):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "STOCK"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        query = "select pid,pbrand_name,pname,pstock from phone"
        self.mycursor.execute(query)
        rs = self.mycursor.fetchall()
        for i in rs:
            f.write(
                "{:^25} || {:^25} || {:^25} || {:^25}\n".format(i[0], i[1], i[2], i[3])
            )
        f.write("\n\n")
        f.write(157 * "-")
        f.close()
        os.startfile(file)

    def viewdeal(self):
        file = "JP.txt"
        f = open(file, "w")
        f.write(157 * "-")
        f.write(157 * "-" + "\n\n\n")
        f.write(157 * "-" + "\n\n")
        f.write(
            "{:^25} || {:^25} || {:^25} || {:^25} || {:^25}\n".format(
                "ID", "BRAND-NAME", "MOBILE-NAME", "SALE-PRICE", "ORIGINAL-PRICE"
            )
        )
        f.write("\n")
        f.write(157 * "-")
        f.write("\n")
        query = "select tid,pbrand_name,pname,pprice,oprice from todaydeal"
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