# Example 1: Handwriting Extraction
import os
import io 
import json
import time
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests # pip install requests
from PIL import Image, ImageDraw, ImageFont

credential = json.load(open ('credential.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

image_url = 'https://i.redd.it/pf440nc480921.jpg'
local_file = './Images/1.png'
# response = cv_client.read(url =image_url,Language='en', raw=True)

response = cv_client.read_in_stream(open(local_file, 'rb'), Language='en', raw=True)
operationLocation = response.headers['Operation-Location']
operation_id = operationLocation.split('/')[-1]
time.sleep(5)
result = cv_client.get_read_result(operation_id)

#print(result)
#print(result.status)
#print(result.analyze_result)

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyzed_result in read_results:
        for line in analyzed_result.lines:
            print(line.text)
            #for word in line.words:
            #    print('Words:')
            #    print(word.text)

image = Image.open(local_file)
# Convert from RGBA to RGB
if image.mode == 'RGBA':
    image = image.convert('RGB')

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyzed_result in read_results:
        for line in analyzed_result.lines:
            x1, y1, x2, y2, x3, y3, x4, y4 = line.bounding_box
            draw = ImageDraw.Draw(image)
            draw.line(
                ((x1, y1), (x2, y1), (x2, y2), (x3, y2), (x3, y3), (x4, y3), (x4, y4), (x1, y4), (x1, y1)),
                fill = (255, 0, 0),
                width=5
            )
image.show()

# Save the modified image in a new folder
output_folder = './New Generated Images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_path = os.path.join(output_folder, 'handwriting_result.jpg')
image.save(output_path)

