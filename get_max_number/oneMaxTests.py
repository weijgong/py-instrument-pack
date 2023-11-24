'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-16 10:54:53
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-21 16:40:10
FilePath: /gongweijing/GeneticAlgorithmsWithPython/ch02/oneMaxTests.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import datetime
import unittest

import genetic

'''
description: 统计二进制染色体中1的个数作为适应函数
param {*} genes 表示的染色体的基因型 binary code
return {*} binary中1的个数
'''
def get_fitness(genes):
    return genes.count(1)

'''
description: 展示总运行时间以及基因型的前后15个数
param {*} candidate 候选最优解
param {*} startTime 程序开始时间
return {*} None
'''
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}...{}\t{:3.2f}\t{}".format(
        ''.join(map(str, candidate.Genes[:15])),
        ''.join(map(str, candidate.Genes[-15:])),
        candidate.Fitness,
        timeDiff))

'''
description: 获取特定长度的最大二进制数值
return {*} None
'''
class OneMaxTests(unittest.TestCase):
    def test(self, length=100):
        geneset = [0, 1]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)

        # 这样设定最优适应度函数的原因是：适应度函数求解的时候采用的是1的个数作为适应度函数数值，而刚好length是最大的适应度函数数值。
        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length, optimalFitness,
                                geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000))


if __name__ == '__main__':
    unittest.main()
