#!/usr/bin/python3
number = input()
number = number.split('/')
first = int(number[0])
second = int(number[1])

if (first == 0) or (second == 0):
    exit()

coeffs = list()

coeffs.append(first//second)

first = first%second

while first!=0:
    temp = first
    first = second
    second = temp
    coeffs.append(first//second)
    first = first%second

for x in range(0, len(coeffs)-1):
    print (coeffs[x], end = ' ')

print (coeffs[len(coeffs)-1])