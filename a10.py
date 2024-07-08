numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
max_value = None  
else:
max_value = numbers[0]  
    for number in numbers:
        if number > max_value:
            max_value = number  

print("The maximum value in the list is:", max_value)
