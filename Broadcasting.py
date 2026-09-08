import numpy as np
#Broadcasting in scalar on a vector
marks = np.arange(1,26)
print(marks)
grace_marks= 5
final_list_marks = grace_marks + marks #This is basically Broadcastin since we are not using loops
print(final_list_marks)

#Broadcasting in scalar on a vector
prices = np.random.randint(20, 100, (1,15))
print(prices)
disc = 15
final_prices = prices - ((prices *disc)/100)
print(final_prices)

#Broadcasting vector on a matrix
matrix = np.array([[10,12,16,15],
                   [22,55,65,25]
                                ])
vector = np.array([10,12,16,14])
add = matrix + vector
print(add)