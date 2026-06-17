const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors()); 
app.use(express.json()); 

// Test route to confirm connectivity
app.get('/api/test', (req, res) => {
    res.json({ message: "Hello from the Windows Backend Server!" });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Backend live on http://localhost:${PORT}`));