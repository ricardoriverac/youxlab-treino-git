import './App.css'

import MinhaLista from './components/Renderizar-Listas';

function App() {
    
   const minhaLista = ["React","Vue","Angular"]

  return (
    <div className="App">
      <h1>Rederização</h1>
      <MinhaLista itens={minhaLista}/>
      <MinhaLista itens={[]}/>
     </div>
  )
}

export default App;
