import style from "./Formulario.module.css";

function Formulario({nome, setNome, cpf, setCpf, dataDeNascimento, setDataDeNascimento, dados, setDados, editando, setEditando, index, setIndex}) {
  function adicionarDados() {
    if (!nome || !cpf || !dataDeNascimento) {
      alert("Preencha todos os campos");
      return;
    } else {
      const obj = { nome: nome, cpf: cpf, dataDeNascimento: dataDeNascimento };
      if (editando) {
        setDados([...dados, obj]);
      } else {
        const dadosEditado = [...dados];
        dadosEditado.splice(index, 1, obj);
        setDados(dadosEditado);
      }
      setNome("");
      setCpf("");
      setDataDeNascimento("");
    }
  }
  return (
    <div className={style.formulario}>
      <label>Nome: </label>
      <input
        type="text"
        value={nome}
        placeholder="Digite o seu nome"
        onChange={(evento) => setNome(evento.target.value)}
      />

      <label>CPF: </label>
      <input
        type="text"
        value={cpf}
        placeholder="Digite o seu CPF"
        onChange={(evento) => setCpf(evento.target.value)}
      />

      <label>Data de nascimento: </label>
      <input
        type="date"
        value={dataDeNascimento}
        onChange={(evento) => setDataDeNascimento(evento.target.value)}
      />

      <button className={style.btnSalvar} onClick={adicionarDados}>
        Salvar
      </button>
    </div>
  );
}

export default Formulario;
