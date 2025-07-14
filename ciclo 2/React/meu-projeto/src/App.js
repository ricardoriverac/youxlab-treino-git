import "./App.css";
import Condicional from "./components/Condicional";
import OutraLista from "./components/OutraLista";
function App() {
  const meusItens = ['React', 'Vue', 'Angular']

  return (
    <div className="App">
      <h1>Rederização condicional</h1>
      <OutraLista itens={meusItens} />
      </div>
  );
}

export default App;
