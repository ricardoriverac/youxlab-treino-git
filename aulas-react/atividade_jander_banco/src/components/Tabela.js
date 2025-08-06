import { FaPen, FaTrash } from "react-icons/fa";
import styles from './Tabela.module.css'

function Tabela({ dados, setDados, editarDados }) {
  const novosDados = [...dados];

  const removerDados = (i) => {
    novosDados.splice(i, 1);
    setDados(novosDados);
  };

  return (
    <div>
      <table className={styles.tabela}>
        <thead>
          <h4>Listagem de Pessoas</h4>
          <tr className={styles.cabecario}>
            <th>Nome</th>
            <th>CPF</th>
            <th>Telefone</th>
            <th>Data de Nascimento</th>
            <th>Editar</th>
            <th>Deletar</th>
          </tr>
        </thead>
        <tbody>
          { dados.length ? dados.map((pessoa, i) => { 
            return (
              <tr key={i} className={styles.dados}>
                <td>{pessoa.name}</td>
                <td>{pessoa.cpf}</td>
                <td>{pessoa.telefone}</td>
                <td>{pessoa.nascimento}</td>
                <td>
                  <button className={styles.botaoEditar} onClick={() => editarDados(i)}><FaPen /></button>
                </td>
                <td>
                  <button className={styles.botaoDeletar} onClick={() => removerDados(i)}><FaTrash /></button>
                </td>
              </tr>
            );
          }) : <tr><td>fds</td></tr>}
          {/* {console.log(dados)} */}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
