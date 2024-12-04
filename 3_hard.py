data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data):

    sum_of_number = 0
    sum_of_len_string = 0

    if isinstance(data, (int, float)):
        sum_of_number += data

    elif isinstance(data, str):
        sum_of_len_string += len(data)

    elif isinstance(data, (list, tuple, set)):
        for items in data:
            sum_of_number += calculate_structure_sum(items)

    elif isinstance(data, dict):
        for key, value in data.items():
            sum_of_number += calculate_structure_sum(key)
            sum_of_number += calculate_structure_sum(value)

    sum = sum_of_number + sum_of_len_string

    return sum

result = calculate_structure_sum(data_structure)
print(result)
