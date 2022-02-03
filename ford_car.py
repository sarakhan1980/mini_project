import csv
with open('ford_escort.csv', 'r') as file:
    ford_file = csv.DictReader(file)
    for row in ford_file:
        print(row)
with open('ford_escort.csv', 'r') as doc:
    csv_file = csv.reader(doc)
    for row in csv_file:
        print(row)
with open('name_file.csv', 'w') as new_file:
    name = csv.writer(new_file)
    name.writerow(['First_name','Last_name', 'Age'])
    name.writerow(['Joe', 'Bloggs', '40'])
    name.writerow(['Jane', 'Smith', '50'])
with open('name_file.csv' , 'a') as file:
    data = csv.writer(file)
    name = (['Mike','Wazowki', 40])
    data.writerows(name)
# import json
# from tkinter import Menu
# #from multiprocessing.sharedctypes import Value
# #from pprint import pp, pprint


# with open('example.json', 'r') as menus:
#     list = json.load(menus)
#     menu = list.get('menu')
#     items = menu.get('id')
#     for key in id: 
#         print(key)
