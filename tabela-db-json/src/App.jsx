import { useState, useEffect } from "react";
import Form from "./componentes/Form";
import Tabela from "./componentes/Tabela";
import "./App.module.css";
import { cadastrarUser, getUsers } from "../src/service/api";
import FormCpf from "./componentes/FormCpf";

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
    cpfMask2(e.target.value);
  };

  function cpfMask2(cpf) {
    if (cpf.length < 3) {
      setCpf(cpf);
    } else if (cpf.length === 3) {
      let copy = `${cpf}.`;
      setCpf(copy);
    } else if (cpf.length > 3 && cpf.length < 7) {
      setCpf(cpf);
    } else if (cpf.length === 7) {
      let copy = `${cpf}.`;
      setCpf(copy);
    } else if (cpf.length > 7 && cpf.length < 11) {
      setCpf(cpf);
    } else if (cpf.length === 11) {
      let copy = `${cpf}-`;
      setCpf(copy);
    } else if (cpf.length > 12) {
      setCpf(cpf)
    }
  }

   function salvarDados() {
    if (nome === "" || idade === "" || estadoCivil === "" || cpf === "") {
      alert("Preencha os campos antes de salvar!");
    } else {
      cadastrarUser(nome, idade, estadoCivil, cpf, dados, setDados);
      console.log(dados);
      setNome("");
      setIdade("");
      setEstadoCivil("");
      setCpf("");
    }
  }


  function cpfMask(cpf) {
    const listaCpf = [];
    let cpfForm = cpf.split("");
    const listaUm = [cpfForm[0], cpfForm[1], cpfForm[2]];
    listaCpf.push(listaUm);
    const listaDois = [cpfForm[3], cpfForm[4], cpfForm[5]];
    if (cpfForm[2]) {
      listaCpf.push(".");
    } else if (cpfForm[5]) {
      listaCpf.push(".");
    } else if (cpfForm[8]) {
      listaCpf.splice(11, 1, "7");
    }

    let listaCpfForm = listaCpf.toString().replaceAll(",", "");

    return listaCpfForm;
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

      <FormCpf
        text="CPF"
        type="text"
        name="name"
        value={cpf}
        onChange={handleChangeCpf}
        maxLength={14}
      />

      <button onClick={salvarDados}>Salvar</button>

      <Tabela dados={dados} setDados={setDados} />
    </>
  );
}

export default App;

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
