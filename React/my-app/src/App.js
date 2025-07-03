import './App.css'

function App() {

  const name = "Kauan"
  const newName = name.toLocaleUpperCase()
  function sum(a, b) {
    return a + b
  }

   const url = "https://via.placeholder.com/150"

  return (
    <div className="App">
       <h2>Ola mundo</h2>
       <p>Ola {newName}</p>
       <p>Soma: {sum(1, 2)}</p>
       <img src={url} alt="Minha imagem" />
    </div>
  )
}

export default App;
