import "./App.css";
import HelloWord from "./components/HelloWord";
import SayMyName from "./components/SayMyName";
import Pessoa from "./components/Pessoa";
import Frase from "./components/Frase";

function App() {
  const name = "Aléxia";
  const newName = name.toUpperCase();

  function sum(a, b) {
    return a + b;
  }

  const url = "https://picsum.photos/300";
  const nome = "sophia";

  return (
    <div className="App">
      <h1>Testando CSS</h1>
      <Frase />
      <Frase />
      <SayMyName nome="Aléxia" />
      <SayMyName nome="Paim" />
      <SayMyName nome={nome} />
      <Pessoa
        nome="Alexia"
        idade="16"
        profissao="Estudante"
        foto="https://picsum.photos/300"
      />
    </div>
  );
}

export default App;
