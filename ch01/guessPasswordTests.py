'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-16 10:54:53
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-20 16:10:53
FilePath: /gongweijing/GeneticAlgorithmsWithPython/ch01/guessPasswordTests.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
# File: guessPasswordTests.py
#    from chapter 1 of _Genetic Algorithms with Python_
#
# Author: Clinton Sheppard <fluentcoder@gmail.com>
# Copyright (c) 2016 Clinton Sheppard
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

import datetime
import random
import unittest

import genetic

'''
description: 
param {*} guess 猜测的基因序列值
param {*} target 目标的基因序列值
return {*}
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


class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    '''
    description: 猜数方法
    param {*} self 
    param {*} target 目标的密码序列
    return {*}
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

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneset)
                         for _ in range(length))

        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)


if __name__ == '__main__':
    unittest.main()
