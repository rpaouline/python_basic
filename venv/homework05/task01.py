if __name__ == "__main__":
    try:
        with open("task01.txt","w") as txt_obj:
            while True:
                new_line = input("Input a line. To break, input an empty line:\n")
                if new_line:
                    txt_obj.write(new_line)
                    txt_obj.write("\n")
                else:
                    break
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
