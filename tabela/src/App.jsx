import { useState } from "react";
import Form from "./componentes/Form";
import Tabela from "./componentes/Tabela";
import './App.module.css'

function App() {
  const [nome, setNome] = useState('');
  const [idade, setIdade] = useState('');
  const [estadoCivil, setEstadoCivil] = useState('');
  const [cpf, setCpf] = useState('');
  const [dados, setDados] = useState([])

  const handleChangeName = (e) => {
    setNome(e.target.value);
  };

  const handleChangeIdade = (e) => {
    setIdade(e.target.value);
  };

  const handleChangeEstadoCivil = (e) => {
    setEstadoCivil(e.target.value);
  };

  const handleChangeCpf = (e) => {
    setCpf(e.target.value);
  };

  function salvarDados() {
    let pessoa = {
      nome: nome,
      idade: idade,
      estadoCivil: estadoCivil,
      cpf: cpf,
      id: 1
    };

    setDados([...dados, pessoa]);

    console.log(dados);
    setNome('')
    setIdade('')
    setEstadoCivil('')
    setCpf('')
  }

  return (
    <>
      <h2>Novo Cadastro</h2>
      <Form
        text="Nome"
        type="text"
        name="name"
        value={nome}
        onChange={handleChangeName}
      />

      <Form
        text="Idade"
        type="number"
        name="name"
        value={idade}
        onChange={handleChangeIdade}
      />

      <Form
        text="Estado Civil"
        type="text"
        name="name"
        value={estadoCivil}
        onChange={handleChangeEstadoCivil}
      />

      <Form
        text="CPF"
        type="number"
        name="name"
        value={cpf}
        onChange={handleChangeCpf}
      />

      <button onClick={salvarDados}>Salvar</button>

      <Tabela 
        dados={dados}
        setDados={setDados}
      />
    </>
  );
}

export default App;
