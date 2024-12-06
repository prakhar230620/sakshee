export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { query } = req.body

    try {
      const response = await fetch('http://localhost:5000/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      })

      const data = await response.json()
      res.status(200).json({ result: data.result })
    } catch (error) {
      res.status(500).json({ error: 'An error occurred while processing your request' })
    }
  } else {
    res.status(405).json({ error: 'Method not allowed' })
  }
}

