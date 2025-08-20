import { FaPen, FaTrash } from "react-icons/fa";
import styles from './Tabela.module.css'

function Tabela({ dados, setDados, editarDados, deletarDados, marcarSelecionados, marcado, handleChange}) {

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
            <th>Selecionar</th>
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
                  <button className={styles.botaoEditar} onClick={() => editarDados(pessoa)}><FaPen /></button>
                </td>
                <td>
                  <button className={styles.botaoDeletar} onClick={() => deletarDados(pessoa.id)}><FaTrash /></button>
                </td>
                <td><input type="checkbox" onChange={() => marcarSelecionados(pessoa.id, i)} /></td>
              </tr>
            );
          }) : <tr><td>vazio</td></tr>}
          {/* {console.log(dados)} */}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
