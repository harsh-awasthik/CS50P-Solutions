camel = input("camelCase: ")
snake = ""

for i in camel:
    if not i.isupper():
        snake += i
    else:
        snake += ("_" + i.lower())

print("snake_case:", snake)


