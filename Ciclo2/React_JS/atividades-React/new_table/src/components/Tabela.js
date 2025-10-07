import { useState } from "react";
import { Deletar } from "../service/api";
import style from "./Tabela.module.css";

function Tabela({
  dados,
  buscarPessoas,
  editar
}) {

  async function deletar(id) {
    try {
      await Deletar(id);
      buscarPessoas();
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div className={style.tabela}>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>CPF</th>
            <th>Data de nascimento</th>
            <th>Editar</th>
            <th>Deletar</th>
          </tr>
        </thead>
        <tbody>
          {dados.map((dado) => {
            return (
              <tr key={dado.id}>
                <td>{dado.name}</td>
                <td>{dado.cpf}</td>
                <td>{dado.dataNascimento}</td>
                <td>
                  <button
                    className={style.btnEditar}
                    onClick={() => editar(dado)}
                  >
                    Editar
                  </button>
                </td>
                <td>
                  <button
                    className={style.btnDeletar}
                    onClick={() => deletar(dado.id)}
                  >
                    Deletar
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
export default Tabela;
