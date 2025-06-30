import './App.css';
import HelloWorld from './components/HelloWorld'
import SayMyName from './components/SayMyName'
import Pessoa from './components/Pessoa'
import Frase from './components/Frase';
import List from './components/List'

function App () {
  const nome = "Maria"

  return(
    <div className='App'>
      <h1>Testando CSS</h1>
      <Frase/>
      <Frase/>
      <HelloWorld/>
      <SayMyName nome="Matheus"/>
      <SayMyName nome="João"/>
      <SayMyName nome={nome}/>
      <Pessoa
        nome = "Kleber"
        idade = "10"
        profissao = "Chefão"
        foto = "/home/youx/youxlab-treino-git/my-app/public/foto01_coalas.jpg"
      />
     <List/>
    </div>
  )
}

export default App;
