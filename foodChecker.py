import tensorflow as tf
from PIL import Image
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from transformers import pipelines
     


extractor = AutoFeatureExtractor.from_pretrained("abhishek/autotrain-dog-vs-food")

model = AutoModelForImageClassification.from_pretrained("abhishek/autotrain-dog-vs-food")



image = Image.open("/content/drive/Shareddrives/coco 앱개발 대회/non-food/이명근떡볶이_8.png")

inputs = extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits


predicted_class_idx = logits.argmax(-1).item()
# print("Predicted class:", model.config.id2label[predicted_class_idx])

s = tf.nn.softmax(logits.detach().numpy()).numpy()

for index, probability in enumerate(s[0]):
  print(index, probability)
  if probability > 0.98:
    print(index)