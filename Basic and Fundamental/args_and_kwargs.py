#======== *args

# def name(first_name, last_name):
#     print(first_name + " " + last_name)
#
# name("John", "Devid")


# def name(first_name, last_name):
#     print(first_name + " " + last_name)
#
# name("John", "Devid", "Cat")


# def name(*args):
#     print(args)
#
# name("John", "David", 25, True)


#======== **kwargs
# ata kintu dictionary onujayi kaj kore. single argument pass korle error dibe

# def info(**kwargs):
#     print(kwargs)
#
# info(name = "Mahbub", id = 95, department = "CS")


def info(**kwargs):
    print(kwargs["department"])

info(name = "Mahbub", id = 95, department = "CS")