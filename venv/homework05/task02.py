if __name__ == "__main__":
    try:
        with open("task02.txt","r") as txt_obj:
            total_lines = 0
            for line in txt_obj:
                total_lines += 1
                total_words = len(line.split(" "))
                print(f"There is {total_words} words in line {total_lines}")
            print(f"There is {total_lines} lines in file.")
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
