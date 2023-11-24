'''
Author: gongweijing 876887913@qq.com
Date: 2023-11-16 10:54:53
LastEditors: gongweijing 876887913@qq.com
LastEditTime: 2023-11-21 19:25:52
FilePath: /gongweijing/GeneticAlgorithmsWithPython/ch03/genetic.py
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''

import random
import statistics
import sys
import time


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    childGenes = parent.Genes[:]
    index = random.randrange(0, len(parent.Genes))
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()

    def fnMutate(parent):
        return _mutate(parent, geneSet, get_fitness)

    def fnGenerateParent():
        return _generate_parent(targetLen, geneSet, get_fitness)

    for improvement in _get_improvement(fnMutate, fnGenerateParent):
        display(improvement)
        if not optimalFitness > improvement.Fitness:
            return improvement

'''
description: 代替了原本函数中变异+迭代的代码编写方法
param {*} new_child 获取新的子代的算法
param {*} generate_parent 生成初始种群的算法
return {*}
'''
# yield的作用是让每次遍历返回的数值随着迭代次数不断变化
def _get_improvement(new_child, generate_parent):
    bestParent = generate_parent()
    yield bestParent
    while True:
        child = new_child(bestParent)
        if bestParent.Fitness > child.Fitness:
            continue
        if not child.Fitness > bestParent.Fitness:
            bestParent = child
            continue
        yield child
        bestParent = child


class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean) if i > 1 else 0))
