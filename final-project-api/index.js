const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 6001;

// Middleware to parse JSON
app.use(express.json());

// Endpoint to receive image from Professor
app.post('/analyze-image', async (req, res) => {
  try {
    // Retrieve image URL from the request body
    const { image } = req.body;

    // Prepare payload for the vendor API
    const payload = {
      url: process.env.VENDOR_API_ENDPOINT + 'vision/v3.1/analyze',
      params: {
        visualFeatures: 'Categories,Description,Color',
        details: 'Celebrities,Landmarks',
        language: 'en',
      },
      data: {
        url: image, // Assuming the image URL is sent in the request body
      },
      headers: {
        'Ocp-Apim-Subscription-Key': process.env.VENDOR_API_KEY,
        'Content-Type': 'application/json',
      },
    };

    // Forward the request to the vendor API
    const vendorResponse = await axios.post(payload.url, payload.data, {
      params: payload.params,
      headers: payload.headers,
    });

    // Send the vendor API's response back to Professor
    res.json(vendorResponse.data);
  } catch (error) {
    // Handle any errors
    res.status(500).json({ error: error.message });
  }
});


app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
