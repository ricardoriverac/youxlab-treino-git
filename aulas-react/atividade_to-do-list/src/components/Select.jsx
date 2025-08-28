import styles from "./Select.module.css";

function Select({ nome, categorias, categoriaSelecionada, setCategoriaSelecionada }) {
  return (
    <div>
      <select
        name={nome}
        id={nome}
        onChange={(e) => setCategoriaSelecionada(e.target.value)}
        className={styles.select}
        value={categoriaSelecionada}
      >
        <option>Selecione a categoria</option>

        {categorias.map((categoria) => (
          <option value={categoria.nome} key={categoria.id}>
            {categoria.nome}
          </option>
        ))}
      </select>
    </div>
  );
}

export default Select;
