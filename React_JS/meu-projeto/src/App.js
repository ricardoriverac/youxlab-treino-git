import "./App.css";
import OutraLista from "./Components/Outralista";
function App() {

  const minhaLista=["React", "HTML" , "Javascript"]

  return ( 
    <div className="App">
      <h1>Renderização de Listas</h1>
      <OutraLista itens={minhaLista}/>
      <OutraLista itens={[]}/>
    </div>
  );
}

export default App;
