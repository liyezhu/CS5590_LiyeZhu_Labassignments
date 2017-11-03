#      A1, the petrol tax;
#      A2, the per capita income;
#      A3, the miles of paved highway;
#      A4, the proportion of drivers;
#      B,  the consumption of petrol.
#
#    We seek a model of the form:
#
#      B = A1 * X1 + A2 * X2 + A3 * X3 + A4 * X4.

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE = 'x15.xls'

# Step 1: read in data from the .xls file
book = xlrd.open_workbook(DATA_FILE, encoding_override="utf-8")
sheet = book.sheet_by_index(0)
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])
n_samples = sheet.nrows - 1

## Step 2: create placeholders
A1 = tf.placeholder(tf.float32, name='A1')
A2 = tf.placeholder(tf.float32, name='A2')
A3 = tf.placeholder(tf.float32, name='A3')
A4 = tf.placeholder(tf.float32, name='A4')
B = tf.placeholder(tf.float32, name='B')

# Step 3: create weight, initialized to 0
x1 = tf.Variable(0.0, name='weights1')
x2 = tf.Variable(0.0, name='weights2')
x3 = tf.Variable(0.0, name='weights3')
x4 = tf.Variable(0.0, name='weights4')

# Step 4: build model to predict B
B_predicted = A1 * x1 + A2 * x2 + A3 * x3 + A4 * x4

# Step 5: use the square error as the loss function
loss = tf.square(B - B_predicted, name='loss')
#
# Step 6: using gradient descent with learning rate of 0..00000000000000000001 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.00000000000000000001).minimize(loss)

with tf.Session() as sess:
    # Step 7: initialize the necessary variables
    sess.run(tf.global_variables_initializer())

    writer = tf.summary.FileWriter('./graphs/linear_reg', sess.graph)

    # Step 8: train the model
    for i in range(48):  # train the model 48 epochs
        total_loss = 0
        for a1,a2,a3,a4,b in data:

            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={A1: a1,A2:a2,A3:a3,A4:a4, B: b})

            total_loss +=  l
        print('Epoch {0}: {1}'.format(i, total_loss / n_samples))

    # close the writer when you're done using it
    writer.close()

    # Step 9: output the values
    x1,x2,x3,x4 = sess.run([x1,x2,x3,x4])
    print(x1)
    print(x2)
    print(x3)
    print(x4)




# plot the results
A1, A2,A3,A4,B = data.T[0],data.T[1], data.T[2],data.T[3],data.T[4]
plt.plot(A1,A2,A3,A4, B, 'bo', label='Real data')
plt.plot(A1,A2,A3,A4,A1 * x1 + A2 * x2 + A3 * x3 + A4 * x4 , 'r', label='Predicted data')
plt.legend()
plt.show()