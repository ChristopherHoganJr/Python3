numbers = [1,1,2,3,5,8,13,21,34,55]

# Square numbers using LC
squared_numbers = [i**2 for i in numbers]
print(squared_numbers)

# Filter even numbers
result = [i for i in numbers if i % 2 == 0]
print(result)
