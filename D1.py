print("Hello, World!")
print("*************ArithmeticOperation - Start ****************************")
a = 5
b = 3
sum = a + b
print("Sum          =",a," + ",b," = ", sum)
diff = a-b
print("Differernce  =",a," - ",b," = ", diff)
mul =a*b
print("Multiply     =",a," * ",b," = ", mul)
div = a/b
print("Division     =",a," / ",b," = ", div)
floor = a//b
print("Floor_div    =",a,"// ",b," = ", floor)
reminder = a%b
print("Reminder_mod =",a," % ",b," = ", reminder)
print("*********************************************************************")

num = 4
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

numbers = [5, 2, 9, 1, 5, 6]

# Sorting the list in ascending order
numbers.sort()

print("Sorted list:", numbers)   