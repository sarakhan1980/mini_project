
import function


choose_dish_message = '\n Please choose your dish from above menu you would like to replac: '
choose_courier_message = '\n Please choose your courier_name from above list you would like to replac: '
print("\n\t\t\t\t\Wellcome ! to the Yorshire Resturant ")
print("*" * 120)
while True:
    user_input = int(input("""\n-------------Main App Menu-------------\n
    1: Resturant Menu
    2: Courier List 
    0: Exit
    \nPlease select your corresponding number: """))
    if user_input == 0:
        print("\nThanks for using our services.Have a great day.\n")
        break
    elif user_input == 1:
        while True:
            print("\n----------Here is your Resturant Panel----------")
            Resturant_panel_list = int(input("""
    1: Print Main Menu
    2: Add New Menu
    3: Update Existing Menu
    4: Delete Product
    0: Exit from Panel
    \nPlease enter the corresponding number: """))
            if Resturant_panel_list == 1:
                print('\nHere is your Menu List\n')
                function.menu_list()
            elif Resturant_panel_list == 2:
                new_dish = input('\n Please Add your dish in menu: ')
                #dish_price = float(input('\n please enter the dish price:  '))
                #dish_dict = {'name': new_dish, 'price' : dish_price}
                #function.menu_list(dish_dict)
                function.add_menu(new_dish.rstrip())
            elif Resturant_panel_list == 0:
                print('\n----------You are back to "Main Menu App----------')
                break
            elif Resturant_panel_list == 3:
                found_item = False
                new_menu = function.menu_list()
                old_menu = input(choose_dish_message)
                amended_dish = input('\n Please enter your dish here : ')
                for index in range(0, len(new_menu)):
                    if new_menu[index].rstrip() == old_menu:
                        new_menu[index] = amended_dish + '\n'
                        found_item = True
                if found_item == True:
                    print('\nThis is your updated menu list.')
                else:
                    print('\nEntered dish is not avaible in menu. ')
                with open('menu_file.txt', 'w+', newline='') as menu_file:
                    menu_file.writelines(new_menu)
                function.menu_list()
            elif Resturant_panel_list == 4:
                removing_menu = function.menu_list()
                delete_menu = input(
                    '\n Please enter the dish you would like to remove : ')
                removing_menu.remove(delete_menu + '\n')
                with open('menu_file.txt', 'w+', newline='') as menu_file:
                    menu_file.writelines(removing_menu)
                function.menu_list()
                #print(removing_menu)
                #break
    elif user_input == 2:
        while True:
            print("\n----------Here is your Courier Panel----------")
            Courier_panel_list = int(input("""
            1: Print Courier List
            2: Add New Staff
            3: Update Existing Courier List
            4: Delete Staff Name
            0: Exit from Panel
            \nPlease enter the corresponding number: """))
            if Courier_panel_list == 1:
                print('\n Here is your Courier List')
                function.courier_file()
            elif Courier_panel_list == 2:
                new_staff = input('\n Please Add new staff in list: ')
                function.add_staff(new_staff.rstrip())
            elif Courier_panel_list == 0:
                print('\n----------You are back to "Main Menu App----------')
                break
            elif Courier_panel_list == 3:
                found_item = False
                update_staff = function.courier_file()
                choose_staff = input(choose_courier_message)
                amended_list = input(
                    '\n Please enter your courier name here : ')
                for index in range(0, len(update_staff)):
                    if update_staff[index].rstrip() == choose_staff:
                        update_staff[index] = amended_list + '\n'
                        found_item = True
                if found_item == True:
                    print('\nThis is your updated staff list.')
                else:
                    print('\nEntered name is not avaible in list. ')
                with open('courier_file.txt', 'w+', newline='') as menu_file:
                    menu_file.writelines(update_staff)
                function.courier_file()
            elif Courier_panel_list == 4:
                staff_names = function.courier_file()
                delete_staff_name = input(
                    '\n Please choose the courier name you would like to remove : ')
                staff_names.remove(delete_staff_name + '\n')
                with open('courier_file.txt', 'w+', newline='') as courier_remove:
                    courier_remove.writelines(staff_names)
                function.courier_file()
            else:
                print('Invalid Entry')
