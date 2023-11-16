'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-15 21:43:50
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-15 21:53:01
FilePath: /gongweijing/py-instrument-pack/general_static_cal.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

'''
description: 计算组合总个数
param {*} n 表示总的选择数
param {*} m 表示要选择的个数
return {*} 计算的结果
'''
def C_n_m(n,m):
    res = 1
    for i in range(m):
        res*=(n-i)
    return res//m

'''
description: 计算排序总个数
param {*} n 表示总的选择数
param {*} m 表示要选择的个数
return {*} 计算的结果
'''
def A_n_m(n,m):
    res = 1
    for i in range(m):
        res*=(n-i)
    return res

print(C_n_m(6,2),A_n_m(5,5))
    