#Assignment 3
#Task: Improve MNIST digit using Convolutions. 
#For your exercise see if you can improve MNIST to 99.8% accuracy or more using only a single convolutional layer 
#and a single MaxPooling 2D. You should stop training once the accuracy goes above this amount. 
#It should happen in less than 20 epochs, so it's ok to hard code the number of epochs for training, 
#but your training must end once it hits the above metric. If it doesn't, then you'll need to redesign your layers.
#When 99.8% accuracy has been hit, you should print out the string "Reached 99.8% accuracy so cancelling training!"

import tensorflow as tf
from os import path, getcwd, chdir

# DO NOT CHANGE THE LINE BELOW. If you are developing in a local
# environment, then grab mnist.npz from the Coursera Jupyter Notebook
# and place it inside a local folder and edit the path to that location
path = f"{getcwd()}/../tmp2/mnist.npz"

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)

# GRADED FUNCTION: train_mnist_conv
def train_mnist_conv():
    # Please write your code only where you are indicated.
    # please do not remove model fitting inline comments.

    # YOUR CODE STARTS HERE
    class mycallback(tf.keras.callbacks.Callback):
          def on_epoch_end(self,epoch,logs={}):
            print("\n debug: ",logs['acc'])    
            if(logs.get('acc')>0.998):
               print("Reached 99.8% acuracy so cancelling training!")
               self.model.stop_training=True
               
    callbacks=mycallback()
    # YOUR CODE ENDS HERE

    mnist = tf.keras.datasets.mnist
    (training_images, training_labels), (test_images, test_labels) = mnist.load_data(path=path)
    # YOUR CODE STARTS HERE
    train_data=training_images.reshape(60000,28,28,1)  # since CNN accept 3D data, so reshape training data in terms of width x height x channels
    train_data=train_data/255.0
    
    # YOUR CODE ENDS HERE

    model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)),
                                        tf.keras.layers.MaxPooling2D(2,2),
                                        tf.keras.layers.Flatten(),
                                        tf.keras.layers.Dense(128,activation='relu'),
                                        tf.keras.layers.Dense(10,activation='softmax')
                                        
            # YOUR CODE STARTS HERE

            # YOUR CODE ENDS HERE
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # model fitting
    history = model.fit(train_data,training_labels,epochs=20,callbacks=[callbacks]
        # YOUR CODE STARTS HERE

        # YOUR CODE ENDS HERE
    )
    # model fitting
    return history.epoch, history.history['acc'][-1]
	
	_, _ = train_mnist_conv()