import styles from "./modules.css/Tabela.module.css";

function Tabela({ tarefas, editarTarefa, removerTarefa, alternarConclusao }) {
  return (
    <table className={styles.table}>
      <thead>
        <tr>
          <th>Concluir</th>
          <th>Tarefa</th>
          <th>Categoria</th>
          <th>Data de Entrega</th>
          <th>Status</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {tarefas.map((tarefa) => (
          <tr key={tarefa.id}>
            <td>
              <input
                type="checkbox"
                checked={tarefa.status === "concluida"}
                onChange={() => alternarConclusao(tarefa)}
              />
            </td>
            <td
              className={tarefa.status === "concluida" ? styles.concluida : ""}
            >
              {tarefa.nome}
            </td>
            <td>{tarefa.categoria}</td>
            <td>{tarefa.dataEntrega}</td>
            <td>{tarefa.status}</td>
            <td className={styles.actions}>
              <button onClick={() => editarTarefa(tarefa)}>Editar</button>
              <button onClick={() => removerTarefa(tarefa.id)}>Remover</button>

            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Tabela;
