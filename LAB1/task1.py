numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_of_numbers = sum([x for x in numbers if isinstance(x, int)])
average_value = sum_of_numbers / len(numbers)
new_list = [x if isinstance(x, int) else average_value for x in numbers]

print("Измененный список:", new_list)
