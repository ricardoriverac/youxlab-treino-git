import { useState, useEffect } from "react";
import styles from "./modules.css/Modal.module.css";
function ModalEditar({ tarefa, onClose, onSave }) {
  const [nome, setNome] = useState("");
  const [categoria, setCategoria] = useState("");
  const [dataEntrega, setDataEntrega] = useState("");

  useEffect(() => {
    if (tarefa) {
      setNome(tarefa.nome || "");
      setCategoria(tarefa.categoria || "");
      setDataEntrega(tarefa.dataEntrega || "");
    }
  }, [tarefa]);

  if (!tarefa) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (nome.trim().length < 3) {
      alert("O nome deve ter pelo menos 3 caracteres!");
      return;
    }
    onSave({ ...tarefa, nome, categoria, dataEntrega });
    onClose();
  };

  return (
    <div className={styles.backdrop}>
      <div className={styles.modal}>
        <header className={styles.header}>
          <h2 className={styles.title}>Editar Tarefa</h2>
          <button className={styles.close} onClick={onClose} >
          </button>
        </header>

        <form className={styles.form} onSubmit={handleSubmit}>
          <div className={styles.row}>
            <label className={styles.label}>Nome</label>
            <input
              className={styles.input}
              value={nome}
              onChange={(e) => setNome(e.target.value)}
            />
          </div>

          <div className={styles.row}>
            <label className={styles.label}>Categoria</label>
            <select
              className={styles.select}
              value={categoria}
              onChange={(e) => setCategoria(e.target.value)}
            >
              <option value="">Selecione</option>
              <option value="escola">Escola</option>
              <option value="casa">Casa</option>
              <option value="trabalho">Trabalho</option>
            </select>
          </div>

          <div className={styles.row}>
            <label className={styles.label}>Data de entrega</label>
            <input
              className={styles.input}
              type="date"
              value={dataEntrega}
              onChange={(e) => setDataEntrega(e.target.value)}
            />
          </div>

          <div className={styles.actions}>
            <button type="button" className={styles.btnCancelar} onClick={onClose}>
              Cancelar
            </button>
            <button type="submit" className={styles.btnSalvar}>
              Salvar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default ModalEditar;
