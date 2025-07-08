import './App.css'
import HellWorld from './components/HelloWord'
import MeuNome from './components/MeuNome'
import Pessoa from './components/pessoa'
import List from './components/Lista'


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
      <List/>
     </div>
  )
}

export default App;
