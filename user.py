#user module
#menu_list={'Email':{'Full_name':'Pranay','Phone_no':8805804762,'Address':23,'Passwoed':1995000}}

import admin1 as ad
class Application:
    login_info={}
    def __init__(self,email,name,phone_no,address,password):
        self.email=email
        self.name=name
        self.phone_no=phone_no
        self.address=address
        self.password=password
        Application.login_info[self.email]={'Email':self.email,
                                            'Full_Name':self.name,
                                            'Phone_no':self.phone_no,
                                            'Address':self.address,
                                            'Password':self.password,
                                            }
        self.order_history={}

    def place_new_order(Self):
        print("what you want to order here in at the restaurent")
        ad.show_menu_item()
        choice_user=int(input("if you want to order then select 1.yes 2.no"))
        if choice_user==1:
            n=int(input("how many item do you want to order"))
            total_bill=0
            total_discount=0
            for i in range(n):
                itemid=int(input("enter the item id here:"))
                quan=int(input("enter the quantity of the item:"))
                total_bill=total_bill+ad.menu_list[itemid]['price']*quan
                total_discount+=ad.menu_list[itemid]['Discount']
                ad.menu_list[itemid]['Stock']=ad.menu_list[itemid]['Stock']-quan
                # add item in user list
                self.order_history[itemid]={"Name":ad.menu_list[itemid]["Name"],"Price":ad.menu_list[itemid]["Price"],"Quantity":quan}
            again_ask=input("confirmed ? yes otherwise no")
            if again_ask=="yes":
                print(f"total Discount allowed is{total_discount}")
                print(f"after deduced Discount it costs is {total_bill-total_discount}INR in total")
                print("you're order is successfully placed..")
            elif again_ask=="no":
                print("you order has cancelled now..")
                self.order_history.clear()
            else:
                print(" invalid input!!!")
        elif choice_user==2:
            print("you selected 2 option so we cancelled this..")
        else:
            print("invalid no  !!")
    def update_history_See(Self):
        print(self.order_history)

    def update_profile(self):
        print("update profile here--------")
        email=input("enter your mail-id")
        if email in Application.login_info.keys():
            print("email matched !!")
            del Application.login_info[email]
            #update
            new_email=input("enter new email")
            new_name=input("enter new name")
            new_phone_no=int(input("enter new phone no"))
            new_Address=input("enter new Address")
            new_password=input("enter new password")

            Application.login_info[new_email]={'Email':new_email,
                                               'Full_Name':new_name,
                                               'Phone_no':new_phone_no,
                                               'Address':new_Address,
                                               'Password':new_password,

                                               }
            print("profile update successfully------")
        else:
            print("email not registered.....please try again")

            
    @classmethod
    def login(cls,email,password):
        if email in cls.login_info.keys():
            if cls.login_info.get(email)['Password']==password:
                print(f"logged in ** successfully ** {cls.login_info.get(email)['Full_Name']}")
                return True
            else:
                print("SORRY! these are the wrong credentials")
                return False
        else:
            print(f"{email} not registered yet. first register then come again!!!")
            return False
obj=Application('pranayraipure57@gmail.com','Pranay',8805804762,'s-343','Pranay@57')


                    
        
        

