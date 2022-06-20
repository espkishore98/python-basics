import constants
#variables
newInput=12
print(newInput)
newInput=12.5
print(newInput)
newInput='abc'
print(newInput)
#take value dynamicly
newInput=int(input("please enter some value:"))
print(newInput+2)
print(type(newInput))
chai=cofee=milk=10#Assigning values to multiple variables sametime
print(chai)
print(cofee)
print(milk)
print(constants.PI)
print(constants.SUCCESS_MESSAGE)
# first=input("first value:")
# second= input("second value:")
# sum=int(first)+int(second)
# print(sum)

sum = int(input("first: "))+int(input("second: "))
print(sum)

#swap 2 values
first=10
second=20
first,second = second,first
print("first",first)
print("second",second)

print(chr(65))
print(ord('a'))