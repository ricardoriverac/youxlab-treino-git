import styles from "./modules.css/Modal.module.css";

function Filter({ filter, setFilter, filterCategoria, setFilterCategoria, ordenacao, setOrdenacao }) {
  return (
    <div className={styles.wrapper}>
      <div className={styles.group}>
        <label className={styles.label}>Filtrar</label>
        <select className={styles.select} value={filter} onChange={(e) => setFilter(e.target.value)}>
          <option value="todas">Todas</option>
          <option value="pendentes">Pendentes</option>
          <option value="concluidas">Concluídas</option>
          <option value="categoria">Por categoria</option>
        </select>

        {filter === "categoria" && (
          <select
            className={styles.select}
            value={filterCategoria}
            onChange={(e) => setFilterCategoria(e.target.value)}
          >
            <option value="">Selecione</option>
            <option value="escola">Escola</option>
            <option value="casa">Casa</option>
            <option value="trabalho">Trabalho</option>
          </select>
        )}
      </div>

      <div className={styles.group}>
        <label className={styles.label}>Ordenar</label>
        <select className={styles.select} value={ordenacao} onChange={(e) => setOrdenacao(e.target.value)}>
          <option value="recentes">Mais recentes</option>
          <option value="entrega">Mais próximas da entrega</option>
          <option value="alfabetica">Alfabética</option>
        </select>
      </div>
    </div>
  );
}

export default Filter;
