import styles from "./inputs.module.css";

function FormularioInputs({
  nome,
  cpf,
  data,
  setNome,
  setCpf,
  setData,
  adicionar,
}) {
  return (
    <div>
      <input
        className={styles.dados}
        type="text"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
        placeholder="Seu nome"
      />
      <input
        className={styles.dados}
        type="text"
        value={cpf}
        onChange={(e) => setCpf(e.target.value)}
        placeholder="Seu CPF"
      />
      <input
        className={styles.dados}
        type="date"
        value={data}
        onChange={(e) => setData(e.target.value)}
        placeholder="Sua data de nascimento"
      />
      <button className={styles.butonA} onClick={() => adicionar()}>
        Adicionar
      </button>
    </div>
  );
}

export default FormularioInputs;
