'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-16 10:54:53
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-21 16:41:35
FilePath: /gongweijing/GeneticAlgorithmsWithPython/ch03/sortedNumbersTests.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''


import datetime
import unittest

import genetic

'''
description: 相邻两个数据满足前一个小于后一个的个数-前一个数大于后一个数的数值(仅前一个>后一个的时候进行计算)
param {*} genes 染色体数据应当为数组
return {*}
'''
def get_fitness(genes):
    fitness = 1
    gap = 0

    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
        else:
            gap += genes[i - 1] - genes[i]
    return Fitness(fitness, gap)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t=> {}\t{}".format(
        ', '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        timeDiff))


class SortedNumbersTests(unittest.TestCase):
    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)

        optimalFitness = Fitness(totalNumbers, 0)
        best = genetic.get_best(fnGetFitness, totalNumbers, optimalFitness,
                                geneset, fnDisplay)
        self.assertTrue(not optimalFitness > best.Fitness)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.sort_numbers(40))


class Fitness:
    def __init__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.NumbersInSequenceCount != other.NumbersInSequenceCount:
            return self.NumbersInSequenceCount > other.NumbersInSequenceCount
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return "{} Sequential, {} Total Gap".format(
            self.NumbersInSequenceCount,
            self.TotalGap)


if __name__ == '__main__':
    unittest.main()
