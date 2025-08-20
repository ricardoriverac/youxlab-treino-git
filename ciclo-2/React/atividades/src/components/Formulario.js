import styles from "./Formulario.module.css";

function Formulario({
  salvarPessoa,
  nome,
  setNome,
  cpf,
  setCPF,
  nascimento,
  setNascimento,
  isEditando
}) {
  function salvarDados() {
    const pessoa = { nome, cpf, nascimento };

    if (!pessoa.nome || !pessoa.cpf || !pessoa.nascimento) {
      alert("Preencha todos os campos!");
      return;
    }
    if (pessoa.cpf.length < 11) {
      alert("CPF inválido! Deve conter 11 dígitos.");
      return;
    }
    if (pessoa.cpf.length > 11) {
      alert("O máximo de caracteres é 11, tente novamente!");
      return;
    }

    salvarPessoa(pessoa);
  }

  return (
    <div className={styles.caixaTotal}>
      <h1 className={styles.titulo}>{isEditando ? "Editar Pessoa" : "Cadastro"}</h1>
      <div className={styles.linha}>
        <p>
          <label className={styles.label}>Nome:</label>
          <input
            className={styles.inputs}
            value={nome}
            type="text"
            placeholder="Digite seu nome"
            onChange={(e) => setNome(e.target.value)}
          />
        </p>
        <p>
          <label className={styles.label}>CPF:</label>
          <input
            className={styles.inputs}
            value={cpf}
            type="text"
            placeholder="Digite seu CPF"
            onChange={(e) => setCPF(e.target.value)}
          />
        </p>
        <p>
          <label className={styles.label}>Data de nascimento:</label>
          <input
            className={styles.inputs}
            value={nascimento}
            type="date"
            onChange={(e) => setNascimento(e.target.value)}
          />
        </p>
        <button className={styles.btnSalvar} onClick={salvarDados}>
          {isEditando ? "Atualizar" : "Salvar"}
        </button>
      </div>
    </div>
  );
}

export default Formulario;