x = int(input("Enter an integer: "))
str_x = str(x)
if str_x == str_x[::-1]:
   print(f"{x} is a palindrome.")
else:
    print(f"{x} is not a palindrome.")

2)Given a non-empty array of integers nums, every element appears twice except for one. Find 
that single one. (LeetCode: Single Number) 

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
single_number = 0
for num in nums:
    single_number ^= num
print(f"The single number in the array is: {single_number}")

