import { useEffect, useState } from "react";
import {
  buscarCategorias,
  deletandoDados,
  pegarDados,
  salvarDadosBanco,
  pegarCategoriasFiltro,
} from "../services/api";

import styles from "./Tela.module.css";

import Inputs from "./Inputs";
import Tabela from "./Tabela";

function Tela() {
  const [categoria, setCategoria] = useState([]);
  const [tarefa, setTarefa] = useState("");
  const [data, setData] = useState("");
  const [categoriaSelecionada, setCategoriaSelecionada] = useState("");
  const [dados, setDados] = useState([]);
  const [status, setStatus] = useState([]);
  const [filtratStatus, setFiltrarStatus] = useState("");

  useEffect(() => {
    buscarCategorias(setCategoria);
  }, []);

  useEffect(() => {
    pegarDadosBanco();
  }, []);

  useEffect(() => {
    setarStatus();
    setFiltrarStatus("Todos");
  }, []);

  async function pegarCategorias() {
    try {
      await buscarCategorias(setCategoria);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function salvarDados() {
    let listaDados = {
      tarefa: tarefa,
      categoriaSelecionada: categoriaSelecionada,
      data: data,
      status: "Em andamento",
    };

    try {
      await salvarDadosBanco(listaDados);
    } catch (err) {
      console.log("err :>> ", err);
    }

    setTarefa("");
    setCategoriaSelecionada("");
    setData("");

    pegarDadosBanco();
  }

  async function pegarDadosBanco() {
    try {
      const pegandoDados = await pegarDados();
      setDados(pegandoDados.data);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function deletarLinha(idLinha) {
    try {
      await deletandoDados(idLinha);
      pegarDadosBanco();
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function setarStatus() {
    try {
      const statusAdicionados = await pegarCategoriasFiltro();
      setStatus(statusAdicionados);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div>
      <Inputs
        categoria={categoria}
        pegarCategorias={pegarCategorias}
        setCategoriaSelecionada={setCategoriaSelecionada}
        salvarDados={salvarDados}
        dados={dados}
        deletarLinha={deletarLinha}
        setTarefa={setTarefa}
        setData={setData}
        data={data}
        tarefa={tarefa}
        categoriaSelecionada={categoriaSelecionada}
      />

      <div>
        <select
          name="selectStatus"
          id="selectStatus"
          className={styles.select}
          onChange={(e) => setFiltrarStatus(e.target.value)}
        >
          {status.map((st) => {
            return (
              <option value={st.nome} key={st.id}>
                {st.nome}
              </option>
            );
          })}
        </select>

        {filtratStatus === "Todos" ? (
          <Tabela
            dados={dados}
            categoria={categoria}
            deletarLinha={deletarLinha}
            pegarDadosBanco={pegarDadosBanco}
          />
        ) : (
          <Tabela
            dados={dados.filter((st) => st.status === filtratStatus)}
            categoria={categoria}
            deletarLinha={deletarLinha}
            pegarDadosBanco={pegarDadosBanco}
          />
        )}
      </div>
    </div>
  );
}

export default Tela;
