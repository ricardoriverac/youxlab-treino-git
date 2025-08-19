import style from "./Tabela.module.css"

function Tabela({ dados, setDados, setNome, setCpf, setDataDeNascimento, setEditando, setIndex }) {
  
  const editar = (index) => {
    setEditando(true)
    setIndex(index)
    const editada = dados[index];
    setNome(editada.nome)
    setCpf(editada.cpf)
    setDataDeNascimento(editada.dataDeNascimento)
  };

  function Deletar(index) {
    const novosDados = [...dados];  
    novosDados.splice(index, 1);
    setDados(novosDados);
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
          {dados.map((dado, index) => {
            return (
              <tr key={index}>
                <td>{dado.nome}</td>
                <td>{dado.cpf}</td>
                <td>{dado.dataDeNascimento}</td>
                <td>
                  <button className={style.btnEditar} onClick={()=> editar(index)}>Editar</button>
                </td>
                <td>
                  <button className={style.btnDeletar} onClick={()=> Deletar(index)}>Deletar</button>
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
