# Example 2: Detect Landmarks
import os
import io 
import json
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from PIL import Image, ImageDraw, ImageFont

# Load credentials
credential = json.load(open('credential.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']
cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

# Detect Landmarks
domain = 'landmarks'
image_path = './Images/landmark2.png' 
with open(image_path, 'rb') as image_file:
    analysis = cv_client.analyze_image_by_domain_in_stream(model=domain, image=image_file)
for landmark in analysis.result.get('landmarks', []):
    print(landmark['name'])

# Open the image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)
font_path = "./font/OpenSans-VariableFont_wdth,wght.ttf"
font = ImageFont.truetype(font_path, 40)  # Larger font size for landmark name

# Display landmark names on the image
if analysis.result and 'landmarks' in analysis.result:
    for landmark in analysis.result['landmarks']:
        landmark_name = landmark.get('name', 'Unknown')
        # Display the name at the top left corner with some margin
        draw.text((20, 20), landmark_name, fill='blue', font=font)

# Display the annotated image
image.show()

# Save the modified image in a new folder
output_folder = './New Generated Images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_path = os.path.join(output_folder, 'annotated_landmark_image.jpg')
image.save(output_path)