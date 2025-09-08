function Tabela({
  filtroCategoria,
  setFiltroCategoria,
  dadosFiltrados,
  Deletar,
  Editando,
}) {
  return (
    <div>
      <label>Filtrar por categoria: </label>
      <select
        value={filtroCategoria}
        onChange={(e) => setFiltroCategoria(e.target.value)}
      >
        <option value="">Todas</option>
        <option value="casa">Casa</option>
        <option value="trabalho">Trabalho</option>
        <option value="estudo">Estudo</option>
      </select>
      <hr/>
      <table>
        <tbody>
          {dadosFiltrados.map((item) => (
            <tr key={item.id}>
              <td>
                <input type="checkbox" />
              </td>
              <td>{item.nome}</td>
              <td>{item.data}</td>
              <td>{item.cartegoria}</td>
              <td>{item.prazo}</td>
              <td>
                <button onClick={() => Deletar(item.id)}>Apagar</button>
                <button onClick={() => Editando(item)}>Editar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
