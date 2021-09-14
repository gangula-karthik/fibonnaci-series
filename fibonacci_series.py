#ask the user for the number of fibonacci terms he wants 
n = int(input("enter the number of fibonacci terms: "))

#let the first number be 0
first_num = 0
print(first_num)

#create the second number which is the next number after zero, in this case 1
second_num = 0 + 1
print(second_num)

#the third number will be in the format of first_number + second_number
next_num = first_num + second_num
print(next_num)

#change the value of the next num to be equal to the first num and loop through to create 10 iterations
for i in range(0,n-3):
    first_num = second_num
    second_num = next_num
    next_num = first_num + second_num
    print(next_num)


