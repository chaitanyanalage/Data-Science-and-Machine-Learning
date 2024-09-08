#Python basics

#Variables
rent = 1220
gas = 202
groceries = 305.6
print (rent)

total = rent + gas + groceries
print (total)

rent = 1400
item1 = "rent"
item2 = "gas"
item3 = "groceries"
print("Expense iteams:", item1, item2, item3)
print("--------------------------------------------------------------------")

#Numbers
a = 5
b = 10
print("addition: ", a+b)
print("subtraction: ", a-b)
print("multiplication: ", a*b)
print("modulo: ", a%b)
print("division: ", a/b)
print("power of: ", a**b)
print(round(22/7,5))
print("--------------------------------------------------------------------")

#Strings
text = "ice cream"
print(text[4:5])
print(text[:5])
print(text[0:])

text = "hello"

#use " " to use ' vice versa
text = "Let's learn python"
text = 'hello "world"'
print(text)

#use ''' to print on new line as it is
address = '''400 Lucera Court
Apr 308
Pomona, California'''
print(address)
print("--------------------------------------------------------------------")

#List
items = ["bread", "pasta", "veggies"]
print(items)

items[0] = "wheat"
print(items)

print(items[0:2])

items.append("butter")
print(items)

items.insert(1, 'fruits')
print(items)


food = ["bread", "pasta", "fruits"]
bathroom = ["shampoo", "soap"]
print(food + bathroom)
print(len(food + bathroom))

print("fruits" in items)
print("soda" in items)
print("--------------------------------------------------------------------")

#if statment
#num = input("Enter a number: ")
num = 10
num = int(num)

if num%2 == 0:
    print("Even")
else:
    print("Odd")
    
indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

#dish = input("Enter a dish name: ")

dish = "risotto"

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Enter valid dish")
print("--------------------------------------------------------------------")

#for loop
exp = [2340, 2500, 2100,3100,2980]
total = 0

for item in exp:
    total = total + item

print("Total: ", total)











