# in this part, we'll learn how to use numerical lists.(page no.94)

    # RANGE FUNTION
for value in range ( 1,6):
 print (value)
# here it takes every number (excluding 6) and prints it one by one

#you can also use range funtion to print a list
numbers=list(range(1,6))
print(numbers)

# you can also use range to skip numbers (in list)
numbers_from_one_to_ten_skipping_3_at_a_time = list(range(1,11,3))
print(numbers_from_one_to_ten_skipping_3_at_a_time)

# or simply you can do this to skip numbers too( not in list)
for i in range(1,11,2): # 1 is the starting, 10 is the ending (excluding 11), 2 is the numbers to skip
    print(i)



