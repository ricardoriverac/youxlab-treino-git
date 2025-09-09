import { useEffect, useState } from "react";
import { pegarProdutos } from "../services/api";
import Modal from "../pages/Modal";
import styles from "./Tabela.module.css";

function Tabela() {
  const [produtos, setProdutos] = useState("");
  const [openModal, setOpenModal] = useState(false);

  useEffect(() => {
    pegarProdutosBanco();
  }, []);

  async function pegarProdutosBanco() {
    try {
      const pegandoProdutos = await pegarProdutos();
      setProdutos(pegandoProdutos.data);
      console.log("produtos :>> ", produtos);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div>
      <Modal
        isOpen={openModal}
        setModalOpen={() => setOpenModal(!openModal)}
        openModal={openModal}
        setOpenModal={setOpenModal}
        pegarProdutosBanco={pegarProdutosBanco}
      />
      <div className={styles.divBotao}>
        <button
        className={styles.btnNovoProduto}
        onClick={() => {
            setOpenModal(true);
        }}>+ Novo Produto</button>
      </div>
        
      <table className={styles.tabela}>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Categoria</th>
            <th>Descrição</th>
            <th>Quantidade</th>
            <th>Preço</th>
          </tr>
        </thead>
        <tbody>
          {produtos.length ? (
            produtos.map((linha, i) => {
              return (
                <tr key={i}>
                  <td>{linha.nome}</td>
                  <td>{linha.categoria}</td>
                  <td>{linha.descricao}</td>
                  <td>{linha.quantidade}</td>
                  <td>R${linha.preco}</td>
                </tr>
              );
            })
          ) : (
            <tr>
              <td>vazio</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
