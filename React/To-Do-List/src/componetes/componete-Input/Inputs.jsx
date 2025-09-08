function Inputs({
  idEdit,
  cartegoria,
  nome,
  setCatrtegoria,
  setData,
  setNome,
  data,
  Adiconar,
}) {
  return (
    <div>
      <input
        type="text"
        placeholder="Nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <input
        type="date"
        value={data}
        onChange={(e) => setData(e.target.value)}
      />
      <select value={cartegoria}
        onChange={(e) => setCatrtegoria(e.target.value)}
      >
      <option value="">Selecione uma Cartegoria</option>
      <option value="casa">Casa</option>
      <option value="trabalho">Trabalho</option>
      <option value="estudo">Estudo</option>
      </select>
      <button onClick={Adiconar}>
        {idEdit ? "Salvar edição" : "Adicionar"}
      </button>
    </div>
  );
}

export default Inputs;