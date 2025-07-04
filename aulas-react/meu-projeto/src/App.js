import "./App.css";
import SayMyName from "./components/SayMyName";
import Pessoa from "./components/Pessoa";
import Frase from "./components/Frase";
import List from "./components/List";

function App() {
  const nome = "Maria";

  return (
    <div className="App">
      <h1>Testando CSS</h1>
      <Frase/>
      <Frase/>
      <SayMyName nome="Tayla" />
      <SayMyName nome="João" />
      <SayMyName nome={nome} />

      <Pessoa
        nome="Tayla"
        idade="16"
        profissao="Programador"
        foto="https://picsum.photos/150"
      />
      <List/>
    </div>
  );
}

export default App;