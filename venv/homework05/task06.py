if __name__ == "__main__":
    try:
        with open("task06.txt","r") as txt_obj:
            subjects = dict()
            for line_number,line in enumerate(txt_obj):
                try:
                    sub = line.split(":")[0]
                    line_hours = line.split(":")[1]
                    hours = [int(i.split("(")[0]) for i in line_hours.split(" ") if i]
                    subjects[sub] = sum(hours)
                except:
                    print(f"There is no correct information in line {line_number+1}")
            print(subjects)
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
