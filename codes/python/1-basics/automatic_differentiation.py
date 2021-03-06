# -*- coding: utf-8 -*-
"""automatic_differentiation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ibfKtpxC_hIhZlPbefCoqpAS7jTdyiFw

## Automatic Differentiation

The [automatic differentiation](https://en.wikipedia.org/wiki/Automatic_differentiation) is to calculate derivative of functions which is useful for algorithms such as [stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent).

It's is particularly useful when we implement neural networks and desire to calculate differentiation of the output with respect to an input that are connected with a **chain of functions**:

$L(x)=f(g(h(x)))$

The differentiation is as below:

$\frac{dL}{dx} = \frac{df}{dg}\frac{dg}{dh}\frac{dh}{dx}$

The above rule is called the [chain rule](https://en.wikipedia.org/wiki/Chain_rule).

So the [gradients](https://en.wikipedia.org/wiki/Gradient) needs to be calculated for ultimate derivative calculations.

Let's see how TensorFlow does it!
"""

# Loading necessary libraries
import tensorflow as tf
import numpy as np

"""### Introduction

Some general information are useful to be addressed here:

* To compute gradients, TensorFlow uses [tf.GradientTape](https://www.tensorflow.org/api_docs/python/tf/GradientTape) which records the operation for later being used for gradient computation.

Let's have three similar example:
"""

x = tf.constant([2.0])

with tf.GradientTape(persistent=False, watch_accessed_variables=True) as grad:
  f = x ** 2

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))

x = tf.constant([2.0])
x = tf.Variable(x)

with tf.GradientTape(persistent=False, watch_accessed_variables=True) as grad:
  f = x ** 2

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))

x = tf.constant([2.0])

with tf.GradientTape(persistent=False, watch_accessed_variables=True) as grad:
  grad.watch(x)
  f = x ** 2

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))

"""What's the difference between above examples?

1. Using tf.Variable on top of the tensor to transform it into a [tf.Variable](https://www.tensorflow.org/guide/variable).
2. Using [.watch()](https://www.tensorflow.org/api_docs/python/tf/GradientTape#watch) operation.

The tf.Variable turn tensor to a variable tensor which is the recommended approach by TensorFlow. The .watch() method ensures the variable is being tracked by the tf.GradientTape(). 

**You can see if we use neither, we get NONE as the gradient which means gradients were not being tracked!**

NOTE: In general it's always safe to work with variable as well as using .watch() to ensure tracking gradients.

We used default arguments as:

1. **persistent=False**: It says, any variable that is hold with tf.GradientTape(), after one calling of gradient will be released. 
2. **watch_accessed_variables=True**: By default watching variables. So if we have a variable, we do not need to use .watch() with this default setting.

Let's have an example with **persistent=True**:
"""

x = tf.constant([2.0])
x = tf.Variable(x)

# For practice, turn persistent to False to see what happens.
with tf.GradientTape(persistent=True, watch_accessed_variables=True) as grad:
  f = x ** 2
  h = x ** 3

# Print gradient output
print('The gradient df/dx where f=(x^2):\n', grad.gradient(f, x))
print('The gradient dh/dx where h=(x^3):\n', grad.gradient(h, x))