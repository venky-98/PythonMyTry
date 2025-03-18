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
cap = a^b
print("Cap          =",a," ^ ",b," = ", cap)
print("*********************************************************************")

print("*************************STRING**************************************")
Fname= "Manasa"
print(Fname)
print("Length of the string ",Fname," ==> ",len(Fname))
print("Indexing  of the string [0]",Fname," ==> ",Fname[0])
print("Indexing  of the string [1]",Fname," ==> ",Fname[1])
print("Indexing  of the string [2]",Fname," ==> ",Fname[2])
print("Indexing  of the string [3]",Fname," ==> ",Fname[3])
print("Indexing  of the string [4]",Fname," ==> ",Fname[4])
print("Indexing  of the string [5]",Fname," ==> ",Fname[5])
print("Indexing  of the string [-1]",Fname," ==> ",Fname[-1])
print("Indexing  of the string [-2]",Fname," ==> ",Fname[-2])
print("Indexing  of the string [-3]",Fname," ==> ",Fname[-3])
print("Indexing  of the string [-4]",Fname," ==> ",Fname[-4])
print("Indexing  of the string [-5]",Fname," ==> ",Fname[-5])
print("Indexing  of the string [-6]",Fname," ==> ",Fname[-6])
print("Slice  - [Start: ]of the string [1:]",Fname," ==> ",Fname[1:])
print("Slice  - [Start: ]of the string [2:]",Fname," ==> ",Fname[2:])
print("Slice  - [end: ]of the string [:1]",Fname," ==> ",Fname[:1])
print("Slice  - [end: ]of the string [:2]",Fname," ==> ",Fname[:2])
print("Slice  - [Start: ]of the string [1:]",Fname," ==> ",Fname[1:])
print("Slice  - [Start: ]of the string [2:]",Fname," ==> ",Fname[2:])
print("Slice  - [end: ]of the string [:1]",Fname," ==> ",Fname[:1])
print("Slice  - [Start:end:step] of the string [0:5:2]",Fname," ==> ",Fname[0:5:2])
print("Slice  - [Start:end:step] of the string [1:5:2]",Fname," ==> ",Fname[1:5:2])
print("Slice  - [Start:end:step] of the string [::]",Fname," ==> ",Fname[::])
print("Slice  - [Start:end:step] of the string [::-1]",Fname," ==> ",Fname[::-1])
print("Slice  - [Start:end:step] of the string [::-2]",Fname," ==> ",Fname[::-2])

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