import './App.css';
import HelloWord from './components/HelloWord';

function App() {
  const name = 'Aléxia'
  const newName = name.toUpperCase()

  function sum(a, b){
    return a + b
  }

  const url = "https://picsum.photos/300"
  return (

    <div className="App">
     <h1>ALterando o JSX</h1>
     <p> Olá, {newName}</p>
     <p> Soma: {2+2}</p>
     <img src={url} alt="Minha Imagem" />
     <HelloWord />
    </div>

  );
}

export default App;
