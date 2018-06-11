# Single Layer Perceptron

import time
import numpy as np


# 3 layer NNet (in,out) dimension of (3, 1)
class NNetSingle:
    def __init__(self):
        np.random.seed()
        self.weights = np.random.random((3, 1))*2 - 1

    def test(self, patterns):
        out = self.sigmoid(np.dot(patterns, self.weights))
        print('input={}\noutput={}'.format(patterns, out))

    def train(self, patterns, targets, iter=1):
        if len(patterns) != len(targets):
            print('Number of patterns and targets should be the same!')
            return

        for _ in range(iter):
            # feed forward
            out = self.sigmoid(np.dot(patterns, self.weights))

            # update weights
            error = targets - out
            delta = error * self.sigmoid(out, True)
            self.weights += patterns.T.dot(delta)

    def printWeights(self):
        print("weights={}".format(self.weights))

    @staticmethod
    def sigmoid(x, derive=False):
        a = np.exp(-x)
        return a/(1+a)**2 if derive else 1/(1+a)


# training patterns
patterns = np.array([
    [0, 0, 1],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

targets = np.array([
    [0],
    [0],
    [1],
    [1]
])

nnet = NNetSingle()
print('***** Before trainig:')
nnet.printWeights()
nnet.test(patterns)

iter = 10000
print('Start training {} iterations...'.format(iter))
tm1 = time.time()
nnet.train(patterns, targets, iter)
tm2 = time.time()
# nnet.printWeights()

print('***** After trainig:')
nnet.test(patterns)
print('Training completed. Elapsed time={}'.format(tm2-tm1))
