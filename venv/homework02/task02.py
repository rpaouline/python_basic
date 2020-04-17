raw_input = input("Input list divided by comma:\n")

raw_list = raw_input.split(',')

# Let's do it in-place

boundary = len(raw_list)//2
i = 0

while i < boundary:
    raw_list[2*i],raw_list[2*i+1]=raw_list[2*i+1],raw_list[2*i]
    i+=1

print(raw_list)
