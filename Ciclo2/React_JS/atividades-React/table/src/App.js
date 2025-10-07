import { UseState } from "react";
import Formulario from "./components/Formulario";
import Tabela from "./components/Tabela";
import "./App.css";
import { useState } from "react";

function App() {
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [dataDeNascimento, setDataDeNascimento] = useState("");
  const [dados, setDados] = useState([]);

  const [editando, setEditando] = useState(false);
  const [index, setIndex] = useState(null);
  return (
    <div className="App">
      <Formulario
        nome={nome}
        setNome={setNome}
        cpf={cpf}
        setCpf={setCpf}
        dataDeNascimento={dataDeNascimento}
        setDataDeNascimento={setDataDeNascimento}
        dados={dados}
        setDados={setDados}
        editando={editando}
        setEditando={setEditando}
        index={index}
        setIndex={setIndex}
      />
      <Tabela
        dados={dados}
        setDados={setDados}
        setNome={setNome}
        setCpf={setCpf}
        setDataDeNascimento={setDataDeNascimento}
        setEditando={setEditando}
        setIndex={setIndex}
      />
    </div>
  );
}

export default App;
