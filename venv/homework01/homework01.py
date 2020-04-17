# subtask 1

greeting = "Hello, world!"
pi = 3.1415
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
cur_month = months[3]
credentials = ("username","password")

print(greeting)
print(f"Today is {cur_month}.")

name = ""
counter = 0
limit = 3
while not name and counter < limit:
    name = input("Input your name, please: \n")
    name = name.strip()
    counter += 1

if not name:
    name = "Anonym"

print(f"Hello, {name}!")

age = input("How old are you? \n")

if age.isdigit():
    age = int(age)
else:
    age = 12

if age < 16:
    print("Does your mother know that you're out?")

# subtask 2

seconds = input("Input current time in seconds: \n")
if seconds.isdigit():
    seconds = int(seconds)
    hours = seconds//3600
    time_in_seconds = seconds%3600
    minutes = time_in_seconds//60
    seconds = seconds%60
    print(f"Current time: {hours}:{minutes}:{seconds}")
else:
    print("Something went wrong.")

# subtask 3

number_n = input("Input number n from 1 to 9: \n")

if len(number_n.strip())>1:
    number_n = number_n.strip()[0]

if number_n.isdigit():
    number_n = int(number_n)
    result = 111*number_n + 11*number_n + number_n
    print(f"nnn+nn+n={result}")

# subtask 4

positive_number = input("Input positive integer number: \n")

if positive_number.isdigit():
    loop_counter = 0
    cur_digit = 0
    while loop_counter<len(positive_number):
        digit = positive_number[loop_counter]
        if int(digit) > cur_digit:
            cur_digit = int(digit)
        loop_counter += 1
    print(f"Max digit in this number is {cur_digit}.")

# subtask 5

income = input("Input your income: \n")
expense = input("Input your expense: \n")

if income.isdecimal() and expense.isdecimal():
    income = float(income)
    expense = float(expense)
    gain_loss = income - expense0
    if gain_loss<=0:
        print(f"You company is almost bankrupted! Your loss is {-gain_loss}.")
    else:
        print(f"Everything looks good! Your gain is {gain_loss}.")
        if income:
            profitability = gain_loss/income
            print(f"Profitability is {profitability}.")

        employees = input("Input number of your employees: \n")
        if employees.isdigit():
            employees = int(employees)
            if employees>0:
                gain_per_person = gain_loss/employees
                print(f"Gain per person is {gain_per_person}.")

# subtask 6

initial_distance = input("Input initial distance: \n")
target_distance = input("Input target distance: \n")

if initial_distance.isdigit() and target_distance.isdigit():
    initial_distance = int(initial_distance)
    target_distance = int(target_distance)

    current_distance = initial_distance
    target_day = 1
    while current_distance<target_distance:
        current_distance *= 1.1
        target_day +=1
    else:
        print(f"Target day is {target_day}")
