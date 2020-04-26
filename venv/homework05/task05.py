from random import randint

if __name__ == "__main__":
    try:
        with open("task05.txt","w") as txt_obj:
            numbers = [randint(0,100) for _ in range(20)]
            for n in numbers:
                txt_obj.write(str(n))
                txt_obj.write(" ")

        with open("task05.txt","r") as txt_obj:
            content = txt_obj.readline()
            numbers = [int(i) for i in content.split(" ") if i]
            print(sum(numbers))
    except IOError:
        print("Unable to open the file.")
    except:
        print("Something went wrong.")
