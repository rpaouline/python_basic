from sys import argv

if __name__ == "__main__":

    script_name, *params = argv

    try:
        hours = float(params[0])
        hour_rate = float(params[1])
        bonus = float(params[2])

        salary = hours * hour_rate + bonus

        print(f"Your salary for {hours} hours is {salary}!")
    except IndexError:
        print("Not enough parameters, must be at least 3!")
    except ValueError:
        print("Parameters must be integers or float!")
