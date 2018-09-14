import tensorflow as tf

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = 'Hello TensorFlow'

hello = tf.constant(hello)
sess = tf.Session()

print(sess.run(hello))

a = tf.constant(20)

b = tf.constant(500)

print(sess.run(a+b))

