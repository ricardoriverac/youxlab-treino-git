function Tabela({ dados, onEditar, }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Nome</th>
          <th>CPF</th>
          <th>Nascimento</th>
        </tr>
      </thead>
      <tbody>
        {dados.map((pessoa, i) => (
          <tr key={i}>
            <td>{pessoa.nome}</td>
            <td>{pessoa.cpf}</td>
            <td>{pessoa.nascimento}</td>
            <td>
              <button onClick={() => onEditar(pessoa)}>Editar</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Tabela;
