raw_input = input("Input string divided by space:\n")

i = 0
for word in raw_input.split(" "):
    if word:
        i += 1
        print(f"{i}: {word[:10]}")
