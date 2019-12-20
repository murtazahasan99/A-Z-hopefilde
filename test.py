import numpy as np


x = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
for i, j in enumerate(x):
    print("i=", i)
    print("j=", j)
y = np.array_split(x, 5)
z = list(y)
print(z[2][4])

# murtaza = [[0.  1. - 1.  1.  1.  3. - 3. - 1. - 3. - 1.  1. - 1. - 1. - 1. - 3.  1. - 3. - 3.
#             - 3. - 3.  1.  3.  3.  3.  1.]
#            [1.  0.  1.  3.  3.  1. - 1.  1. - 1.  1. - 1.  1.  1.  1. - 1. - 1. - 1. - 1.
#             - 1. - 1. - 1.  1.  1.  1. - 1.]
#            [-1.  1.  0.  1.  1. - 1.  1. - 1.  1. - 1.  1. - 1. - 1. - 1.  1.  1.  1.  1.
#             1.  1.  1. - 1. - 1. - 1.  1.]
#            [1.  3.  1.  0.  3.  1. - 1.  1. - 1.  1. - 1.  1.  1.  1. - 1. - 1. - 1. - 1.
#             - 1. - 1. - 1.  1.  1.  1. - 1.]
#            [1.  3.  1.  3.  0.  1. - 1.  1. - 1.  1. - 1.  1.  1.  1. - 1. - 1. - 1. - 1.
#             - 1. - 1. - 1.  1.  1.  1. - 1.]
#            [3.  1. - 1.  1.  1.  0. - 3. - 1. - 3. - 1.  1. - 1. - 1. - 1. - 3.  1. - 3. - 3.
#             - 3. - 3.  1.  3.  3.  3.  1.]
#            [-3. - 1.  1. - 1. - 1. - 3.  0.  1.  3.  1. - 1.  1.  1.  1.  3. - 1.  3.  3.
#             3.  3. - 1. - 3. - 3. - 3. - 1.]
#            [-1.  1. - 1.  1.  1. - 1.  1.  0.  1.  3. - 3.  3.  3.  3.  1. - 3.  1.  1.
#             1.  1. - 3. - 1. - 1. - 1. - 3.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  0.  1. - 1.  1.  1.  1.  3. - 1.  3.  3.
#             3.  3. - 1. - 3. - 3. - 3. - 1.]
#            [-1.  1. - 1.  1.  1. - 1.  1.  3.  1.  0. - 3.  3.  3.  3.  1. - 3.  1.  1.
#             1.  1. - 3. - 1. - 1. - 1. - 3.]
#            [1. - 1.  1. - 1. - 1.  1. - 1. - 3. - 1. - 3.  0. - 3. - 3. - 3. - 1.  3. - 1. - 1.
#             - 1. - 1.  3.  1.  1.  1.  3.]
#            [-1.  1. - 1.  1.  1. - 1.  1.  3.  1.  3. - 3.  0.  3.  3.  1. - 3.  1.  1.
#             1.  1. - 3. - 1. - 1. - 1. - 3.]
#            [-1.  1. - 1.  1.  1. - 1.  1.  3.  1.  3. - 3.  3.  0.  3.  1. - 3.  1.  1.
#             1.  1. - 3. - 1. - 1. - 1. - 3.]
#            [-1.  1. - 1.  1.  1. - 1.  1.  3.  1.  3. - 3.  3.  3.  0.  1. - 3.  1.  1.
#             1.  1. - 3. - 1. - 1. - 1. - 3.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  3.  1. - 1.  1.  1.  1.  0. - 1.  3.  3.
#             3.  3. - 1. - 3. - 3. - 3. - 1.]
#            [1. - 1.  1. - 1. - 1.  1. - 1. - 3. - 1. - 3.  3. - 3. - 3. - 3. - 1.  0. - 1. - 1.
#             - 1. - 1.  3.  1.  1.  1.  3.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  3.  1. - 1.  1.  1.  1.  3. - 1.  0.  3.
#             3.  3. - 1. - 3. - 3. - 3. - 1.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  3.  1. - 1.  1.  1.  1.  3. - 1.  3.  0.
#             3.  3. - 1. - 3. - 3. - 3. - 1.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  3.  1. - 1.  1.  1.  1.  3. - 1.  3.  3.
#             0.  3. - 1. - 3. - 3. - 3. - 1.]
#            [-3. - 1.  1. - 1. - 1. - 3.  3.  1.  3.  1. - 1.  1.  1.  1.  3. - 1.  3.  3.
#             3.  0. - 1. - 3. - 3. - 3. - 1.]
#            [1. - 1.  1. - 1. - 1.  1. - 1. - 3. - 1. - 3.  3. - 3. - 3. - 3. - 1.  3. - 1. - 1.
#             - 1. - 1.  0.  1.  1.  1.  3.]
#            [3.  1. - 1.  1.  1.  3. - 3. - 1. - 3. - 1.  1. - 1. - 1. - 1. - 3.  1. - 3. - 3.
#             - 3. - 3.  1.  0.  3.  3.  1.]
#            [3.  1. - 1.  1.  1.  3. - 3. - 1. - 3. - 1.  1. - 1. - 1. - 1. - 3.  1. - 3. - 3.
#             - 3. - 3.  1.  3.  0.  3.  1.]
#            [3.  1. - 1.  1.  1.  3. - 3. - 1. - 3. - 1.  1. - 1. - 1. - 1. - 3.  1. - 3. - 3.
#             - 3. - 3.  1.  3.  3.  0.  1.]
#            [1. - 1.  1. - 1. - 1.  1. - 1. - 3. - 1. - 3.  3. - 3. - 3. - 3. - 1.  3. - 1. - 1.
#             - 1. - 1.  3.  1.  1.  1.  0.]]