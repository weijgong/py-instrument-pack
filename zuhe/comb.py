'''
Author: gongweijing 876887913@qq.com
Date: 2023-12-03 17:30:01
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-12-03 17:58:03
FilePath: /root/py_instument_pack/zuhe/comb.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from math import factorial


def get_all_permutations(sequence, current_permutation, all_permutations):
    if not sequence:
        all_permutations.append("".join(current_permutation.copy()))
        return

    for i in range(len(sequence)):
        current_permutation.append(sequence[i])
        remaining_elements = sequence[:i] + sequence[i+1:]
        get_all_permutations(remaining_elements, current_permutation, all_permutations)
        current_permutation.pop()

def generate_all_permutations(sequence):
    all_permutations = []
    get_all_permutations(sequence, [], all_permutations)
    return all_permutations

# 丙开头
# # 给定序列
# sequence = ['甲', '甲', '甲', '甲', '甲', '乙', '乙', '乙', '丙']

# # 获取所有排列
# all_permutations = list(set(generate_all_permutations(sequence)))

# print('start')

# # 打印结果
# for i in range(len(all_permutations)):
#     all_permutations[i]="丙"+all_permutations[i]
#     print(f"排列 {i+1}: {all_permutations[i]}")

# import csv

# with open('/root/py_instument_pack/zuhe/丙__.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(all_permutations)

# "甲丙丙"
# 给定序列
# sequence = ['甲', '甲', '甲', '甲', '乙', '乙', '乙']

# # 获取所有排列
# all_permutations = list(set(generate_all_permutations(sequence)))

# print('start')

# # 打印结果
# for i in range(len(all_permutations)):
#     all_permutations[i]="甲丙丙"+all_permutations[i]
#     print(f"排列 {i+1}: {all_permutations[i]}")

# import csv

# with open('/root/py_instument_pack/zuhe/甲丙丙.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(all_permutations)

# sequence = ['甲', '甲', '甲', '甲', '甲','乙', '乙']

# # 获取所有排列
# all_permutations = list(set(generate_all_permutations(sequence)))

# print('start')

# # 打印结果
# for i in range(len(all_permutations)):
#     all_permutations[i]="乙丙丙"+all_permutations[i]
#     print(f"排列 {i+1}: {all_permutations[i]}")

# import csv

# with open('/root/py_instument_pack/zuhe/乙丙丙.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(all_permutations)

sequence = ['甲', '甲', '甲', '甲','乙', '乙']

# 获取所有排列
all_permutations = list(set(generate_all_permutations(sequence)))

print('start')

# 打印结果
for i in range(len(all_permutations)):
    all_permutations[i]="甲丙乙丙"+all_permutations[i]
    print(f"排列 {i+1}: {all_permutations[i]}")

import csv

with open('/root/py_instument_pack/zuhe/甲丙乙丙.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(all_permutations)