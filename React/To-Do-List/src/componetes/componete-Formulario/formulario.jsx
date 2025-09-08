import { useState, useEffect } from "react";
import {
  AdicionarTipo,
  listarCArtegorias,
  Apagar,
  Editar,
} from "../service/api";
import Inputs from "../componete-Input/Inputs";
import Tabela from "../componete-Tabela/tabela";


function Formulario() {
  const [nome, setNome] = useState("");
  const [data, setData] = useState("");
  const [idEdit, setEditando] = useState(null);
  const [cartegoria, setCatrtegoria] = useState("");
  const [dados, setDados] = useState([]);
  const [filtroCategoria, setFiltroCategoria] = useState("");
  const [filtroPrazo, setFiltroPrazo] = useState("");

  const DataAtual = new Date();

  useEffect(() => {
    MostrarDados();
  }, []);

  async function MostrarDados() {
    const tipos = await listarCArtegorias();
    setDados(tipos.data);
  }

  async function Adiconar() {
    try {
      const item = {
        nome: nome,
        data: data,
        cartegoria: cartegoria,
        prazo: new Date(data) < DataAtual ? "atrasada" : "Pendente",
      };

      
      if (idEdit) {
        await Editar(idEdit, item);
      } else {
        await AdicionarTipo(item);
      }

      await MostrarDados();
      Limpar();
    } catch (error) {
      console.error(error);
    }
  }

  function Limpar() {
    setNome("");
    setData("");
    setCatrtegoria("");
    setEditando(null);
  }

  async function Deletar(id) {
    try {
      await Apagar(id);
      MostrarDados();
    } catch (error) {
      console.error(error);
    }
  }

  function EditandoItem(item) {
    setEditando(item.id);
    setNome(item.nome);
    setData(item.data);
    setCatrtegoria(item.cartegoria);
  }

  async function MarcarConcluido(item) {
    try {
      await Editar(item.id, { ...item, prazo: "Concluído" });
      await MostrarDados();
    } catch (error) {
      console.error(error);
    }
  }

  const dadosFiltrados = dados.filter((item) => {
    const filtroCategoriaOk =
      filtroCategoria === "" || item.cartegoria === filtroCategoria;

    const filtroPrazoOk = filtroPrazo === "" || item.prazo === filtroPrazo;

    return filtroCategoriaOk && filtroPrazoOk;
  });

  return (
    <div>
      <Inputs
        idEdit={idEdit}
        cartegoria={cartegoria}
        nome={nome}
        setCatrtegoria={setCatrtegoria}
        setData={setData}
        setNome={setNome}
        data={data}
        Adiconar={Adiconar}
      />
      <Tabela
        filtroCategoria={filtroCategoria}
        setFiltroCategoria={setFiltroCategoria}
        filtroPrazo={filtroPrazo}
        setFiltroPrazo={setFiltroPrazo}
        dadosFiltrados={dadosFiltrados}
        Deletar={Deletar}
        Editando={EditandoItem}
        MarcarConcluido={MarcarConcluido}
      />
    </div>
  );
}

export default Formulario;
