list = "fesagdatomuoncb"
format = "abcdefghijklmnopqrstuvwxyz"

temp = 0;
for s in format:
    if not s in list:
        temp = 1
        break

if temp == 0:
    print("the string contains all letters of the alphabet")
else:
    print("the string doesn't contain all letters of the alphabet")