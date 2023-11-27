def square_numbers(nums):
    return list(map(lambda num: num ** 2 ,nums))

squared_numbers = square_numbers([2, 3, 4])
print(squared_numbers)

def filter_even_nums(nums):
    return list(filter(lambda num: num % 2 == 0,nums))

even_numbers = filter_even_nums([1,2,3,4,5,6])
print(even_numbers)
