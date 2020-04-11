
products_list = []

product_input = "initial non-empty string"

while product_input:
    product_input = input("Input product description: (name, price, quantity, unit of measure). Press enter to exit.\n")
    product_structure = product_input.split(',')

    # check if there are enough parameters and second and third are digits (for unknown reason doesn't work for decimals)
    if len(product_structure) >= 4 and product_structure[1].isdigit() and product_structure[2].isdigit():
        products_list.append((len(products_list)+1,
                              {
                                  "name": product_structure[0],
                                  "price": int(product_structure[1]),
                                  "quantity": int(product_structure[2]),
                                  "unit": product_structure[3],
                              }
                              ))

summary = {
    "name": [],
    "price": [],
    "quantity": [],
    "unit": []
}

for product in products_list:
    for key in summary.keys():
        summary[key].append(product[1][key])

# Group unit
summary["unit"] = list(set(summary["unit"]))

for k, v in summary.items():
    print(f"{k}: {v}")
