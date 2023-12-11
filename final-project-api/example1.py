import os
import io 
import json

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
import requests # pip install requests
from PIL import Image, ImageDraw, ImageFont

credential = json.load(open('credential.json'))

API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']

cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

image_url = ''
local_file = './Image/1.jpg'
response = cv_client.read(url =image_url,Language='en', raw=True)
response = cv_client.read_in_stream(open(local_file, 'rb')
)
operationLocation = response.headers['Operation-Location']
Operation_id = operationLocation.split('/')[-1]
result = cv_client.get_read_result(operation_id)

print(result)
print(result.status)
print(result.analyze_result)

if result.status == OperationStatusCodes.succeeded:
    read_results = result.analyze_result.read_results
    for analyzed_result in read_results:
        for line in analyzed_result.lines:
            print('line: ')
            print(line.text)
            for word in line.words:
                print('Words:')
                print(word.text)
            break

{'additional_properties': {}, 'language': None,
'bounding_box': []}