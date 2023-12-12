const express = require('express');
const axios = require('axios');
const fs = require('fs');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 6001;

// Middleware to parse JSON
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Define a route handler for the root endpoint
app.get('/', (req, res) => {
  res.send('Welcome to the image analysis service!');
});

app.get('/analyze-image', async (req, res) => {
  try {
    // Extract image URL from the query parameter
    const imageUrl = req.query.image;

    // Call the handwriting detection logic here using Azure Cognitive Services or other services
    const vendorEndpoint = process.env.VENDOR_API_ENDPOINT;
    const apiKey = process.env.VENDOR_API_KEY;

    // Implement your logic to call the vendor's API with the provided image URL
    const vendorVisionEndpoint = `${vendorEndpoint}/vision/v3.1/analyze`;

    // Set up request headers and parameters as needed by the vendor's API
    const headers = {
      'Content-Type': 'application/json',
      'Ocp-Apim-Subscription-Key': apiKey,
    };

    const payload = {
      url: imageUrl, // Assuming the image URL is sent as a query parameter
      visualFeatures: 'Categories,Description,Color',
      details: 'Celebrities,Landmarks',
      language: 'en',
    };

    const vendorResponse = await axios.post(vendorVisionEndpoint, payload, { headers });

    // Process the response from the vendor's API
    const vendorData = vendorResponse.data;

    // You can send the extracted text or any other processed data back to the client
    res.json(vendorData);
  } catch (error) {
    console.error('Error:', error.response ? error.response.data : error.message);
    res.status(500).json({ error: 'An error occurred while processing the image.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
