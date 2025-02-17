# multiply_even_numbers
# Write a function called multiply_even_numbers. This function accepts a list of numbers and returns the product of all even numbers in the list.

def multiply_even_numbers(numbers):
    total = 1
    for num in numbers:
        if num % 2 == 0 and num != 0:
            total = num * total
    return total

print(multiply_even_numbers(list(range(7))))
