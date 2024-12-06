import { useState } from 'react'
import SearchForm from '../components/SearchForm'
import ResultDisplay from '../components/ResultDisplay'

export default function Home() {
  const [result, setResult] = useState('')

  const handleSearch = async (query) => {
    const response = await fetch('/api/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query })
    })
    const data = await response.json()
    setResult(data.result)
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Web Content Search</h1>
      <SearchForm onSearch={handleSearch} />
      <ResultDisplay result={result} />
    </div>
  )
}

