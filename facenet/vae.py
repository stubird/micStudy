"""
   Copyright 2018 (c) Jinxin Xie

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets

mnist = read_data_sets('../tmp/', one_hot=True)
n_samples = mnist.train.num_examples

np.random.seed(0)
tf.set_random_seed(0)

def xavier_init(fan_in, fan_out, constant=1):
    """ Xavier initialization of network weights"""
    # https://stackoverflow.com/questions/33640581/how-to-do-xavier-initialization-on-tensorflow
    low = -constant*np.sqrt(6.0/(fan_in + fan_out))
    high = constant*np.sqrt(6.0/(fan_in + fan_out))
    return tf.random_uniform((fan_in, fan_out),
                             minval=low, maxval=high,
                             dtype=tf.float32)

class vaenet:
    def __init__(self, network_architecture,
                 batchsize = 100, learning_rate = 0.001,
                 transfer_fct = tf.nn.softplus):
        #tf.nn.softplus:log(exp(features) + 1).
        self.transfer_fct = transfer_fct
        self.batchsize = batchsize
        self.learning_rate = learning_rate
        self.network_architecture = network_architecture

        #tf graph input
        self.x = tf.placeholder(tf.float32, [None, network_architecture["input_size"]])

        #create vae network
        self._create_network()

        input_size = 784
        layer1 = 500
        layer2 = 500
        z_size = 20
        hidden_1 = 500
        hidden_2 = 500

        #create loss optimizer
        self._create_loss_optimizer()

        # init
        self.init = tf.global_variables_initializer()

        self.sess = tf.InteractiveSession()
        self.sess.run(self.init)

    def _init_weights(self, input_size, z_size,
                      recong_size_1, recong_size_2,
                      generator_size_1, generator_size_2):
        all_weights = dict()
        all_weights['weights_recog'] = {
            'h1': tf.Variable(xavier_init(input_size, recong_size_1)),
            'h2': tf.Variable(xavier_init(recong_size_1, recong_size_2)),
            'out_mean': tf.Variable(xavier_init(recong_size_2, z_size)),
            'out_log_sigma': tf.Variable(xavier_init(recong_size_2, z_size))
        }
        all_weights['bias_recog'] = {
            'b1': tf.Variable(tf.zeros([recong_size_1], dtype=tf.float32)),
            'b2': tf.Variable(tf.zeros([recong_size_2], dtype=tf.float32)),
            'out_mean': tf.Variable(tf.zeros([z_size], dtype=tf.float32)),
            'out_log_sigma': tf.Variable(tf.zeros([z_size], dtype=tf.float32))
        }
        #the generator size also can named as n_hidden_gener
        all_weights['weights_generator'] = {
            'h1': tf.Variable(xavier_init(z_size, generator_size_1)),
            'h2': tf.Variable(xavier_init(generator_size_1, generator_size_2)),
            'out_mean': tf.Variable(xavier_init(generator_size_2, input_size)),
            'out_log_sigma': tf.Variable(xavier_init(generator_size_2, input_size))
        }
        all_weights['bias_generator'] = {
            'b1': tf.Variable(tf.zeros([generator_size_1], dtype=tf.float32)),
            'b2': tf.Variable(tf.zeros([generator_size_2], dtype=tf.float32)),
            'out_mean': tf.Variable(tf.zeros([input_size], dtype=tf.float32)),
            'out_log_sigma': tf.Variable(tf.zeros([input_size], dtype=tf.float32))
        }
        return all_weights

    def _create_network(self):
        self.initweight = self._init_weights(**self.network_architecture)

        self.z_mean , self.z_log_sigma = self._recogizer()
        z_size = self.network_architecture["z_size"]
        eps = tf.random_normal((self.batchsize, z_size),0,1,dtype=tf.float32)
        self.z = tf.add(self.z_mean, tf.multiply(tf.sqrt(tf.exp(self.z_log_sigma)), eps))
        self.x_reconstr_mean = self._generator()


    def _recogizer(self):
        initdata = self.initweight
        #first layer
        layer1 = tf.add(tf.matmul(self.x, initdata['weights_recog']['h1']),
                        initdata['bias_recog']['b1'])
        layer2 = tf.add(tf.matmul(layer1, initdata['weights_recog']['h2']),
                        initdata['bias_recog']['b2'])
        z_mean = tf.add(tf.matmul(layer2, initdata['weights_recog']['out_mean']),
                        initdata['bias_recog']['out_mean'])
        z_log_sigma = tf.add(tf.matmul(layer2, initdata['weights_recog']['out_log_sigma']),
                        initdata['bias_recog']['out_log_sigma'])
        return (z_mean, z_log_sigma)

    def _generator(self):
        initdata = self.initweight
        layer1 = tf.add(tf.matmul(self.z, initdata['weights_generator']['h1']),
                        initdata['bias_generator']['b1'])
        layer2 = tf.add(tf.matmul(layer1, initdata['weights_generator']['h2']),
                        initdata['bias_generator']['b2'])
        x_reconstr_mean = tf.nn.sigmoid(tf.add(tf.matmul(layer2, initdata['weights_generator']['out_mean']),
                        initdata['bias_generator']['out_mean']))
        return x_reconstr_mean

    def _create_loss_optimizer(self):
        # cross entropy loss is used
        # use 1e-10 to avoid evaluating of log(0.0)
        # 这里表示每个像素上，原图形和生成图形做差值
        reconstr_loss = \
            -tf.reduce_sum(self.x * tf.log(1e-10 + self.x_reconstr_mean)
                           + (1 - self.x) * tf.log(1e-10 + 1 - self.x_reconstr_mean),1)

        # Kullback Leibler loss
        latent_loss = -0.5 * tf.reduce_sum(1 + self.z_log_sigma - tf.square(self.z_mean)
                                           - tf.exp(self.z_log_sigma), 1)
        self.cost = tf.reduce_mean(reconstr_loss + latent_loss)
        self.optimizer = \
            tf.train.AdadeltaOptimizer(learning_rate=self.learning_rate).minimize(self.cost)

    def partial_fit(self, X):
        # train data by minimized cost
        _, cost = self.sess.run((self.optimizer, self.cost), feed_dict={self.x:X})

        return cost

    def transform(self, X):
        # mapping data to latent space
        return self.sess.run(self.z_mean, feed_dict={self.x:X})

    def generate(self, z_mu = None):
        """ Generate data by sampling from latent space.
        """
        if z_mu is None:
            z_mu = np.random.normal(size=self.network_architecture["n_z"])

        return self.sess.run(self.x_reconstr_mean, feed_dict={self.z: z_mu})

    def reconstruct(self, X):
        return self.sess.run(self.x_reconstr_mean, feed_dict={self.x:X})

def train(network_architecture, learning_rate = 0.001,
          batch_size = 100, training_epochs = 10, display_step = 5):
    vae = vaenet(network_architecture, learning_rate=learning_rate, batchsize=batch_size)

    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(n_samples / batch_size)

        # Loop over all batches
        for i in range(total_batch):
            batch_xs, _ = mnist.train.next_batch(batch_size)

            # Fit training using batch data
            cost = vae.partial_fit(batch_xs)
            # compute average loss
            avg_cost += cost / n_samples * batch_size

        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1),
                  "cost=", "{:.9f}".format(avg_cost))
    return vae

network_architecture = \
    dict(recong_size_1=500, # 1st layer encoder neurons
         recong_size_2=500, # 2nd layer encoder neurons
         generator_size_1=500, # 1st layer decoder neurons
         generator_size_2=500, # 2nd layer decoder neurons
         input_size=784, # MNIST data input (img shape: 28*28)
         z_size=20)  # dimensionality of latent space

vae = train(network_architecture, training_epochs=6)

# test
x_sample = mnist.test.next_batch(100)[0]
x_reconstruct = vae.reconstruct(x_sample)

plt.figure(figsize=(8, 12))
for i in range(5):

    plt.subplot(5, 2, 2*i + 1)
    plt.imshow(x_sample[i].reshape(28, 28), vmin=0, vmax=1, cmap="gray")
    plt.title("Test input")
    plt.colorbar()
    plt.subplot(5, 2, 2*i + 2)
    plt.imshow(x_reconstruct[i].reshape(28, 28), vmin=0, vmax=1, cmap="gray")
    plt.title("Reconstruction")
    plt.colorbar()
plt.tight_layout()


# 2d graph
x_sample, y_sample = mnist.test.next_batch(5000)
z_mu = vae.transform(x_sample)
plt.figure(figsize=(8, 6))
plt.scatter(z_mu[:, 0], z_mu[:, 1], c=np.argmax(y_sample, 1))
plt.colorbar()
plt.grid()

# picture
# nx = ny = 20
# x_values = np.linspace(-3, 3, nx)
# y_values = np.linspace(-3, 3, ny)
#
# canvas = np.empty((28*ny, 28*nx))
# for i, yi in enumerate(x_values):
#     for j, xi in enumerate(y_values):
#         z_mu = np.array([[xi, yi]]*vae.batchsize)
#         x_mean = vae.generate(z_mu)
#         canvas[(nx-i-1)*28:(nx-i)*28, j*28:(j+1)*28] = x_mean[0].reshape(28, 28)
#
# plt.figure(figsize=(8, 10))
# Xi, Yi = np.meshgrid(x_values, y_values)
# plt.imshow(canvas, origin="upper", cmap="gray")
# plt.tight_layout()
