# -*- coding: utf-8 -*-
import random as rd

n = abs(int(input('Enter n: ')))

matrix = lambda n: [[rd.randint(0, 99) for i in range(n)] for i in range(n)]
sh_matrix = matrix(2*n-1)

def spiral(matrix, inp_n):
    n = 2*inp_n-1
    dif_x, dif_y = 0, 1
    x_pos, y_pos = n//2, n//2
    ind_turn = 2
    double_iter = 1
    k_ind_step = 1
    b_result_s = [];
    for i in range(1, n**2+1):
        b_result_s.append(matrix[x_pos][y_pos])
        buf_x, buf_y = x_pos - dif_x, y_pos - dif_y
        if not i%ind_turn:
            ind_turn = ind_turn + k_ind_step
            double_iter += 1
            if double_iter > 1:
                k_ind_step += 1
                double_iter = 0
            dif_x, dif_y = -dif_y, dif_x
            x_pos, y_pos = x_pos - dif_x, y_pos - dif_y
        else:
            x_pos, y_pos = buf_x, buf_y
    return b_result_s

print('Matrix: ')
for i in range(len(sh_matrix)):
    print(sh_matrix[i])

result_s = spiral(sh_matrix, n)
print('Result: ')
print(result_s)