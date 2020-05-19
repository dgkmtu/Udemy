from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import keras
import numpy as np
from PIL import Image
import os, glob, sys

classes = ['monkey', 'boar', 'crow']
num_classes = len(classes)
image_size = 50

def build_model():
	model = Sequential()
	model.add(Conv2D(32, (3, 3), padding='same', input_shape=(50, 50, 3)))
	model.add(Activation('relu'))
	model.add(Conv2D(32, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Dropout(0.25))

	model.add(Conv2D(64, (3, 3), padding='same'))
	model.add(Activation('relu'))
	model.add(Conv2D(64, (3, 3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Flatten())
	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(3)) # number of images
	model.add(Activation('softmax'))

	opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

	model.compile(loss='categorical_crossentropy',
					optimizer=opt, metrics=['accuracy'])

	# save load
	model = load_model('./animal_cnn_aug.h5')

	return model

def main():
	image = Image.open(sys.argv[1])
	image = image.convert('RGB')
	image = image.resize((image_size, image_size))
	data = np.asarray(image)
	X = []
	X.append(data)
	X = np.array(X)
	model = build_model()

	result = model.predict([X])[0]
	predicted = result.argmax()
	persentage = int(result[predicted] * 100)
	print('{0} ({1} %)'.format(classes[predicted], persentage))

if __name__ == '__main__':
	main()