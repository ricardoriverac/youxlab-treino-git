import { useState } from "react";
import "./Tabela.css";
import { apagarLinha, pegarDados, pegarImagem, salvarDados } from "../service/api";
import { useEffect } from "react";

function Tabela() {
  const [nome, setNome] = useState("");
  const [dados, setDados] = useState([]);

  useEffect(() => {
    pegarDadosBanco();
    console.log('nome :>> ', nome);
  }, [nome]);

  async function pegarImagemDados(nome) {
    try {
      const pegandoImagem = await pegarImagem(nome);
      const imagemCerta = pegandoImagem.data.hits[0].webformatURL;

      return imagemCerta;
    } catch (error) {
      console.log("error :>> ", error);
      return null;
    }
  }
  
  async function pegarDadosBanco() {
    try {
      const pegandoDados = await pegarDados();
      setDados(pegandoDados.data);
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  async function salvarDadosBanco() {
    try {
      const imagemURL = await pegarImagemDados(nome);

      let novoItem = {
        nome: nome,
        imagem: imagemURL,
      };

      setDados((prev) => [...prev, novoItem]);
      await salvarDados(novoItem);
      
      setNome("");
      pegarDadosBanco();

      console.log('nomeD :>> ', nome);
    } catch (err) {
        console.log("err :>> ", err);
    }
  }

  async function deletarLinha(idLinha) {
    try {
      await apagarLinha(idLinha);
      pegarDadosBanco();
    } catch (err) {
      console.log("err :>> ", err);
    }
  }

  return (
    <div>
      <div className="form">
        <input
          className="input"
          type="text"
          value={nome}
          onChange={(e) => setNome(e.target.value)}
          placeholder="Digite um nome"
        />
        <button className="btn" onClick={() => salvarDadosBanco()}>
          Enviar
        </button>
      </div>
      <table className="tabela">
        <thead>
          <tr>
            <th>Nome</th>
            <th>Imagem</th>
            <th>Deletar</th>
          </tr>
        </thead>
        <tbody>
          {dados.length ? (
            dados.map((linha, i) => {
              return (
                <tr key={i}>
                  <td>{linha.nome}</td>
                  <td>
                    <img src={linha.imagem} alt={linha.nome} width={80} />
                  </td>
                  <td>
                    <button className="btnDeletar" onClick={() => deletarLinha(linha.id)}>Deletar</button>
                  </td>
                </tr>
              );
            })
          ) : (
            <tr>
              <td>vazio</td>
              <td>Imagem não encontrada</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}

export default Tabela;
