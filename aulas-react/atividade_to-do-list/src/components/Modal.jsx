import { useEffect, useState } from "react";
import { editarDadosApi } from "../services/api";

import styles from "./Modal.module.css";

import Select from "./Select";

function Modal({
  isOpen,
  linhaClicada,
  pegarDadosBanco,
  categoria,
  setModalOpen,
  openModal,
  setOpenModal,
}) {
  const [tarefa, setTarefa] = useState("");
  const [categoriaSelecionada, setCategoriaSelecionada] = useState("");
  const [data, setData] = useState("");

  useEffect(() => {
    if (linhaClicada) {
      editarDados();
    }
  }, [linhaClicada]);

  async function editarDados() {
    setTarefa(linhaClicada.tarefa);
    setCategoriaSelecionada(linhaClicada.categoriaSelecionada);
    setData(linhaClicada.data);
  }

  async function salvarDadosEditados() {
    let listaDados = {
      tarefa: tarefa,
      categoriaSelecionada: categoriaSelecionada,
      data: data,
    };

    try {
      await editarDadosApi(linhaClicada.id, listaDados);
    } catch (err) {
      console.log("err :>> ", err);
    } finally {
      pegarDadosBanco();
    }
  }

  if (isOpen) {
    return (
      <div className={styles.caixa}>
        <div className={styles.conteudo}>
          <div className={styles.titulo}>
            <h2 className={styles.h2}>Editar tarefas</h2>
          </div>
          <div className={styles.divInputs}>
            <input
              type="text"
              className={styles.inputNome}
              placeholder="Nome da tarefa"
              onChange={(e) => setTarefa(e.target.value)}
              value={tarefa}
            />

            <Select
              nome="category_id"
              categorias={categoria}
              setCategoriaSelecionada={setCategoriaSelecionada}
              categoriaSelecionada={categoriaSelecionada}
            />

            <input
              type="date"
              className={styles.inputData}
              onChange={(e) => setData(e.target.value)}
              value={data}
            />
          </div>
          <div className={styles.divBotoes}>
            <button
              onClick={() => {
                salvarDadosEditados();
                setOpenModal(!openModal);
              }}
              className={styles.btn}
            >
              Salvar
            </button>
            <button onClick={setModalOpen} className={styles.btnFechar}>
              Fechar
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default Modal;
