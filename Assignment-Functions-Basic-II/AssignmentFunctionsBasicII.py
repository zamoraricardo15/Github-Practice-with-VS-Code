# Countdown 
def count(number):
    countdown = []
    for i in range(number, -1, -1):
        countdown.append(i)
    return countdown

print(count(5))

# Print and Return
def print_return(values):
    print(values[0])
    return values[1]

print(print_return([1,2]))

# First Plus Length
def first_length(list):
    return list[0] + len(list)

print(first_length([1,2,3,4,5]))

#Values Greater than Second 
def greater_than(list):
    greater = []
    for i in range (0, len(list)):
        if list[1] < list[i]:
            greater.append(list[i])
    print(len(greater))
    return greater

print(greater_than([5,2,3,2,1,4]))

#This Length, That Value
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))

