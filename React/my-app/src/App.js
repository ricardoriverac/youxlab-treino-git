import './App.css'
import HellWorld from './components/HelloWord'

function App() {

  const name = "Kauan"
  const newName = name.toLocaleUpperCase()
  function sum(a, b) {
    return a + b
  }

  const url = "https://picsum.photos/300"

  return (
    <div className="App">
       <h2>Ola mundo</h2>
       <p>Ola {newName}</p>
       <p>Soma: {sum(3, 2)}</p>
       <img src={url} alt="Minha imagem" />
       <HellWorld/> 
       <segundo/>   
     </div>
  )
}

export default App;
