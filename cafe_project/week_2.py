
def menu_list():
            with open('menu_file.txt' , 'r') as Menu_file:
                menu = Menu_file.readlines()
                for list in menu:
                    print(list.rstrip())
                    #Menu_file.close()
def add_menu(add_dish):
    with open('menu_file.txt', 'a') as adding_menu:
        adding_menu.write(add_dish)
    menu_list()


print("\n\t\t\t\t\t\t\tWellcome ! to the Yorshire Resturant ")
print("*" * 145)
while True:
        user_input = int(input("""\n-------------Main App Menu-------------\n
        1: Resturant Menu
        2: Courier List 
        0: Exit
        \nPlease select your corresponding number: """))
        if user_input== 0:
            print("\nThanks for using our services.Have a great day.\n")
            break
        elif user_input == 1:
            while True :
                print("\n----------Here is your Resturant Panel----------")
                Resturant_panel_list = int(input("""
        1-(Print Main Menu) 
        2-(Add New Menu) 
        3-(Update Existing Menu) 
        4-(Delete Product) 
        5-(Go to Courier Panel) 
        0-(Exit from Panel)
        \nPlease enter the corresponding number: """))
                #while True :
                if Resturant_panel_list == 1:
                            print('\nHere is your Menu List: ')
                            menu_list()
                elif Resturant_panel_list == 2:
                            new_dish = input('\n Please Add your dish in menu: ')
                            add_menu(new_dish.strip())

        elif user_input== 2 :
            print("\n----------Here is your Courier Panel----------")
            Courier_panel_list = input("""
        1-(Print Courier List) 
        2-(Add New Staff) 
        3-(Update Existing Courier List) 
        4-(Delete Staff Name) 
        5-(Go to Resturant Panel)
        0-(Exit from Panel) 
        \nPlease enter the corresponding number: """)
                # if Courier_panel_list == 1:
                #     def courier_list():
                #         return courier_list
                # staff = open("courier_file.txt", "r+")
                # list = staff.readlines()
                # for item in list:
                #     print(item.rstrip())
                    
        # def menu_list():
        #     with open('menu_file.txt' , 'r') as Menu_file:
        #         menu = Menu_file.readlines()
        #         for list in menu:
        #             print(list.rstrip)
            


    





        
