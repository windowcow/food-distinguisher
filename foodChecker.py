import tensorflow as tf
from PIL import Image
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from transformers import pipelines



extractor = AutoFeatureExtractor.from_pretrained("abhishek/autotrain-dog-vs-food")
model = AutoModelForImageClassification.from_pretrained("abhishek/autotrain-dog-vs-food")
THRESHOLD = 0.90

def isItFood(imgPath : str) -> bool :
	'''
	imgPath : /content/drive/Shareddrives/coco 앱개발 대회/non-food/이명근떡볶이_8.png
	THRESHOLD : 몇 퍼센트 이상인 경우에 음식이라 판단할지
	'''


	image = Image.open(imgPath)

	inputs = extractor(images=image, return_tensors="pt")
	outputs = model(**inputs)
	logits = outputs.logits

	s = tf.nn.softmax(logits.detach().numpy()).numpy()

	if s[0][1] > THRESHOLD :
		return True
	else:
		return False