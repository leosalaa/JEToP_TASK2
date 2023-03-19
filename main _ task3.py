import json

file_name = ["blogs.json", "page.json", "products.json", "shop.json"]

for file in file_name:
    file_input = json.load(open(file, "r", encoding='utf-8'))
    print(file_input, "\n")

    file_output = {}
    with open("output files/" + file, "w") as outfile:
        json.dump(file_input, outfile, indent=4)

