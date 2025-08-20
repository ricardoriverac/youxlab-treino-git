import React from "react";

import style from "./tabela.module.css";


function TabelaDados({ dados, remover, editar }) {
  return (
    <div>
      <h3 className={style.h3}>Lista de Dados</h3>
      <table className={style.table}>
        <thead>
          <tr>
            <th>Nome</th>
            <th>CPF</th>
            <th>Data de Nascimento</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {dados.map((item) => (
            <tr key={item.id}>
              <td>{item.nome}</td>
              <td>{item.cpf}</td>
              <td>{item.data}</td>
              <td>
                <button onClick={() => remover(item.id)}>Remover</button>
                <button onClick={() => editar(item)}>Editar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default TabelaDados;
