if __name__ == "__main__":
    try:
        with open("task03.txt","r") as txt_obj:
            total_employees = 0
            total_salary = 0
            for line_number, line in enumerate(txt_obj):
                try:
                    employee = line.split(" ")[0]
                    salary = float(line.split(" ")[1])
                    total_employees += 1
                    total_salary += salary
                    if salary < 20000:
                        print(f"Employee {employee} has salary {salary}")
                except IndexError:
                    print(f"In line {line_number+1} of the file must be 2 values separated by space.")
                except ValueError:
                    print(f"In line {line_number+1} of the file the second value must be numeric.")
            try:
                average_salary = total_salary/total_employees
                print(f"Average salary: {average_salary:.2f}")
            except ZeroDivisionError:
                print("There is no salary information in the file.")
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
