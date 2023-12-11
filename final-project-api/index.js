const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Endpoint to access the vendor API
app.post('/api/vendor', async (req, res) => {
  try {
    // Process request from Professor John
    // Prepare payload or handle data as needed
    
    // Forward the request to the vendor API
    const vendorResponse = await axios.post('VENDOR_API_ENDPOINT', req.body, {
      headers: {
        'Authorization': 'Bearer YOUR_VENDOR_API_KEY',
        'Content-Type': 'application/json'
      }
    });

    // Return the vendor API response to Professor John
    res.json(vendorResponse.data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

