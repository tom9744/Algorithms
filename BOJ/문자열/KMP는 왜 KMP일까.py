long_name = input()
short_name = "".join([chunk[0] for chunk in long_name.split("-")])
print(short_name)