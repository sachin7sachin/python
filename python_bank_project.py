import datetime

class bank:
    bank_name = "SBI"
    ifsc_code = "SBI1234"
    location = "hyderabad"
    no_of_customers = 0
    customer_data = {}
    transaction_data = {}

    def __init__(self,name,age,phone,aadhar,address,pin,balance):
        self.name = name
        self.age = age
        self.phone = self.validate_phone(phone)
        self.aadhar = self.validate_aadhar(aadhar)
        self.address = address
        self.pin = self.validate_pin(pin)
        self.balance = balance

        self.cust_no_increment()

        self.acc_no = 0 + self.no_of_customers
        self.storing_data(self.acc_no,self)
    
    @classmethod
    def cust_no_increment(cls):
        cls.no_of_customers += 1
    

    @classmethod
    def storing_data(cls,acc_no,object_address):
        cls.customer_data[acc_no] = object_address.__dict__

    @staticmethod
    def validate_phone(phone):
        if len(str(phone)) == 10 and str(phone).isdigit():
            return phone
        else:
            print("enter a valid phone number")

    @staticmethod
    def validate_aadhar(aadhar):
        if len(str(aadhar)) == 12 and str(aadhar).isdigit():
            return aadhar
        else:
            print("enter a valid aadhar number")

    @staticmethod
    def validate_pin(pin):
        if len(str(pin)) == 4 and str(pin).isdigit():
            return pin
        else:
            # print("enter a valid pin")
            raise Exception("invalid user")

    @classmethod
    def create_acc(cls):
        aadhar_no = int(input("enter your aadhar number: "))

        for acc_no in cls.customer_data:
            if aadhar_no == cls.customer_data[acc_no]["aadhar"]:
                break
        
        else:
            name = input("enter your name: ")
            age = int(input("enter your age: "))
            phone = int(input("enter your phone number: "))
            aadhar = aadhar_no
            address = input("enter your address")
            pin = int(input("enter your pin: "))
            min_bal = int(input("enter the amount: "))

            var = cls(name,age,phone,aadhar,address,pin,min_bal)
    

    @classmethod
    def user_balance(cls):
        print("------------------------   Balance page    --------------------------")
        acc_no = int(input("enter your account number: "))
        pin = int(input("enter your pin: "))

        if acc_no in cls.customer_data and pin == cls.customer_data[acc_no]["pin"]:
            print(f"your bank balance is {cls.customer_data[acc_no]["balance"]}")

        else:
            raise Exception("invalid user")
        
    @classmethod
    def deposit(cls,chance = 1):
        print("------------------      deposit page    -------------------------")
        
        if chance == 4:
            print("no attempts left")
            return


        acc_no = int(input("enter your account number: "))
        pin = int(input("enter your pin: "))

        if acc_no in cls.customer_data and pin == cls.customer_data[acc_no]["pin"]:

            amount = int(input("enter the amount: "))

            if amount > 0:
                cls.customer_data[acc_no]["balance"] += amount
                print(f"deposited amount {amount} and your bank balance is {cls.customer_data[acc_no]["balance"]}")

                if acc_no not in cls.transaction_data:
                    cls.transaction_data[acc_no] = [{
                        "date_time" : datetime.datetime.now(),
                        "type" : "credit",
                        "amount" : amount,
                        "balance" : cls.customer_data[acc_no]["balance"]
                    }]

                else:
                    cls.transaction_data[acc_no] += [{
                        "date_time" : datetime.datetime.now(),
                        "type" : "credit",
                        "amount" : amount,
                        "balance" : cls.customer_data[acc_no]["balance"]
                    }]
            else:
                print("invalid amount")
        else:
            print("invalid user")
            cls.deposit(chance + 1)

    @classmethod
    def withdraw(cls,chance = 1):
        print("-------------------       withdraw page     -----------------------")

        if chance == 4:
            print("no attempts left")
            return
        
        acc_no = int(input("enter your account number: "))
        pin = int(input("enter your pin: "))

        if acc_no in cls.customer_data and pin == cls.customer_data[acc_no]["pin"]:

            amount = int(input("enter the amount: "))

            if amount > 0:
                print(f"withdrawn amount {amount} and your current bank balance is {cls.customer_data[acc_no]["balance"]}")

                if acc_no not in cls.transaction_data:
                    cls.transaction_data[acc_no] = [{
                        "date_time" : datetime.datetime.now(),
                        "type" : "debit",
                        "amount" : amount,
                        "balance" : cls.customer_data[acc_no]["balance"]
                    }]
                else:
                    cls.transaction_data[acc_no] += [{
                        "date_time" : datetime.datetime.now(),
                        "type" : "debit",
                        "amount" : amount,
                        "balance" : cls.customer_data[acc_no]["balance"]
                    }]
            else:
                print("enter valid amount")
        else:
            print("invalid user")
            cls.withdraw(chance + 1)

    @classmethod
    def change_pin(cls):

        print("---------------------      change_pin_page    ----------------------")

        acc_no = int(input("enter your account number: "))
        pin = int(input("enter your pin: "))

        if acc_no in cls.customer_data and pin == cls.customer_data[acc_no]["pin"]:

            new_pin = int(input("enter your new pin: "))
            confirm_pin = int(input("enter your new pin:"))

            if new_pin == confirm_pin:
                cls.customer_data[acc_no].pin = new_pin
                print("pin changed successfully")
            else:
                print("new_pin and confirm_pin are not matching")
        else:
            print("invalid user")

    @classmethod
    def user_details_modification(cls):
        print("----------------------      user details modification page    -----------------------")

        acc_no = int(input("enter your account number: "))
        pin = int(input("enter your pin: "))

        if acc_no in cls.customer_data and pin == cls.customer_data[acc_no]["pin"]:

            print("select 1 to modify name","select 2 to modify  the phone","select 3 to modify the age",sep = "\n")

            select = int(input("enter the number: "))

            match select:
                case 1:
                    print("-----------------     modify name page  --------------------------")

                    new_name = input("enter the name: ")
                    confirm_name = input("enter the confirm_name: ")

                    if new_name == confirm_name:
                        cls.customer_data[acc_no]["name"] = new_name
                        print("name modified successfully")
                        
                    else:
                        print("new_name and confirm_name are not matching")
                    
                
                case 2:
                    print("--------------    modify phone number page  -------------------")

                    new_phone = int(input("enter the phone number: "))
                    confirm_phone = int(input("enter the confirm_phone number: "))

                    if new_phone == confirm_phone:
                        cls.customer_data[acc_no]["phone"] = new_phone
                        print("phone number modified successfully")
                    else:
                        print("new_phone and confirm_phone are not matching")

                case 3:
                    print("-----------------   modify age page   ----------------")

                    new_age = int(input("enter the age: "))
                    confirm_age = int(input("enter the confirm_age: "))

                    if new_age == confirm_age:
                        cls.customer_data[acc_no]["age"] = new_age
                        print("age modified successfully")
                    else:
                        print("new_age and confirm_ age are not matching")
                    
                case _:
                    print("please select enter a number from (1,2,3)")

        else:
            print("invalid user")

    @classmethod
    def transfer_money(cls):
        print("-------------------     transfer money page     -------------------")

        sender_acc_no = int(input("enter your account number: "))
        sender_pin = int(input("enter your pin: "))

        if sender_acc_no in cls.customer_data and sender_pin == cls.customer_data[sender_pin]["pin"]:

            receiver_acc_no = int(input("enetr receiver's account number: "))
            receiver_ifsc_code = input("enter receiver's ifsc code: ")

            if receiver_acc_no in cls.customer_data and receiver_ifsc_code == cls.ifsc_code:

                amount = int(input("enter the ammount: "))

                if amount <= cls.customer_data[sender_acc_no]["balance"]:
                    cls.customer_data[sender_acc_no]["balance"] -= amount
                    cls.customer_data[receiver_acc_no]["balance"] += amount
                    print(f"""amount {amount} has been transferred successfully to account number {receiver_acc_no}
                           and your current balance is {cls.customer_data[sender_acc_no]["balance"]} """)
                else:
                    print("insufficient blance")
            else:
                print("receiver not found")

        else:
            print("invalid user")


    @classmethod
    def mini_statement(cls):
        print("--------------------    mini statement page   -----------------")

        acc_no = int(input("enter the account number: "))
        pin = int(input("enter the pin: "))

        if acc_no in cls.customer_data and cls.customer_data[acc_no]["pin"] == pin:
            print("datetime".ljust(20),"type".ljust(15),"amount".ljust(15),"balance",sep="|")

            transaction_history = cls.transaction_data[acc_no]
            print(transaction_history)

            for d in transaction_history:
                print(d["date_time"],d["type"],str(d["amount"]),str(d["balance"]))

        else:
            print("invalid user")


o1 = bank("sachin",23,1234567890,123456789012,"nzb",1234,1234567890)
o2 = bank("sachin reddy",23,1234567890,123456789012,"nzb",1234,1234567890)


# print(o1.customer_data)

# o1.deposit()
# o1.user_details_modification()

# print(o1.transaction_data)
# o1.mini_statement()
# print(o1.customer_data)
# o1.create_acc()
# print(o1.customer_data)






        
    



