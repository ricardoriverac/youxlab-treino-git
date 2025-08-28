import { FaPen, FaTrash } from "react-icons/fa";
import { useState } from "react";
import { editarDadosApi } from "../services/api";

import Modal from "./Modal";
import styles from "./Tabela.module.css";

function Tabela({ dados, deletarLinha, categoria, pegarDadosBanco }) {
  const [openModal, setOpenModal] = useState(false);
  const [linhaClicada, setLinhaClicada] = useState(null);

  async function editarStatus(idLinha, linha) {
    if (linha.status !== "Concluido") {
      linha.status = "Concluido";
    } else {
      linha.status = "Em andamento";
    }

    try {
      await editarDadosApi(idLinha, linha);
      pegarDadosBanco();
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div>
      <Modal
        isOpen={openModal}
        setModalOpen={() => setOpenModal(!openModal)}
        categoria={categoria}
        linhaClicada={linhaClicada}
        pegarDadosBanco={pegarDadosBanco}
        openModal={openModal}
        setOpenModal={setOpenModal}
      />

      <table className={styles.tabela}>
        <thead>
          <tr>
            <th>Concluir</th>
            <th>Tarefa</th>
            <th>Categoria</th>
            <th>Data de entrega</th>
            <th>Status</th>
            <th>Editar</th>
            <th>Deletar</th>
          </tr>
        </thead>
        <tbody>
          {dados.length ? (
            dados.map((linha, i) => {
              return (
                <tr key={i}>
                  <td>
                    <input
                      checked={linha.status === "Concluido"}
                      type="checkbox"
                      onChange={() => editarStatus(linha.id, linha)}
                    />
                  </td>
                  <td>{linha.tarefa}</td>
                  <td>{linha.categoriaSelecionada}</td>
                  <td>{linha.data}</td>
                  <td>
                    <label
                      className={
                        linha.status === "Concluido"
                          ? styles.statusConcluido
                          : styles.statusPendente
                      }
                    >
                      {linha.status}
                    </label>
                  </td>
                  <td>
                    <button
                      onClick={() => {
                        setOpenModal(true);
                        setLinhaClicada(linha);
                      }}
                      className={styles.icon}
                    >
                      <FaPen />
                    </button>
                  </td>
                  <td>
                    <button
                      className={styles.icon}
                      onClick={() => deletarLinha(linha.id)}
                    >
                      <FaTrash />
                    </button>
                  </td>
                </tr>
              );
            })
          ) : (
            <tr>
              <td>vazio</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
