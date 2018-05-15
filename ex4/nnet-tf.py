# Backpropagation using TensorFlow
# ref: https://datascience.stackexchange.com/questions/694/best-python-library-for-neural-networks

import tensorflow as tf

# training patterns
patterns = [
  [0,0,1],
  [0,1,1],
  [1,0,1],
  [1,1,1]
]

targets = [
  [1],
  [0],
  [0],
  [1]
]

### induction
dimention = 10

# Layer 0: x3 inputs
x0 = tf.constant( patterns  , dtype=tf.float32 )
y0 = tf.constant( targets , dtype=tf.float32 )

# Layer 1: 3 x dimension hidden sigmoid
m1 = tf.Variable( tf.random_uniform( [3,dimention] , minval=0.1 , maxval=0.9 , dtype=tf.float32  ))
b1 = tf.Variable( tf.random_uniform( [dimention]   , minval=0.1 , maxval=0.9 , dtype=tf.float32  ))
h1 = tf.sigmoid( tf.matmul( x0,m1 ) + b1 )

# Layer 2: dimension x 1 sigmoid output
m2 = tf.Variable( tf.random_uniform( [dimention,1] , minval=0.1 , maxval=0.9 , dtype=tf.float32  ))
b2 = tf.Variable( tf.random_uniform( [1], minval=0.1 , maxval=0.9 , dtype=tf.float32  ))
y_out = tf.sigmoid( tf.matmul( h1,m2 ) + b2 )


### loss
# loss : sum of the squares of y0 - y_out
loss = tf.reduce_sum( tf.square( y0 - y_out ) )

# training step : gradient decent (1.0) to minimize loss
train = tf.train.GradientDescentOptimizer(1.0).minimize(loss)


### training
# run 500 times using all the X and Y
# print out the loss and any other interesting info
with tf.Session() as sess:
  sess.run( tf.global_variables_initializer() )
  for step in range(500):
    sess.run(train)

  results = sess.run([m1,b1,m2,b2,y_out,loss])
  labels  = "m1,b1,m2,b2,y_out,loss".split(",")
  for label,result in zip(*(labels,results)) :
    print("")
    print(label)
    print(result)
