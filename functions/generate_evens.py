def generate_evens():
    numbers = range(1,50)
    
    return [num for num in numbers if num % 2 == 0]

print(generate_evens())