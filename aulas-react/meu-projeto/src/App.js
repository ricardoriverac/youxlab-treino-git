import "./App.css";
import SayMyName from "./components/SayMyName";
import Pessoa from "./components/Pessoa";

function App() {
  const nome = "Maria";

  return (
    <div className="App">
      <SayMyName nome="Tayla" />
      <SayMyName nome="João" />
      <SayMyName nome={nome} />

      <Pessoa
        nome="Tayla"
        idade="16"
        profissao="Programador"
        foto="https://picsum.photos/300"
      />
    </div>
  );
}

export default App;