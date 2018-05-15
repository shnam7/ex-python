# Double Layer Neural Network
# ref: https://iamtrask.github.io/2015/07/12/basic-python-network/

import time
import numpy as np

# 3 layer NNet (in,out) dimension of (3, 1)
class NNetDouble:
  def __init__(self, dimension=50):
    self.w1 = np.random.random((3, dimension))*2 - 1
    self.w2 = np.random.random((dimension,1))*2 - 1

  def test(self, patterns):
    out1 = self.sigmoid(np.dot(patterns, self.w1))
    out2 = self.sigmoid(np.dot(out1, self.w2))
    print('input={}\noutput={}'.format(patterns, out2))

  def train(self, patterns, targets, iter=1):
    if len(patterns) != len(targets):
      print('Number of patterns and targets should be the same!')
      return

    for _ in range(iter):
      # feed forward
      out1 = self.sigmoid(np.dot(patterns, self.w1))
      out2 = self.sigmoid(np.dot(out1, self.w2))
      
      # update output weights (w2)
      error2 = targets - out2
      delta2 = error2 * self.sigmoid(out2, True)
      self.w2 += out1.T.dot(delta2)

      # update hidden layer weights (w1)
      error1 = delta2.dot(self.w2.T)
      delta1 = error1 * self.sigmoid(out1, True)
      self.w1 += patterns.T.dot(delta1)

  def printWeights(self):
    print("w1={}, w2={}".format(self.w1, self.w2))

  @staticmethod
  def sigmoid(x, derive=False):
    a = np.exp(-x)
    return a/(1+a)**2 if derive else 1/(1+a)


# training patterns
patterns = np.array([
  [0,0,1],
  [0,1,1],
  [1,0,1],
  [1,1,1]
])

targets = np.array([
  [1],
  [0],
  [0],
  [1]
])

nnet = NNetDouble()
print('***** Before trainig:')
# nnet.printWeights()
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
