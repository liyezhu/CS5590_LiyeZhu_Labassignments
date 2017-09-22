str = input("Input:")
list = str.split(" ")
result=[]
for s in list:
    if s in result:
        continue
    else:
        result.append(s)
result.sort()
print(result)