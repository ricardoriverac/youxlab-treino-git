import "./App.css";
import HelloWorld from "./Components/HelloWorld";
import SayMyName from "./Components/SayMyName";
import Pessoa from "./Components/Pessoa";

function App() {
  const nome = "Yago";

  return (
    <div className="App">
      <HelloWorld />
      <SayMyName nome="Sophia" />
      <SayMyName nome="Sarah" />
      <SayMyName nome={nome} />
      <Pessoa
        nome="Elena"
        idade="17"
        profissao="Product"
        foto="https://via.placeholder.com/150"
      />
    </div>
  );
}

export default App;
