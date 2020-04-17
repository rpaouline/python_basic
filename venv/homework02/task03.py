
month_number = 0

while not month_number:
    month_number = input("Input month number (1-12)\n")
    if month_number.isdigit():
        month_number = int(month_number)

        if month_number < 1 or month_number > 12:
            month_number = 0
    else:
        month_number = 0

# list

months_list = ["Winter",
               "Winter",
               "Spring",
               "Spring",
               "Spring",
               "Summer",
               "Summer",
               "Summer",
               "Fall",
               "Fall",
               "Fall",
               "Winter",
               ]

print(months_list[month_number-1])

# dict

months_dict = {1:"Winter",
               2:"Winter",
               3:"Spring",
               4:"Spring",
               5:"Spring",
               6:"Summer",
               7:"Summer",
               8:"Summer",
               9:"Fall",
               10:"Fall",
               11:"Fall",
               12:"Winter",
               }

print(months_dict[month_number])
