
# %%
import numpy as np
import tensorflow as tf
import os
import argparse
import cv2


class Inference:
    def __init__(self, weightspath, metaname, ckptname, imagepath):
    self.weightspath = weightspath
    self.metaname = metaname
    self.ckptname = ckptname
    self.imagepath = imagepath
    mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
    inv_mapping = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}

    sess = tf.Session()
    tf.get_default_graph()
    saver = tf.train.import_meta_graph(
        os.path.join(self.weightspath, self.metaname))
    saver.restore(sess, os.path.join(self.weightspath, self.ckptname))

    graph = tf.get_default_graph()

    image_tensor = graph.get_tensor_by_name("input_1:0")
    pred_tensor = graph.get_tensor_by_name("dense_3/Softmax:0")

    x = cv2.imread(self.imagepath)
    h, w, c = x.shape
    x = x[int(h/6):, :]
    x = cv2.resize(x, (224, 224))
    x = x.astype('float32') / 255.0
    pred = sess.run(pred_tensor, feed_dict={
                    image_tensor: np.expand_dims(x, axis=0)})

    def __getPrediction__(self):
        return 'Prediction: {}'.format(inv_mapping[pred.argmax(axis=1)[0]])

    def __getConfidence__(self):
        return 'Normal: {:.3f}, Pneumonia: {:.3f}, COVID-19: {:.3f}'.format(pred[0][0], pred[0][1], pred[0][2])


# %%
!ls

# %%
