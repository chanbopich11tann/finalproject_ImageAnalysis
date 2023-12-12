# Example: Describe an image
import os
import io 
import json
import requests
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
from PIL import Image, ImageDraw, ImageFont

# Load credentials
credential = json.load(open('credential.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']
cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))


img_url = 'https://preview.redd.it/cl68jx3jprk71.jpg?width=640&crop=smart&auto=webp&s=ac05cca80dfb5db579343a59c99c76fa908d7517'

max_description = 3
response = cv_client.describe_image(img_url, max_description)

print(response)
for caption in response.captions:
    print('Image Description: {0}'.format(caption.text))
    print('Confidence: {0}'.format(caption.confidence * 100))

# Fetch the image
image_response = requests.get(img_url)
image = Image.open(io.BytesIO(image_response.content))

# Draw text on the image
draw = ImageDraw.Draw(image)
font_size = 20
font = ImageFont.truetype("./font/OpenSans-VariableFont_wdth,wght.ttf", font_size)
description = response.captions[0].text  # Considering the first caption
draw.text((10, 10), description, fill='blue', font=font)

# Save the image with a descriptive name
output_folder = './New Generated Images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_path = os.path.join(output_folder, 'described_image.jpg')
image.save(output_path)

print(f"Described image with text saved successfully at {output_path}")