import { useState } from "react";
import Formulario from "./components/Formulario";
import Tabela from "./components/Tabela";

function App() {
  const [dados, setDados] = useState([]);
  const [nome, setNome] = useState("");
  const [cpf, setCPF] = useState("");
  const [nascimento, setNascimento] = useState("");

  function salvarPessoa(novaPessoa) {
    setDados([...dados, novaPessoa]);
  }

  return (
    <div>
      <Formulario salvarPessoa={salvarPessoa} dados={dados} setDados={setDados} nome={nome} nascimento={nascimento} cpf={cpf} setNome={setNome} setCPF={setCPF} setNascimento={setNascimento} />
      <Tabela dados={dados} setDados={setDados} setNome={setNome} setCPF={setCPF} setNascimento={setNascimento} />
    </div>
  );
}

export default App;
