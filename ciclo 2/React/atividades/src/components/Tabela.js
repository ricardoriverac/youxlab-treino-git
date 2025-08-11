import { FaTrash } from "react-icons/fa";
import { FaPencilAlt } from "react-icons/fa";
import styles from "./Tabela.module.css";
function Tabela({ dados, setDados, setNome, setCPF, setNascimento }) {
  const removerDados = (i) => {
    const novosDados = [...dados];
    novosDados.splice(i, 1);
    setDados(novosDados);
  };

  const editarDados = (index) => {
    const dadosNovo = dados[index];
    setNome(dadosNovo.nome);
    setCPF(dadosNovo.cpf);
    setNascimento(dadosNovo.nascimento);

    const novosDados = [...dados];
    novosDados.splice(index, 1);
    setDados(novosDados);
  };
  

  return (
    <table className={styles.tabela}>
      
      <thead>
        <tr>
          <th className={styles.tabelinha}>Nome</th>
          <th>CPF</th>
          <th>Nascimento</th>
        </tr>
      </thead>
      <tbody>
        {dados.map((pessoa, i) => (
          <tr key={i}>
            <td className={styles.tabelatd}>{pessoa.nome}</td>
            <td className={styles.tabelatd}>{pessoa.cpf}</td>
            <td className={styles.tabelatd}>{pessoa.nascimento}</td>
            <td>
              <button  className={styles.btnEditar} onClick={() => editarDados(i)}>
                Editar <FaPencilAlt />
              </button>
              <button className={styles.btnApagar} onClick={() => removerDados(i)}>
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
