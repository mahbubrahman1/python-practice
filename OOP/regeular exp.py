# import re

# pattern = r"Cyan"

# if re.match(pattern, "Cyan is a colour and i love this colour"):
#     print("Match")
# else:
#     print("Not matched")


# import re

# pattern = r"color"

# if re.match(pattern, "Cyan is a color and i love this color"):
#     print("Match")
# else:
#     print("Not matched")


# import re

# pattern = r"Audi"

# if re.search(pattern, "I love Audi because Audi is best car"):
#     print("Match")
# else:
#     print("Not Matched")


# import re

# pattern = r"Toyota"

# if re.search(pattern, "I love Audi because Audi is best car"):
#     print("Match")
# else:
#     print("Not Matched")


# import re

# pattern = r"Car"
# print(re.findall(pattern, "Audi is best Car, Toyota is also best Car"))


# import re

# pattern = r"Phone"

# text = "My favourite phone is iPhone12 Pro Max"
# match = re.search(pattern, text)

# if match:
#     print(match.start())


"""meta chractare"""


# import re

# pattern = r"bangl.desh"

# if re.match(pattern, "bangladese"):
#     print("Matched")


import re
pattern = r"^bang..desh$"

if re.match(pattern, "bangladesh"):
    print("Match")
else:
    print("Not match")
