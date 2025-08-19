import styles from "./Tabela.module.css";
import DeleteOutlineIcon from "@mui/icons-material/DeleteOutline";
import * as React from "react";
import { useState } from "react";
import Modal from "./Modal";
import EditIcon from "@mui/icons-material/Edit";
import {
  getUser,
  deleteUser,
  deleteUsers,
  selecionadosUsers
} from "../service/api";

function Tabela({ dados, setDados }) {
  const [abrirModal, setAbrirModal] = useState(false);
  const [pessoaEdit, setPessoaEdit] = useState();
  const [indexPessoa, setIndexPessoa] = useState(null);
  const [selecionados, setSelecionados] = useState([]);

  function editar(pessoa, index) {
    setIndexPessoa(index);
    setAbrirModal(true);
    setPessoaEdit(pessoa);
    console.log(pessoa, index);
    getUser(pessoa?.nome);
  }

  function fecharModal() {
    setAbrirModal(false);
  }

  function selecionar (id) {
    if (selecionados.indexOf(id) !== -1) { // Se retornar -1 o id não está na lista
      const copiaSelecionado = selecionados.filter((elemento) => elemento != id)
      setSelecionados(copiaSelecionado)
    } else {
      let copia = [...selecionados, id]
      setSelecionados(copia)
    }
  }
  
  console.log(selecionados)

  return (
    <>
      <Modal
        pessoa={pessoaEdit}
        setAbrirModal={setAbrirModal}
        abrirModal={abrirModal}
        fecharModal={fecharModal}
        id={indexPessoa}
      />
      <div>
        {/* <h2 className={styles.title}>Tabela</h2> */}
        <table className={styles.table}>
          <thead className={styles.th}>
            <tr>
              <th>NOME</th>
              <th>IDADE</th>
              <th>ESTADO CIVIL</th>
              <th>CPF</th>
              <th>EDITAR</th>
              <th>APAGAR</th>
              <th>SELECIONAR</th>
            </tr>
          </thead>

          <tbody>
            {dados?.map((cadastroPessoa, index) => (
              <tr className={styles.td} key={index}>
                <td>{cadastroPessoa.nome}</td>
                <td>{cadastroPessoa.idade}</td>
                <td>{cadastroPessoa.estadoCivil}</td>
                <td>{cadastroPessoa.cpf}</td>
                <td>
                  <button
                    className={styles.btn}
                    onClick={() => {
                      editar(cadastroPessoa, index);
                    }}
                  >
                    <EditIcon
                      sx={{
                        fontSize: "large",
                        color: "white",
                        bgcolor: "transparent",
                      }}
                    />
                  </button>
                </td>
                <td>
                  <button
                    className={styles.btn}
                    onClick={() => {
                      deleteUser(cadastroPessoa.id);
                    }}
                  >
                    <DeleteOutlineIcon
                      sx={{
                        fontSize: "large",
                        color: "white",
                        bgcolor: "transparent",
                      }}
                    />
                  </button>
                </td>
                <td className={styles.input}>
                    <input type="checkbox" name="checkbox" id={cadastroPessoa.id} className={styles.input} checked={selecionados.includes(cadastroPessoa.id)} onChange={() => {selecionar(cadastroPessoa.id)}}/>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        {selecionados.length > 0 && (
          <button className={styles.buttonApagarSelecionados} onClick={() => {
            deleteUsers(selecionados)
          }}>Apagar Selecionados</button>
        )}
      </div>
    </>
  );
}

export default Tabela;
