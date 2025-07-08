import "./App.css";
import OutraLista from "./components/OutraLista";

function App() {

  const meusItems = ['React', 'Vue', 'Angular']

  return (
    <div className="App">
      <h1>Renderização de Listas</h1>
      <OutraLista itens={meusItems}/>
      <OutraLista itens={[]}/>
    </div>
  );
}

export default App;