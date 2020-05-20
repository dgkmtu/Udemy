# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:50:08 2020

@author: yinag
"""

from PIL import Image
import os, glob
import numpy as np
from sklearn import model_selection

classes = ['stripey', 'sea_goldie', 'neon_damselfish']
num_classes = len(classes)
image_size = 50

# Read Images

X = []
Y = []
for index, class_label in enumerate(classes):
	photos_dir = './' + class_label
	files = glob.glob(photos_dir + '/*.jpg')
	for i, file in enumerate(files):
		if i >= 200: break
		image = Image.open(file)
		image = image.convert('RGB')
		image = image.resize((image_size, image_size))
		data = np.asarray(image)
		X.append(data)
		Y.append(index)

# usable for tensorflow
X = np.array(X)
Y = np.array(Y)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y)

xy = (X_train, X_test, Y_train, Y_test)
np.save('./fish.npy', xy)