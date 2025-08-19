import { FaTrash, FaPencilAlt } from "react-icons/fa";
import styles from "./Tabela.module.css";

function Tabela({ dados, setNome, setCPF, setNascimento, removerPessoa }) {
  const editarDados = (index) => {
    const pessoa = dados[index];
    setNome(pessoa.nome);
    setCPF(pessoa.cpf);
    setNascimento(pessoa.nascimento);
  };

  return (
    <table className={styles.tabela}>
      <thead>
        <tr>
          <th className={styles.tabelinha}>Nome</th>
          <th>CPF</th>
          <th>Nascimento</th>
          <th>Ações</th>
        </tr>
      </thead>
      <tbody>
        {dados.map((pessoa, i) => (
          <tr key={pessoa.id}>
            <td className={styles.tabelatd}>{pessoa.nome}</td>
            <td className={styles.tabelatd}>{pessoa.cpf}</td>
            <td className={styles.tabelatd}>{pessoa.nascimento}</td>
            <td>
              <button
                className={styles.btnEditar}
                onClick={() => editarDados(i)}
              >
                Editar <FaPencilAlt />
              </button>
              <button
                className={styles.btnApagar}
                onClick={() => removerPessoa(pessoa.id)}
              >
                Apagar <FaTrash />
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Tabela;