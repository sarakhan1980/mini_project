def menu_list():
    with open('menu_file.txt' , 'r+') as Menu_file:
        menu = Menu_file.readlines()
        for list in menu:
            print(list.rstrip())
    return menu
def add_menu(add_dish):
    with open('menu_file.txt', 'a') as adding_menu:
        adding_menu.writelines(add_dish + '\n')
    menu_list()
def courier_file():
    with open('courier_file.txt' ,'r+') as courier_panel:
        panel = courier_panel.readlines()
        for list in panel:
            print(list.rstrip())
    return panel
def add_staff(add_courier):
    with open('courier_file.txt', 'a') as adding_staff:
        adding_staff.writelines(add_courier + '\n')
    courier_file()