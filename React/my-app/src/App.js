import './App.css'
import HellWorld from './components/HelloWord'
import MeuNome from './components/MeuNome'
import Pessoa from './components/pessoa'


function App() {
    
  

  // const url = "https://picsum.photos/300"

  return (
    <div className="App">
       <HellWorld/> 
       <MeuNome nome="Kauan"/>
       <Pessoa 
       nome="Kauna" 
       idade="18" 
       profissao="Atendente"
       foto="https://picsum.photos/300"
       />
     </div>
  )
}

export default App;
