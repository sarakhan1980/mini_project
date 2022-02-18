import csv

# REUSABLE FUNCTIONS
def read_csv(file_name):
    data = []
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def write_csv(file_name, data):
    with open(file_name, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def update_order(orders):
    for index, order in enumerate(orders):
        print(index, order)

    chosen_order_index = int(input("pick an order: "))

    for index, status in enumerate(statuses):
        print(index, status)

    chosen_status_index = int(input("pick a status: "))

    orders[chosen_order_index]["status"] = statuses[chosen_status_index]

    return orders


# GLOBAL VARIABLES
products = ["coke", "fanta"]
couriers = ["john"]
statuses = ["preparing", "out-for-delivery", "delivered"]
orders = read_csv("orders.csv")


# App
update_order(orders)
write_csv("orders.csv", orders)
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)

    employee_writer.writerow(['John Smith', 'Accounting', 'November', 67493229])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March', 9473949647])
# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')
with open('employee_file2.csv', mode='w') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})