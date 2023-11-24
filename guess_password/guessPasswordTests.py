'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-16 10:54:53
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-21 16:40:18
FilePath: /gongweijing/GeneticAlgorithmsWithPython/ch01/guessPasswordTests.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import datetime
import random
import unittest

import genetic

'''
description: 
param {*} guess 猜测的基因序列值
param {*} target 目标的基因序列值
return {*} 相同的基因序列总个数
'''
def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)

'''
description: 展示函数
param {*} candidate 候选的染色体（最优解）
param {*} startTime 函数开始执行时间
return {*} 输出候选染色体的基因序列、适应度，并输出函数执行到现在的执行时间
'''
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(
        candidate.Genes, candidate.Fitness, timeDiff))

'''
description: 猜密码类采用Unit test库进行了单元测试
return {*}
'''
class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
    '''
    description: Hello World单元测试
    param {*} self
    return {*} 
    '''
    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    '''
    description: For I am fearfully and wonderfully made.单元测试
    param {*} self
    return {*}
    '''
    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    '''
    description: 猜数方法调用遗传算法进行迭代求解
    param {*} self 
    param {*} target 目标的密码序列
    return {*} 最优的基因序列
    '''    
    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness,
                                self.geneset, fnDisplay)
        self.assertEqual(best.Genes, target)

    '''
    description: 随机150个任意字符测试
    param {*} self
    return {*}
    '''
    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneset)
                         for _ in range(length))

        self.guess_password(target)

    '''
    description: benchmark测试
    param {*} self
    return {*} 计算test_Random所需时间
    '''
    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)


if __name__ == '__main__':
    unittest.main()
