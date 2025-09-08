function Tabela({
  filtroCategoria,
  setFiltroCategoria,
  filtroPrazo,
  setFiltroPrazo,
  dadosFiltrados,
  Deletar,
  Editando,
  MarcarConcluido,
}) {
  const getRowStyle = (prazo) => {
    if (prazo === "Concluído") {
      return {
        textDecoration: "line-through",
        backgroundColor: "#f0f0f0ff",
        color: "green",
      };
    }
    if (prazo === "atrasada") {
      return { backgroundColor: "#ffcccc", color: "red" };
    }
    if (prazo === "Pendente") {
      return { backgroundColor: "#fff8cc", color: "#b8860b" };
    }
    return {};
  };
 
  return (
    <div>
      <div>
        <label>
          Categoria:
          <input
            type="text"
            value={filtroCategoria}
            onChange={(e) => setFiltroCategoria(e.target.value)}
            placeholder="Filtrar por categoria"
          />
        </label>

        <label>
          Prazo:
          <select
            value={filtroPrazo}
            onChange={(e) => setFiltroPrazo(e.target.value)}
          >
            <option value="">Todos</option>
            <option value="Pendente">Pendentes</option>
            <option value="atrasada">Atrasadas</option>
            <option value="Concluído">Concluídas</option>
          </select>
        </label>
      </div>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Data</th>
            <th>Categoria</th>
            <th>Prazo</th>
            <th>Concluído</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {dadosFiltrados.map((item) => (
            <tr key={item.id} style={getRowStyle(item.prazo)}>
              <td>{item.nome}</td>
              <td>{item.data}</td>
              <td>{item.cartegoria}</td>
              <td>{item.prazo}</td>
              <td>
                <input
                  type="checkbox"
                  checked={item.prazo === "Concluído"}
                  onChange={() => MarcarConcluido(item)}
                />
              </td>
              <td>
                <button onClick={() => Editando(item)}>Editar</button>
                <button onClick={() => Deletar(item.id)}>Deletar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;