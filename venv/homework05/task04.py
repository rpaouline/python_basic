if __name__ == "__main__":
    num_dict = {"one":"один","two":"два","three":"три","four":'четыре'}
    try:
        with open("task04.txt","r") as txt_obj:
            try:
                with open("task04_new.txt","w") as new_txt_obj:
                    for line in txt_obj:
                        splitted_line = line.split(" - ")
                        splitted_line[0] = num_dict[splitted_line[0].lower()].capitalize()
                        new_line = " - ".join(splitted_line)
                        new_txt_obj.write(new_line)
            except IOError:
                print("Unable to open a new file.")
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
