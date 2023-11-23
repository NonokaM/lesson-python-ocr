import io
import os

from google.cloud import vision

def text_detection(image):
    response =  client.document_text_detection(image=image, image_context={'language_hints': ['ja']})

    print(response.full_text_annotation.text)

image_list = [
    {
        'type': 'テスト過去問題',
        'file_name': 'img.JPG'
    },
]

client = vision.ImageAnnotatorClient()

for im in image_list:
    print('検証画像：' + im['type'])

    file_name = os.path.abspath('resources/' + im['file_name'])

    # 画像をメモリにロード
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    text_detection(image)
