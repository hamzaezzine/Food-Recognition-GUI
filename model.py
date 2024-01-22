import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

model = load_model('Food.h5')

def predict_food(img_file):
	labels = {
		0: 'apple', 1: 'banana', 2: 'beetroot', 3: 'bell pepper', 4: 'cabbage', 5: 'capsicum', 6: 'carrot',
		7: 'cauliflower', 8: 'chilli pepper', 9: 'corn', 10: 'cucumber', 11: 'eggplant', 12: 'garlic', 13: 'ginger',
		14: 'grapes', 15: 'jalepeno', 16: 'kiwi', 17: 'lemon', 18: 'lettuce',
		19: 'mango', 20: 'onion', 21: 'orange', 22: 'paprika', 23: 'pear', 24: 'peas', 25: 'pineapple',
		26: 'pomegranate', 27: 'potato', 28: 'raddish', 29: 'soy beans', 30: 'spinach', 31: 'sweetcorn',
		32: 'sweetpotato', 33: 'tomato', 34: 'turnip', 35: 'watermelon'
	}

	def prepare_image(img_path):
		img = load_img(img_path, target_size=(224, 224, 3))
		img = img_to_array(img)
		img = img / 255
		img = np.expand_dims(img, [0])
		answer = model.predict(img)
		y_class = answer.argmax(axis=-1)
		y = " ".join(str(x) for x in y_class)
		y = int(y)
		res = labels[y]
		return res.capitalize()

	result = prepare_image(f"images\{img_file}")
	return result

