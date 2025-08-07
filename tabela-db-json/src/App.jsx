import { useState, useEffect } from "react";
import Form from "./componentes/Form";
import Tabela from "./componentes/Tabela";
import "./App.module.css";
import { getUser, getResp, cadastrarUser, getUsers } from "../src/service/api";
import { all } from "axios";

function App() {
  const [nome, setNome] = useState("");
  const [idade, setIdade] = useState("");
  const [estadoCivil, setEstadoCivil] = useState("");
  const [cpf, setCpf] = useState("");
  const [dados, setDados] = useState([]);

  useEffect(() => {
    getUsers().then((resp) => {
      setDados(resp);
    });
  }, [dados]);

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
    cadastrarUser(nome, idade, estadoCivil, cpf, dados, setDados);
    // let pessoa = {
    //   nome: nome,
    //   idade: idade,
    //   estadoCivil: estadoCivil,
    //   cpf: cpf,
    //   id: 1
    // };

    // setDados([...dados, pessoa]);

    console.log(dados);
    setNome("");
    setIdade("");
    setEstadoCivil("");
    setCpf("");
  }

  function cpfMask(cpf) {
    const listaCpf = [];
    let cpfForm = cpf.split("");
    if (cpfForm[3]) {
      const listaUm = [cpfForm[0], cpfForm[1], cpfForm[2]];
      listaCpf.push(listaUm);
      listaCpf.push(".");
    }
    if (cpfForm[6]) {
      const listaDois = [cpfForm[3], cpfForm[4], cpfForm[5]];
      listaCpf.push(listaDois);
      listaCpf.push(".");
    }
    if (cpfForm[9]) {
      const listaTres = [cpfForm[6], cpfForm[7], cpfForm[8]];
      listaCpf.push(listaTres);
      listaCpf.push("-");
    }
    if (cpfForm[10]) {
      const listaQuatro = [cpfForm[9], cpfForm[10]]
      listaCpf.push(listaQuatro);
    }
    return listaCpf.toString().replaceAll(",", "");
  }

  // const cpfMask = () => {
  //   let tamanhoCpf = cpf.length;
  //   let cpfFormatado = cpf;
  //   let arrayCpf = cpf.split("");
  //   console.log(tamanhoCpf);
  //   console.log(arrayCpf);
  //   if (tamanhoCpf === 4) {
  //     arrayCpf[4] = arrayCpf[3];
  //     arrayCpf[3] = ".";
  //     console.log(arrayCpf);
  //     cpfFormatado = arrayCpf.toString().replaceAll(",", "");
  //     tamanhoCpf = cpfFormatado.length;
  //     console.log(arrayCpf.toString().replaceAll(",", ""));
  //   } else if (tamanhoCpf === 8) {
  //     arrayCpf[4] = arrayCpf[3];
  //     arrayCpf[3] = ".";
  //     arrayCpf[8] = arrayCpf[7];
  //     arrayCpf[7] = ".";
  //     console.log(arrayCpf.toString().replaceAll(",", ""));
  //   } else if (tamanhoCpf === 12) {
  //     arrayCpf[4] = arrayCpf[3];
  //     arrayCpf[3] = ".";
  //     arrayCpf[8] = arrayCpf[7];
  //     arrayCpf[7] = ".";
  //     arrayCpf[12] = arrayCpf[11];
  //     arrayCpf[11] = ".";
  //     console.log(arrayCpf.toString().replaceAll(",", ""));
  //   }
  // };

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

      <h1>{cpfMask(cpf)}</h1>

      <button onClick={salvarDados}>Salvar</button>

      <Tabela dados={dados} setDados={setDados} />
    </>
  );
}

export default App;
