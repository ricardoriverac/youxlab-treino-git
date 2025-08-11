import styles from "./Formulario.module.css";

function Formulario({
  salvarPessoa,
  dados,
  setDados,
  nome,
  setNome,
  cpf,
  setCPF,
  nascimento,
  setNascimento,
}) {
  function salvarDados() {
    let dados = { nome, cpf, nascimento };

    if (dados.nome === "" || dados.cpf === "" || dados.nascimento === "") {
      alert("Preencha todos os campos!");
      return;
    } else if (dados.cpf.length < 11) {
      alert("CPF inválido! Deve conter 11 dígitos.");
      return;
    } else if (dados.cpf.length > 12) {
      alert("O Maximo de caracteres é 11, tente novamente!");
      return;
    }

    salvarPessoa(dados);

    setNome("");
    setCPF("");
    setNascimento("");
  }

  return (
    <div className={styles.caixaTotal}>
      <h1 className={styles.titulo}> Cadastro </h1>
      <div className={styles.linha}>
        <p>
          <label className={styles.label}>Nome: </label>
          <input
            className={styles.inputs}
            value={nome}
            type="text"
            placeholder="Digite seu nome"
            onChange={(e) => setNome(e.target.value)}
          />
        </p>
        <p>
          <label  className={styles.label}>CPF: </label>
          <input
            className={styles.inputs}
            value={cpf}
            type="text"
            placeholder="Qual é o seu CPF"
            onChange={(e) => setCPF(e.target.value)}
          />
        </p>
        <p>
          <label className={styles.label}>Data de nascimento: </label>
          <input
            className={styles.inputs}
            value={nascimento}
            type="date"
            placeholder="Data de nascimento"
            onChange={(e) => setNascimento(e.target.value)}
          />
        </p>
        <button className={styles.btnSalvar} onClick={salvarDados}>
          Salvar
        </button>
      </div>
    </div>
  );
}

export default Formulario;
