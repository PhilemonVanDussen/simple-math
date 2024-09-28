# PJ VanDussen
# 9/25/24
# Simple Math

#Practice 1
# num1 = 2
# num2 = 3

# sum = num1 + num2 
# difference = num2 - num1
# product = num1 * num2
# quotient = num2 / num1

# print(f'The sum of {num1} and {num2} is {sum}')
# print(f'The difference of {num2} and {num1} is {difference}')
# print(f'The product of {num1} and {num2} is {product}')
# print(f'The quotient of {num2} and {num1} is {quotient}')

#Practice 2
# length = float(input('Enter the length of your rectangular room in feet \n'))
# width = float(input('Enter the width of your rectangular room in feet \n'))

# area = length * width 

# print(f'The length ({length} ft) and the width ({width} ft) of your room, times them together and the area is {area:.1f} sq. ft.')

#Practice 3 
#Part 1
f_name = 'PJ'
age = 17
fav_color = 'blue, yellow'
message = 'My name is {0} and I am {1}, and the colors I like are {2}. '.format(f_name, age, fav_color)
print(message)
#Part 2
sst = 0.06
bannas = 2
ceral = 4
coke = 1.50
total = bannas + ceral + coke
gt = total * sst + total
print(f'A customer wants to buy some groceries at the store, the bannas cost ${bannas:.2f}, the ceral cost ${ceral:.2f} and the coke cost ${coke:.2f}. The total cost is ${total:.2f}. But with the state sales tax the cost is ${gt:.2f}. Now after buying their groceries they can put bannas and use coke as milk in their ceral. Delicous. ')
#Part3
friend = 'Eathon'
school = 'Kingsley High School'
message = 'My friend {0} goes to {1} and we sit together in lunch.'.format(friend, school)
print(message)
