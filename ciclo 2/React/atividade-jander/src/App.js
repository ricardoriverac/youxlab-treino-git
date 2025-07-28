import { useState } from "react";
import Formulario from "./components/Formulario";
import Tabela from "./components/Tabela";

function App() {
  const [dados, setDados] = useState([]);

  function salvarPessoa(novaPessoa) {
    setDados([...dados, novaPessoa]);
  }

  return (
    <div>
      <Formulario salvarPessoa={salvarPessoa} />
      <Tabela dados={dados} />
    </div>
  );
}

export default App;
