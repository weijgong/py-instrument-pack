'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-18 11:56:02
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-18 12:30:43
FilePath: /gongweijing/py-instrument-pack/unconfirm_equation.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

cons = 31
x_c = 3
y_c = 5
res_list = []
y_c_list = []

for x in range(1,(cons//x_c)+1):
    y_c_list.append((cons-x_c*x))
    if (cons-x_c*x)%y_c==0:
            res_list.append((x,(cons-x_c*x)//y_c))
print(y_c_list)
print(res_list)
# xyz_list = []
# for i in res_list:
#     xyz_list.append((i[0],i[1],100-i[0]-i[1]))
# print(xyz_list)