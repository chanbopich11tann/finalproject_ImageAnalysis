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

cv_client = ComputerVisionClient(ENDPOINT, API_KEY)
