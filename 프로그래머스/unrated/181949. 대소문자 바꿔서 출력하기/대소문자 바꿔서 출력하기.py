str = input()
result = []
for i in range(len(str)):
    if(str[i].isupper()):
        result.append(str[i].lower())
    if(str[i].islower()):
        result.append(str[i].upper())
print("".join(result))