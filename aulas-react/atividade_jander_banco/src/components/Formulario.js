import { useEffect, useState } from "react";
import styles from "./Formulario.module.css";

import Tabela from "./Tabela";
import {
  buscarTodosDados,
  editarDadosApi,
  salvarNovosDados,
} from "../services/api";

function Formulario() {
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [dataNascimento, setDataNascimento] = useState("");
  const [telefone, setTelefone] = useState("");
  const [dados, setDados] = useState([]);

  let editando = false;

  useEffect(() => {
    buscarDados();
  }, []);

  async function salvarDados() {
    if (editando === false) {
      let listaDados = {
        name: nome,
        cpf: cpf,
        telefone: telefone,
        nascimento: dataNascimento,
      };
      if (
        listaDados.name === "" ||
        listaDados.cpf === "" ||
        listaDados.telefone === "" ||
        listaDados.nascimento === ""
      ) {
        alert("Preencha todos os campos");
      } else {
        try {
          await salvarNovosDados(listaDados);
        } catch (err) {
          alert("Deu ruim");
          console.log("err :>> ", err);
        }

        setNome("");
        setCpf("");
        setTelefone("");
        setDataNascimento("");

        buscarDados();
      }
    }
  }

  async function buscarDados() {
    try {
      const pegandoDados = await buscarTodosDados();
      setDados(pegandoDados.data);
    } catch (err) {
      alert("Deu ruim");
      console.log("err :>> ", err);
    }
  }

  async function editarDados(index) {
    try {
      const linhaEditada = dados[index];
      setNome(linhaEditada.name);
      setCpf(linhaEditada.cpf);
      setTelefone(linhaEditada.telefone);
      setDataNascimento(linhaEditada.nascimento);
      
      await editarDadosApi(dados, index);
      // editando = true;
      // console.log("dados :>> ", dados);
      // await editarDadosApi(dados, index);

      // editando = false;
    } catch (err) {
      // alert("Deu ruim");
      console.log("err :>> ", err);
    }
  }

  return (
    <div className={styles.quadradoGrande}>
      <h2>Novo Cadastro</h2>
      <div className={styles.linha}>
        <p>
          {/* <label>Nome: </label> */}
          <input
            placeholder="Digite seu nome"
            className={styles.inputs}
            value={nome}
            type="text"
            onChange={(e) => setNome(e.target.value)}
          />
        </p>

        <p>
          {/* <label>CPF: </label> */}
          <input
            placeholder="Digite seu CPF"
            className={styles.inputs}
            value={cpf}
            type="text"
            onChange={(e) => setCpf(e.target.value)}
          />
        </p>

        <p>
          {/* <label>CPF: </label> */}
          <input
            placeholder="Digite o número de telefone"
            className={styles.inputs}
            value={telefone}
            type="text"
            onChange={(e) => setTelefone(e.target.value)}
          />
        </p>

        <p>
          {/* <label>Data de Nascimento: </label> */}
          <input
            className={styles.inputs}
            value={dataNascimento}
            type="date"
            onChange={(e) => setDataNascimento(e.target.value)}
          />
        </p>

        <button className={styles.botao} onClick={salvarDados}>
          Salvar Dados
        </button>
      </div>
      <Tabela dados={dados} setDados={setDados} editarDados={editarDados} />
    </div>
  );
}
export default Formulario;
