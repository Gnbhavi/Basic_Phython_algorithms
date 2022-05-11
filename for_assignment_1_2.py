import numpy as np
np.random.seed(32)

X_train = np.random.randint(10, size=(4, 3))
X = np.random.randint(10, size=(2, 3))
num_test = X.shape[0]

dists = np.reshape(np.sum(X ** 2, axis=1), [num_test, 1]) + np.sum(X_train ** 2, axis=1) \
                - 2 * np.matmul(X, X_train.T)
A = np.reshape(np.sum(X ** 2, axis=1), [num_test, 1])
B = np.sum(X_train ** 2, axis=1)
C = 2 * np.matmul(X, X_train.T)
print('Train square', np.reshape(np.sum(X ** 2, axis=1), [num_test, 1]))
print('Test square', B)
print('Two times train dot test', C)
print('Train plus test square', A+B)