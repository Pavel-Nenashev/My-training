from fake_math import divide as fake_divide
from true_math import divide as true_divide

print('Результаты при использовании Fake_math:')

result1 = fake_divide(27, 3)
result2 = fake_divide(27, 0)
print(result1)
print(result2)

print('Результаты при использовании True_math:')

result3 = true_divide(30, 3)
result4 = true_divide(30, 0)
print(result3)
print(result4)

