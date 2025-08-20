import { useEffect, useState } from "react";
import styles from "./Formulario.module.css";

import Tabela from "./Tabela";
import {
  buscarTodosDados,
  deletandoDados,
  editarDadosApi,
  salvarNovosDados,
} from "../services/api";

function Formulario() {
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [dataNascimento, setDataNascimento] = useState("");
  const [telefone, setTelefone] = useState("");
  const [dados, setDados] = useState([]);
  const [editando, setEditando] = useState(false);
  const [id, setId] = useState("");
  const [selecionados, setSelecionados] = useState([]);
  const [marcado, setMarcado] = useState(false);

  useEffect(() => {
    buscarDados();
  }, []);

  useEffect(() => {
    // console.log('selecionados :>> ', selecionados);
  }, [selecionados])

  async function salvarDados() {
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
        if (!editando) {
          await salvarNovosDados(listaDados);
        } else {
          await editarDadosApi(listaDados, id);
        }
      } catch (err) {
        alert("Deu ruim");
        console.log("err :>> ", err);
      } finally {
        setEditando(false);
        setId("");
      }

      setNome("");
      setCpf("");
      setTelefone("");
      setDataNascimento("");

      buscarDados();
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

  async function editarDados(pessoa) {
    setEditando(true);
    setNome(pessoa.name);
    setCpf(pessoa.cpf);
    setTelefone(pessoa.telefone);
    setDataNascimento(pessoa.nascimento);
    setId(pessoa.id);
  }

  async function removerDados(idPessoa) {
    try {
      await deletandoDados(idPessoa);
      buscarDados();
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function removerTodos() {
    try {
      for (let i = 0; i < dados.length; i++) {
        await deletandoDados(dados[i].id);
        buscarDados();
      }
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function marcarSelecionados(idPessoa) {
    console.log('idPessoa :>> ', idPessoa);

    if (selecionados.includes(idPessoa)) {
      const copiaSelecionados = [...selecionados]
      console.log('antes :>> ', copiaSelecionados);
      
      const pegarIndexSelecionado = selecionados.findIndex(id => id === idPessoa)

      copiaSelecionados.splice(pegarIndexSelecionado ,1)

      console.log('depois :>> ', copiaSelecionados);
      setSelecionados(copiaSelecionados);
    } else {
      setSelecionados([...selecionados, idPessoa]);
    }

  }

  async function handleChange(e) {
    setMarcado(e.target.marcado)
  }

  async function removerSelecionados() {
    for (let i = 0; i < selecionados.length; i++) {
      try {
        await deletandoDados(selecionados[i]);
        buscarDados();
      } catch (err) {
        console.log("err :>> ", err);
      }
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

        <button className={styles.botao} onClick={removerTodos}>
          Apagar todos
        </button>
        <button className={styles.botao} onClick={removerSelecionados}>
          Apagar selecionados
        </button>
      </div>
      <Tabela
        dados={dados}
        setDados={setDados}
        editarDados={editarDados}
        deletarDados={removerDados}
        marcarSelecionados={marcarSelecionados}
        marcado={marcado}
        handleChange={handleChange}
      />
    </div>
  );
}
export default Formulario;
