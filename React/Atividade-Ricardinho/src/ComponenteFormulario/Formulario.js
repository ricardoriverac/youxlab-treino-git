import { useState, useEffect } from "react";
import style from "./formulario.module.css";
import FormularioInputs from "../componeteInputs/formularioInputs";
import TabelaDados from "../ComponenteTabela/tabela";
import { listarPessoas, salvarPessoa, ApagarPessoas, EditarPessoa } from "../services/api";

function Formulario() {
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [data, setData] = useState("");
  const [idEditado, setIdEditado] = useState(null);
  const [dados, setDados] = useState([]);

  useEffect(() => {
    carregarDados();
  }, []);

  async function carregarDados() {
    const resposta = await listarPessoas();
    setDados(resposta.data);
  }

  async function adicionar(item) {
    try {
      if (idEditado) {
        await EditarPessoa(idEditado, item);
        carregarDados(null);
      } else {
        await salvarPessoa({nome, cpf, data});
      }
      LimparInputs();
     carregarDados();
    } catch (error) {
      console.error(error);
    }
  }

  async function remover(id) {
    try {
      await ApagarPessoas(id);
      carregarDados();
    } catch (error) {
      console.error(error);
    }
  }

  async function editar(item) {
    setIdEditado(item.id);
    setNome(item.nome);
    setCpf(item.cpf);
    setData(item.data);
  }

  function LimparInputs() {
    setNome("");
    setCpf("");
    setData("");
  }

  return (
    <div>
      <h2 className={style.h2}>Cadastro</h2>
      <FormularioInputs
        nome={nome}
        cpf={cpf}
        data={data}
        setNome={setNome}
        setCpf={setCpf}
        setData={setData}
        adicionar={adicionar}
      />
      <TabelaDados dados={dados} remover={remover} editar={editar} />
    </div>
  );
}

export default Formulario;
