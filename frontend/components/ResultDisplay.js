export default function ResultDisplay({ result }) {
  return (
    <div className="mt-4">
      <h2 className="text-xl font-semibold mb-2">Search Result:</h2>
      <p>{result}</p>
    </div>
  )
}

