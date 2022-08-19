import admin1 as admin
from user import Application
user=Application (str,str,str,str,str,)

temp_variable=1
temp=True
Temp_var=True
while Temp_var:


    inp=int(input("where you want to login? 1.admin 2.user 3.user Registration 4.Exit "))
    if temp_variable == 0:
            temp=True

    #check inp

    if inp == 1:
            print("login as admin panel..")
            username=input("enter a username")
            password=input("enter a password")
            if admin.admin_info[username]==password:
            
               print("you logged in **** successfully *******")
               while Temp_var:
                   admin_input=int(input(
                       "choose the option of admin panel 1.Add new item 2.Edit item 3.View menu list 4.Remove item 5.Exit"))

                   if admin_input==1:
                       admin.add_food_item()
                   elif admin_input==2:
                       admin_edit_food_item()
                   elif admin_input==3:
                       admin.show_menu_item()
                       
                   elif admin_input==4:
                       admin.removing_food_item()

                   elif admin_input==5:
                       print(f"you are Exit to the admin panel {username}")
                       Temp_var=False
                   else:
                        print("wrong input please read carefully instruction !!")

            else :
                print("Invalid Credentials !!!!")
                          
                        
    elif inp == 2 :
        print("login as user panel..")
        email_enter = input("enter a email")
        password = input("enter a password")

        if Application.login(email_enter,password):

            while temp:
                choice_user = int(input(f"{email_enter},enter the option 1.Place new order 2.Order history 3.Update profile 4.Exir"))
                if choice_user == 1:
                    user.place_new_order()
                elif choice_user == 2:
                    user.order_history_see()
                elif choice_user == 3:
                    user.update_profile()
                    temp=False
                    temp_variable = 0
                elif choice_user == 4:
                    print("you are successfully logged out")
                    temp=False
                    temp_variable = 0

                else:
                    print("wrong number please follow this Instruction")

        elif inp==3:
         new_email = input("enter new email")
         if new_email in user.login_info.keys():
             print("email already registered...")
         else:
                print("enter your detail here<<<<")
                new_name = input("enter new name")
                new_phone_no = int(input("enter new phone no"))
                new_Address=input("enter new Address")
                new_password=input("enter new password")
                user =Application(new_email,new_name,new_phone_no,new_Address,new_password)


                print("you have registered successfully")
                print("now you can login..")


        elif inp==4:
            Temp_var=False
            exit()
        else:
            print("Follow Option's")

                    
               
              
            
