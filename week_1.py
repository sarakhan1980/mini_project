from os import remove

print('\n')
print("Welcome to 'Cafe Yorkshire', here is your menu! \n") 

main_menu = ["Latte", "Cafe Mocha","Cappuccino","Cafe Tea", "Espresso"] # MAin_menu_list
print(main_menu)

while True:
    # Panel
    user_input =int(input(""" \n Choose your option : 
    \t\t0 - exit Menu
    \t\t1 - go to the product list
    what would you like to do? """)) 
    
    if user_input == 0:
        print("thank you! you are exit")
        break
    elif user_input == 1:   
        while True:
        # Product list
            print("\nHere is your product Options: ")
            
            product_list = input("""
    \t\t(1-Print Main Menu) 
    \t\t(2-Add New Menu) 
    \t\t(3-Update Existing Menu) 
    \t\t(4-Delete Product) 
    \t\t(0-Return to panel) 
    \nPlease enter the corresponding number: """)

            if product_list == "0" : # Return back panel
                print("\nYou'r back to the panel")
                break
            elif product_list == "1": # print Main_menu_list
                print("\nWhat would you like to have today!" , main_menu)
            elif product_list == "2": # Add new drink in Main_menu_list
                add_new_drink = input("\nplease add new drink in your list : ")
                main_menu.append(add_new_drink)
                print(main_menu)
            elif product_list == "3" : # Replace existing Main_menu_list
                for item in main_menu:
                    print(main_menu.index(item),  item) 
                existing_drink = int(input('\n Please enter the number of the drink you would like to update: '))
                updated_drink = input("\n Please enter the new drink name: ")
                main_menu [existing_drink] = updated_drink
                print('\n', main_menu)
            elif product_list == "4" : # Delete Item from Main_menu_list
                for drinks in main_menu:
                    print(main_menu.index(drinks), drinks)
                del_drink = input('\n Please enter the drink you would like to remove: ')
                main_menu.remove(del_drink)
                print('\n',main_menu)
            else:
                print("\nInvalid option") 
                
    