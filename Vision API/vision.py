import io
from google.cloud import vision

vision_client = vision.Client()
file_name = 'ee0e0e7b8e70210a2c808c45b7033086.jpg'

with io.open(file_name,'rb') as f:
    content = f.read()
    image = vision_client.image(content=content)

labels = image.detect_labels()

print('Image Labels:\n')
for l in labels:
    print(l.description, l.score)

print('\nText in Image:\n')
print(image.detect_full_text().text)
