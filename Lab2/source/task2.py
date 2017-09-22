str = input("please enter a number:")

number = int(str)
dictionary = {}

for i in range(1,number+1):
    dictionary[i] = i*i

print(dictionary)