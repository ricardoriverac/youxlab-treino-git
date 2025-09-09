import { useState } from "react";

import styles from "./Modal.module.css";
import { salvarNovoProduro } from "../services/api";

function Modal({ isOpen, setModalOpen, openModal, setOpenModal, pegarProdutosBanco }) {
  const [nome, setNome] = useState("");
  const [categoria, setCategoria] = useState("");
  const [descricao, setDescricao] = useState("");
  const [quantidade, setQuantidade] = useState("");
  const [preco, setPreco] = useState("");

  async function adicionarProduto() {
    let novoProduto = {
      nome: nome,
      categoria: categoria,
      descricao: descricao,
      quantidade: quantidade,
      preco: preco,
    };

    try {
      await salvarNovoProduro(novoProduto);
    } catch (err) {
      console.log("err :>> ", err);
    }

    pegarProdutosBanco()
  }

  if (isOpen) {
    return (
      <div className={styles.caixa}>
        <div className={styles.conteudo}>
          <div className={styles.titulo}>
            <h2 className={styles.h2}>Adicionar produto</h2>
          </div>
          <div className={styles.divInputs}>
            <input
              type="text"
              className={styles.inputNome}
              placeholder="Nome do produto"
              onChange={(e) => setNome(e.target.value)}
              value={nome}
            />

            <input
              type="text"
              className={styles.inputNome}
              placeholder="Categoria"
              onChange={(e) => setCategoria(e.target.value)}
              value={categoria}
            />

            <input
              type="text"
              className={styles.inputNome}
              placeholder="Descrição"
              onChange={(e) => setDescricao(e.target.value)}
              value={descricao}
            />

            <input
              type="number"
              className={styles.inputNome}
              placeholder="Quantidade"
              onChange={(e) => setQuantidade(e.target.value)}
              value={quantidade}
            />

            <input
              type="number"
              className={styles.inputNome}
              placeholder="Preço"
              onChange={(e) => setPreco(e.target.value)}
              value={preco}
            />
          </div>
          <div className={styles.divBotoes}>
            <button
              onClick={() => {
                setOpenModal(!openModal);
                adicionarProduto()
              }}
              className={styles.btn}
            >
              Salvar
            </button>
            <button onClick={setModalOpen} className={styles.btnFechar}>
              Fechar
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default Modal;
