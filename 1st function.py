def find_largest_number(numbers):
    largest = float('-inf')
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage:
my_list = [10, 5, 8, 21, 13]
result = find_largest_number(my_list)
print("The largest number is:", result)
