my_list = [7,88,88,3,4,6,3,1,3,2,6,9,4,88,88,2,4,5,3,1]
my_list_sorted = sorted(my_list) # отсортировал список 
numbers_and_counts = {}
for my_number in my_list_sorted:
     numbers_and_counts[my_number] = 1 if not my_number in numbers_and_counts.keys() else numbers_and_counts[my_number] +1
 # заполнил словарь
sorted_counts_from_numbers_and_counts = sorted(numbers_and_counts.values())[::- 1]  # отсортировал  counts по убыванию 
sorted_numbers_and_counts = {} # создал пустой словарь 
for item in sorted_counts_from_numbers_and_counts:
    for key in numbers_and_counts.keys():
        if numbers_and_counts[key] == item:
            sorted_numbers_and_counts[key] = numbers_and_counts[key]  
            # сделал словарь отсортированный по убыванию count
print(sorted_numbers_and_counts)
result = []
for key1, val1 in sorted_numbers_and_counts.items():
    element = [key1] * val1
    result +=  element
print(result)
