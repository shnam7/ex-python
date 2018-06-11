# Monte-Carlo Simulator

import random


class MonteCarloSimulator:
    def __init__(self, fileName=''):
        self.countTotal = 0
        self.countCircle = 0
        self.unitTestSize = 100
        self.file = open(fileName, 'w') if len(fileName) > 0 else None
        random.seed()

    def run(self, iteration=1):
        testSize = self.unitTestSize
        for i in range(iteration):
            print("iteration={}".format(i+1), end=' ')
            testSize *= 2
            self.runSingle(testSize)

    def runSingle(self, count=-1, verbose=False):
        if count == -1:
            count = self.unitTestSize
        for i in range(count):
            rx = random.random()
            ry = random.random()
            self.countTotal += 1
            if MonteCarloSimulator.isInsideCircle(rx, ry):
                self.countCircle += 1
                if verbose:
                    print("count={}".format(i), rx, ry)
                if self.file:
                    self.file.write("%f,%f\n" % (rx, ry))
            if self.file:
                self.file.close()

        estimatedPi = 4 * self.countCircle / self.countTotal
        print('total={}, in-circle={}, estimated Pi={}'.format(
            self.countTotal, self.countCircle, estimatedPi))

    @staticmethod
    def isInsideCircle(x, y):
        cx = cy = r = 0.5
        deviation = (x-cx)**2 + (y-cy)**2 - r**2
        return deviation <= 0

simulatror = MonteCarloSimulator()
simulatror2 = MonteCarloSimulator()
simulatror.run(12)
