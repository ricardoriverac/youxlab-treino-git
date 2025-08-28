import Select from "./Select";

import styles from "./Inputs.module.css";

function Inputs({
  categoria,
  pegarCategorias,
  setCategoriaSelecionada,
  salvarDados,
  setTarefa,
  setData,
  data,
  tarefa,
  categoriaSelecionada,
}) {
  return (
    <div>
      <section className={styles.form}>
        <h2 className={styles.titulo}>Adicionar tarefa</h2>
        <div className={styles.formRow}>
          <input
            type="text"
            className={styles.inputNome}
            onChange={(e) => setTarefa(e.target.value)}
            placeholder="Nome da tarefa"
            value={tarefa}
          />
        </div>
        <div className={styles.formRow}>
          <Select
            nome="category_id"
            categorias={categoria}
            handleChange={pegarCategorias}
            setCategoriaSelecionada={setCategoriaSelecionada}
            categoriaSelecionada={categoriaSelecionada}
          />
          <input
            type="date"
            className={styles.inputData}
            onChange={(e) => setData(e.target.value)}
            value={data}
          />
        </div>

        <button onClick={salvarDados} className={styles.btn}>
          Adicionar
        </button>

        <h2 className={styles.titulo}>Lista de tarefas</h2>
      </section>
    </div>
  );
}

export default Inputs;
