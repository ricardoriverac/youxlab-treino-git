import './App.css';
import HelloWorld from './components/HelloWorld';

function App() {
  const nome = 'Tayla'
  const novoNome = nome.toUpperCase()

  function sum(a, b){
    return a + b
  }

  const url = 'https://picsum.photos/300'

  return ( 
    <div className="App">
      <h2>Alterando o JSX</h2>
      <p>Olá, {novoNome}</p>
      <p>Soma: {sum(1, 4)}</p>
      <img src={url} alt='Minha Imagem'/>
      <HelloWorld/>
    </div>
  );
}

export default App;