import './App.css';
import HelloWorld from './Components/HelloWorld';
import Frase from './Components/Frase';

function App() {

  const nome = "Sophia"

  const novoNome= nome.toLocaleUpperCase()

  const url = 'https://via.placeholder.com/150'

  function soma(x,y){
    return x + y
  }

  return (
    <div className="App">
      <h2>Alterando o JSX</h2>
      <p>Olá,{novoNome}!</p>
      <p>Soma = {soma(3,5 )}</p>
      <img src={url} alt='img'/>

      <HelloWorld/>
      <Frase/>
    </div>
  );
}

export default App;
