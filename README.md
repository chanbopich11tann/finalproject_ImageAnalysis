# Final Project Documentation
---

# API Name: Image Analysis

## Purpose

This API facilitates various image processing tasks like handwriting extraction, landmark detection, and image description using Azure Cognitive Services. It provides functionalities to interact with Azure's Computer Vision API.

## Getting Started

### Installation

To get started, ensure you have Python installed. Then, clone the repository and install the required dependencies using the following commands:

```bash
git clone https://github.com/chanbopich11tann/finalproject_ImageAnalysis.git
cd final_project_api
```

### Authentication

1. I obtained an API key and endpoint from Azure Cognitive Services.
2. I created a `credential.json` file in the root directory with the following structure:

```json
{
    "API_KEY": "d5dab499fc804fb28355568d460055f8",
    "ENDPOINT": "https://ai-vision-api-demo.cognitiveservices.azure.com/"
} 
```

## Usage

### 1. Handwriting Extraction

#### Purpose

The Handwriting Extraction functionality in our API utilizes Azure Cognitive Services to detect and extract handwritten text from images. Detail Code can be found in `example1.py` file.


#### Explanation

The provided code snippet demonstrates the process of extracting handwritten text from an image using our API, leveraging Azure Cognitive Services' AI Vision capabilities.

1. **Loading Credentials:** The code initializes the API client by loading the necessary credentials from the `credential.json` file.

2. **Initializing the Client:** It creates the Computer Vision client using the loaded credentials to interact with Azure Cognitive Services.

3. **Handwriting Extraction:** The API performs handwriting extraction on a local image file (for example, `1.png`) in `Images` folder by sending a request to the Cognitive Services API and retrieving the extracted text.

Original Handwriting Image: 
![](final_project_api/Images/1.png)

5. **Text Annotation:** The script visualizes the extracted text by drawing bounding boxes around the identified text lines on the image.

Extracted Text: 
![](final_project_api/Images/text1.png)

Extracted Image: 
![](final_project_api/New%20Generated%20Images/handwriting_result.jpg)


7. **Saving the Modified Image:** The modified image, with highlighted text areas, is saved in a new folder named 'New Generated Images' as 'handwriting_result.jpg'.

### Usage Instructions

1. **Install Dependencies:** Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.

2. **Authentication:** Obtain the API key and endpoint from Azure Cognitive Services and create a `credential.json` file in the root directory following the provided format.

3. **Run the Example:** Replace the placeholder code in the example with your actual code and execute it to extract handwriting from your images.

### Note

Make sure to replace the placeholders in the code example (`[Insert the code example here]`) with your actual Python code for handwriting extraction using the Azure Cognitive Services API.

---

Enhance this section by embedding code snippets, explanations, and additional details specific to your API's Handwriting Extraction functionality. Incorporate visuals such as images or diagrams to illustrate the process for clearer understanding.
#### Code Example:

```python
# Code for handwriting extraction
# ...
```

### Landmark Detection

#### Code Example:

```python
# Code for landmark detection
# ...
```

### Image Description

#### Code Example:

```python
# Code for image description
# ...
```

## Error Handling

The API handles errors gracefully. Check the response status and handle exceptions as needed. Refer to the API documentation for error codes and messages.

## Best Practices

- Use descriptive variable names in your code.
- Ensure proper error handling to manage unexpected scenarios.
- Optimize API calls by batching requests where possible.

## Support

For any queries or support, contact us at support@example.com.

## Contributing

We welcome contributions! Follow our [contribution guidelines](CONTRIBUTING.md) to contribute to this project.

## License

This project is licensed under the [LICENSE_NAME](LICENSE) - e.g., MIT License.

---

Enhance this README with real code snippets, explanations, and examples. Embed images or GIFs to illustrate usage wherever necessary. Organize sections, provide clear explanations, and use markdown formatting to improve readability.

Consider creating separate files (like CONTRIBUTING.md, LICENSE, etc.) and linking them appropriately in the README for a more organized repository structure.

This template serves as a foundation; you can build upon it with actual code snippets, visual aids, and detailed explanations to create an excellent documentation README for your API.
