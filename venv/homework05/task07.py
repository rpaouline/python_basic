import json

if __name__ == "__main__":
    try:
        with open("task07.txt","r") as txt_obj:
            total_profit = 0
            total_companies = 0
            companies_dict = {}
            for line_number, line in enumerate(txt_obj):
                try:
                    splitted_line = line.split(",")
                    company = splitted_line[0]
                    revenue = int(splitted_line[2].strip())
                    expense = int(splitted_line[3].strip())
                    profit = revenue - expense

                    companies_dict[company] = profit
                    if profit > 0:
                        total_profit += profit
                        total_companies += 1
                except IndexError:
                    print(f"There is non-structured information in line {line_number+1}")
            if total_companies != 0:
                average_profit = total_profit/total_companies
            else:
                average_profit = 0
            result = [companies_dict,{"average_profit":average_profit}]

            with open("task07_new.txt","w") as new_txt_obj:
                json.dump(result,new_txt_obj)

    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
