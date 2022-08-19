#ADMIN MODULE

admin_info={"Pranay":"Pranay@57"}
#stock in Resaurent
menu_list={1:{'foodId':1,'Name':'Burger','Quantity':21,'Price':30,'Discount':5,'Stock':20},
           2:{'foodId':2,'Name':'Pizza','Quantity':10,'Price':100,'Discount':7,'Stock':15},
           3:{'foodId':3,'Name':'Cake','Quantity':5,'Price':200,'Discount':0,'Stock':8},
           }
#automatic Generated
food_id=3
def add_food_item():
    global food_id
    food_id+=1
    item_name=input("enter the food item name")
    item_quantity=int(input("enter the food item quantity"))
    item_price=int(input("enter food item price"))
    item_discount=int(input("enter food item discount"))
    item_stock=int(input("enter food item stock"))

    if food_id in menu_list.key():
        print("You can't add new food item!! because ID is present already")
    else:
        menu_list[food_id]={'foodId':food_id,
                            'Name':item_name,
                            'Quantity':item_quantity,
                            'Price':item_price,
                            'Discount':item_discount,
                            'Stock':item_stock
                            }
        print("food item is successfully added")
def edit_food_item():
    """first check id then you can edit"""
    item_id=int(input("enter food item id"))
    if item_id in menu_list.key():
        print("Id is correct you can edit !!")
        item_name=input("enter food item name")
        item_quantity=int(input("enter food item quantity"))
        item_price=int(input("enter food item price"))
        item_discount=int(input("enter food item discount"))
        item_stock=int(input("enter food item stock"))
        #Update the menu
        menu_list[item_id]['Name']=item_name
        menu_list[item_id]['Quantity']=item_quantity
        menu_list[item_id]['Price']=item_price
        menu_list[item_id]['Discount']=item_discount
        menu_list[item_id]['Stock']=item_stock
        print(f"{item_id} is update successfully...!")
    else:
        print(f"{item_id} is not present inside the menu list...")
def show_menu_item():
    i=0
    for values in menu_list.values():
        i+=1
        print(i,values)
def removing_food_item():
    """check wether id here or not"""
    item_id=int(input("enter food item id"))
    if item_id in menu_list.key():
        del menu_list[item_id]
        print(f"{item_id} is deleted successfully..!")
    else:
        print(f"{item_id} is not here in menu list..")
            
        
                      
