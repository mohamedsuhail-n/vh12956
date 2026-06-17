import { useState, useEffect } from 'react'

function App() {
  const [message, setMessage] = useState("Connecting to backend...")

  useEffect(() => {
    // Fetches live data from your local Express server port
    fetch('http://localhost:5000/api/test')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => {
        console.error(err)
        setMessage("Error connecting to backend server. Make sure it's running!")
      })
  }, [])

  return (
    <div style={{ padding: '40px', fontFamily: 'sans-serif', maxWidth: '600px', margin: '0 auto' }}>
      <h1 style={{ color: '#0066cc' }}>Afford Medical Workspace Baseline</h1>
      <hr />
      <div style={{ marginTop: '20px', padding: '20px', background: '#f4f4f5', borderRadius: '8px', border: '1px solid #e4e4e7' }}>
        <h3>Live API Response status:</h3>
        <p style={{ fontWeight: 'bold', color: '#16a34a' }}>{message}</p>
      </div>
    </div>
  )
}

export default App