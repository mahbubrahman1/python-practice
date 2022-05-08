

car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020}
print(car)


car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020}
print(car["Model"])


car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
result = car["Year"]
print(result)


# === amra caile evabe o likhte pari


Computer = {
    "CPU" : "Intel",
    "SSD" : "Corsair",
    "Motherboard" : "Gigabyte",
    "Case" : "NZXT"
}

print(Computer)




Computer = {
    "CPU" : "Intel",
    "SSD" : "Corsair",
    "Motherboard" : "Gigabyte",
    "Case" : "NZXT"
}

print(Computer["SSD"])




car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
x = car.get("Year")
print(x)



phone = {
    "Brand" : "Samsung",
    "Model" : "Note20 Ultra",
    "Storage" : "RAM & ROM - 12GB & 512GB",
    "Processor" : "SD888"
}
print(phone.get("Model"))





'''=== print all keys'''

car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
for x in car:
    print(x)


car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
for x in car.keys():
    print(x)




'''=== print values all values'''

car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
for x in car:
    print(car[x])



car = {"Brand" : "Audi", "Model" : "A6", "Year" : 2020, "Registration" : 2021}
for x in car.values():
    print(x)



car = {
    "Brand" : "Audi",
    "Model" : "A6",
    "Year" : 2020,
    "Registration" : 2021
}

for i in car:
    print(car[i])




'''=== print the values in the dictionary along with keys...'''


car = {"Brand:" : "Audi", "Model:" : "A6", "Year:" : 2020, "Registration:" : 2021}
for x, y in car.items():
    print(x, y)


car = {
    "Brand:" : "Audi",
    "Model:" : "A6",
    "Year:" : 2020,
    "Registration:" : 2021
}
for m, n in car.items():
    print(m, n)




'''=== add keys and values'''


roll = {}
roll["Jack"] = 56
roll["Rose"] = 34
roll["Icson"] = 65
roll["Bell"] = 32
print(roll)



name = {'Name' : 'Mahbub', 'Age' : 18, 'Study' : 'CSE', 'Location' : 'Moulvibazar'}
name['Birth'] = 2002
print(name)



car = {
    "Brand" : "Audi",
    "Model" : "A6",
    "Year" : 2020,
    "Registration" : 2021
}
car["Made in"] = "Germany"
print(car)




name = {'Name' : 'Mahbub', 'Age' : 18, 'Study' : 'CSE', 'Location' : 'Moulvibazar'}
name['Birth'] = 2002
print(name)




'''#=== change value'''

name = {'Name' : 'Mahbub', 'Age' : 18, 'Study' : 'CSE', 'Location' : 'Moulvibazar'}
name['Study'] = 'CSE in BUET'
print(name)




roll = {
    "Jhon" : 80,
    "Mark" : 50,
    "Rose" : 40,
    "Jack" : 60,
    "Bill" : 30,
}
roll["Rose"] = 90
print(roll)



'''=== delete/remove value'''


roll = {"Jhon" : 80, "Mark" : 50, "Rose" : 40, "Jack" : 60, "Bill" : 30}
del roll["Jack"]
print(roll)




roll = {
    "Jhon" : 80,
    "Mark" : 50,
    "Rose" : 40,
    "Jack" : 60,
    "Bill" : 30,
}
del roll["Mark"]
print(roll)



'''=== type'''

roll = {1 : 80, 2 : 50, 3 : 40, 4 : 60, 5 : 30}
print(type(roll))


roll = {"Jhon" : 80, "Mark" : 50, "Rose" : 40, "Jack" : 60, "Bill" : 30}
print(type(roll))


"""=== === === ==="""



marks = {"Jhon": {"Bangla": 74, "English": 73}, "Bill": {"Bangla": 70, "English": 75}}
print(marks["Bill"])



marks = {
    "Jhon" : {"Bangla" : 74, "English" : 73},
    "Bill" : {"Bangla" : 70, "English" : 75},
    "Icson" : {"Bangla" : 67, "English" : 80}
}
print(marks["Icson"])



marks = {
    "Jhon" : {"Bangla" : 74, "English" : 73},
    "Bill" : {"Bangla" : 70, "English" : 75},
    "Icson" : {"Bangla" : 67, "English" : 80}
}
print(marks["Bill"])



bd_division_info = {
    "Dhaka" : {"District": 13, "Upazila": 93, "Union": 1833},   
    "Sylhet" : {"District": 4, "Upazila": 38, "Union": 334},   
    "Barishal" : {"District": 6, "Upazila": 39, "Union": 333},   
    "Chittagong" : {"District": 11, "Upazila": 97, "Union": 336},   
    "Khulna" : {"District": 10, "Upazila": 59, "Union": 270},   
    "Mymensingh" : {"District": 4, "Upazila": 34, "Union": 350},   
    "Rajshahi" : {"District": 8, "Upazila": 70, "Union": 558},   
    "Rangpur" : {"District": 4, "Upazila": 38, "Union": 536}   
}
print(bd_division_info["Sylhet"])








bd_division_info = {}

bd_division_info["Dhaka"] = {"District": 13, "Upazila": 93, "Union": 1833}
bd_division_info["Sylhet"] = {"District": 4, "Upazila": 38, "Union": 334}
bd_division_info["Khulna"] = {"District": 10, "Upazila": 59, "Union": 270}
bd_division_info["Rangpur"] = {"District": 4, "Upazila": 38, "Union": 536}
bd_division_info["Barishal"] = {"District": 6, "Upazila": 39, "Union": 333}
bd_division_info["Rajshahi"] = {"District": 8, "Upazila": 70, "Union": 558}
bd_division_info["Mymensingh"] = {"District": 4, "Upazila": 34, "Union": 350}


print(bd_division_info)


print(bd_division_info["Khulna"])


divisions = bd_division_info.keys()
print(divisions)


for i in bd_division_info:
    print(i)


for division in divisions:
    print(division, "Upazila", bd_division_info[division]["Upazila"])


for m, n in bd_division_info.items():
    print(m, n)


del bd_division_info["Khulna"]
print(bd_division_info)