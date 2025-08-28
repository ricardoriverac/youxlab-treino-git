import "./App.css";
import SayMyName from "./Components/SayMyName";
import Pessoa from "./Components/Pessoa";
import Frase from "./Components/Frase";
import List from "./Components/List";

function App() {
  const nome = "Yago";

  return (
    <div className="App">
      <h1>Testando CSS</h1>
      <Frase/>
      <SayMyName nome="Sophia" />
      <SayMyName nome="Sarah" />
      <SayMyName nome={nome} />
      <Pessoa
        nome="Elena"
        idade="17"
        profissao="Product"
        foto="https://via.placeholder.com/150"
      />
      <List/>
    </div>
  );
}

export default App;
