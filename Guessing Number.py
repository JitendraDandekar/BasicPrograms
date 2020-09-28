import random
import time

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
comp_num = random.choice(nums)
print(nums)
user_num = int(input("Enter a Number between 1 to 15 : "))
t = 1
while t <= 3:
    if t != 1:
        user_num = int(input("Select another number : "))

    if comp_num > user_num:
        nums = [i for i in nums if i > user_num]
        print(nums)

    if comp_num < user_num:
        nums = [i for i in nums if i < user_num]
        print(nums)

    if comp_num == user_num:
        print("You Win..!!")
        break
    t += 1

print()
print("Computer's selected number is : " + str(comp_num))
print()
print("Bye Bye..!!")
time.sleep(1)
