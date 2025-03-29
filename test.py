import numpy as np

vec_a = [1, 2, 3]
vec_b = [4, 5, 6]

result = 0
for val1, val2 in zip(vec_a, vec_b):
    print(val1 * val2)
    result += val1 * val2
print(result)

result = np.dot(vec_a, vec_b)
print(result)

result = np.outer(vec_a, vec_b)
print(result)
