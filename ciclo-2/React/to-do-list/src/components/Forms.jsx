import Inputs from "./Inputs";

function Forms({
  salvarTarefa,
  nome,
  setNome,
  categoria,
  setCategoria,
  dataEntrega,
  setDataEntrega,
  isEditando,
}) {
  function handleSubmit(e) {
    e.preventDefault();

    if (nome.trim().length < 3) {
      alert("O nome deve ter pelo menos 3 caracteres!");
      return;
    }

    const novaTarefa = {
      nome,
      categoria,
      dataEntrega,
      status: "pendente", 
      dataCriacao: new Date 
    };

    salvarTarefa(novaTarefa);
  }

  return (
    <form onSubmit={handleSubmit}>
      <Inputs label="Tarefa" value={nome} onChange={setNome} />

      <div>
        <label>Categoria</label>
        <select
          value={categoria}
          onChange={(e) => setCategoria(e.target.value)}
        >
          <option value="">Selecione</option>
          <option value="escola">Escola</option>
          <option value="casa">Casa</option>
          <option value="trabalho">Trabalho</option>
        </select>
      </div>

      <Inputs
        label="Data de entrega"
        type="date"
        value={dataEntrega}
        onChange={setDataEntrega}
      />

      <button type="submit">
        {isEditando ? "Salvar Alteração" : "Adicionar Tarefa"}
      </button>
    </form>
  );
}

export default Forms;
