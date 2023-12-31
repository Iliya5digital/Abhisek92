import numpy as np

gamma = 0.5

T = np.array(
    [[[(1/2), (1/2), 0, 0, 0],
     [(1/4), (1/2), (1/4), 0, 0],
     [0, (1/4), (1/2), (1/4), 0],
     [0, 0, (1/4), (1/2), (1/4)],
     [0, 0, 0, (1/2), (1/2)]],
 
    [[(1/2), (1/2), 0, 0, 0],
     [(1/3), (2/3), 0, 0, 0],
     [0, (1/3), (2/3), 0, 0],
     [0, 0, (1/3), (2/3), 0],
     [0, 0, 0, (1/3), (2/3)]],
 
    [[(2/3), (1/3), 0, 0, 0],
     [0, (2/3), (1/3), 0, 0],
     [0, 0, (2/3), (1/3), 0],
     [0, 0, 0, (2/3), (1/3)],
     [0, 0, 0, (1/2), (1/2)]]]
)

R = np.zeros((5, 5))
R[4, :] = 1

V = np.zeros(5)

for i in range(200):
    V = np.max(np.sum(T * (R + gamma * V), axis=2), axis=0)

# Print final value function
print(V)
