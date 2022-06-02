# brands = ["Samsung", "Apple", "Google"]
# products = ["Mobile", "Buds", "Watch"]
#
# for brand in brands:
#     for product in products:
#         print(brand, product)


my_list = []

for i in range(3):
    my_list.append([])
    for j in range(4):
        my_list[i].append(j)

print(my_list)