import "./Emprestimo.css";
import lupa from "../imagem/lupa.svg";
import Tabela from "../tabelas/Tabela";
import { useEffect, useState } from "react";
import {
  buscarEmprestimos,
  devolvendoLivros,
  renovandoEmprestimos,
} from "../services/api";
import formatarDate from "../utils/formataData";
import iconRenovar from "../imagem/iconRenovar.svg";
import iconDevolver from "../imagem/iconDevolver.svg";
import RenovarEmpretimo, { hoje } from "../modais/RenovarEmprestimo";
import EfetuarDevolucao from "../modais/DevolucaoLivros";
import { toastError, toastSuccess } from "../toasts/toast";
import validaData from "../utils/ValidaData";
import { ToastContainer } from "react-toastify";

document.body.style.overflow = "hidden";

export default function Emprestimo() {
  const [dadosEmprestimo, setDadosEmprestimo] = useState([]);
  const [dadosFormatadosEmprestimo, setDadosFormatadosEmprestimo] = useState(
    []
  );
  const [inputFiltro, setInputFiltro] = useState("");
  const [paginandoEmprestimo, setPaginandoEmprestimo] = useState(0);
  const [openRenovar, setOpenRenovar] = useState(false);
  const [openDevolver, setOpenDevolver] = useState(false);
  const [rowSelecionada, setRowSelecionada] = useState(0);
  const [carregandoPagina, setCarregandoPagina] = useState(false);
  const [dataDevolvendo, setDataDevolvendo] = useState(0);
  const [atualizarEmprestimos, setAtualizarEmprestimos] = useState(false);

  const colunasEmprestimo = [
    "titulo",
    "aluno",
    "emprestimo",
    "status",
    "devolucao",
    "acoes",
  ];
  const estiloTabelaEmprestimo = {
    height: "130%",
    width: "100%",
    margin: "0 auto",
    border: "1px solid var(--cor-cinzaMargin)",
    borderRadius: 2,
  };

  useEffect(() => {
    carregarDados();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    formataDadosEmprestimo();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [dadosEmprestimo]);

  useEffect(() => {
    if (inputFiltro === "") {
      carregarDados();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [inputFiltro]);

  useEffect(() => {
    carregarDados();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [atualizarEmprestimos]);

  async function enviandoEmprestimoRenovado() {
    if (validaData(dataDevolvendo)) {
      setOpenRenovar(true);
      return;
    }
    try {
      const objRenovando = {
        id_emprestimo: rowSelecionada.id,
        dataAtual: hoje(),
        dataEntrega: formatarDate(dataDevolvendo),
      };
      await renovandoEmprestimos(objRenovando);
      toastSuccess("Empréstimo renovado!");
      setOpenRenovar(false);
      setAtualizarEmprestimos(!atualizarEmprestimos);
      limparCampos();
    } catch (error) {
      toastError("Erro ao efetuar empréstimo!");
    }
  }

  async function enviandoDevolvendoLivros() {
    if (validaData(dataDevolvendo)) {
      setOpenDevolver(true);
      return;
    }
    try {
      const objDevolvendo = {
        id_emprestimo: rowSelecionada.id,
        dataEntregue: formatarDate(dataDevolvendo),
      };
      await devolvendoLivros(objDevolvendo);
      toastSuccess("Devolução efetuada com sucesso!");
      setOpenDevolver(false);
      setAtualizarEmprestimos(!atualizarEmprestimos);
      limparCampos();
    } catch (error) {
      toastError("Erro ao efetuar devolução");
    }
  }

  async function carregarDados(pagina = 1, limite = 10) {
    try {
      setCarregandoPagina(true);
      const objEmprestimo = {
        limit: limite,
        page: pagina,
        nome: inputFiltro,
      };
      const { data } = await buscarEmprestimos(objEmprestimo);
      setDadosEmprestimo(data.emprestimos || []);
      setPaginandoEmprestimo(data.quantidadeEmprestimos || 0);
    } catch (error) {
    } finally {
      setCarregandoPagina(false);
    }
  }

  function formataDadosEmprestimo() {
    const objRetorno = [];
    dadosEmprestimo?.map((c) =>
      objRetorno.push({
        id: c.id,

        titulo:
          c.livro.titulo.length > 32
            ? c.livro.titulo.slice(0, 32) + "..."
            : c.livro.titulo,

        aluno:
          c.aluno.nome.length > 20
            ? c.aluno.nome.slice(0, 20) + "..."
            : c.aluno.nome,

        emprestimo: formatarDate(c.dataEmprestimo),

        status: c.status === "EM_DIA" ? "Em dia" : "Em atraso",

        devolucao: formatarDate(c.dataPrevistaEntrega),
      })
    );
    setDadosFormatadosEmprestimo(objRetorno);
  }

  function calculadorQtdPaginas() {
    const itensPorPagina = 10;
    const totalPaginas = Math.ceil((paginandoEmprestimo || 0) / itensPorPagina);
    return totalPaginas || 1;
  }

  function clickPaginacao(event, value) {
    carregarDados(value);
  }

  function openModalRenovar(e) {
    setRowSelecionada(e);
    setOpenRenovar(true);
  }

  function openModalDevolver(e) {
    setRowSelecionada(e);
    setOpenDevolver(true);
  }

  function closeModalRenovar() {
    setRowSelecionada(null);
    setOpenRenovar(false);
    limparCampos();
  }

  function closeModalDevolver() {
    setRowSelecionada(null);
    setOpenDevolver(false);
    limparCampos();
  }

  function devolver() {
    enviandoDevolvendoLivros();
  }

  function limparCampos() {
    setDataDevolvendo("");
  }
  const acoes = [
    {
      texto: "Renovar",
      icon: iconRenovar,
      func: openModalRenovar,
    },
    {
      texto: "Devolver",
      icon: iconDevolver,
      func: openModalDevolver,
    },
  ];

  return (
    <div className="container_emprestimo">
      <ToastContainer />
      <RenovarEmpretimo
        open={openRenovar}
        cancelar={() => closeModalRenovar()}
        renovar={() => enviandoEmprestimoRenovado()}
        titulo={rowSelecionada?.titulo}
        aluno={rowSelecionada?.aluno}
        id={rowSelecionada?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />
      <EfetuarDevolucao
        open={openDevolver}
        cancelar={() => closeModalDevolver()}
        devolver={() => devolver()}
        titulo={rowSelecionada?.titulo}
        aluno={rowSelecionada?.aluno}
        id={rowSelecionada?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />

      <h1>Empréstimos</h1>
      <>
        <div className="caixa_buscar">
          <input
            id="input_emprestimo"
            value={inputFiltro}
            type="text"
            placeholder="Buscar"
            className="input_emprestimo"
            onChange={(e) => setInputFiltro(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                carregarDados();
              }
            }}
          />
          <button className="btn_pesquisar" onClick={() => carregarDados()}>
            <img src={lupa} alt="lupa" />
          </button>
        </div>

        <div className="div_tabela">
          {dadosFormatadosEmprestimo.length === 0 ? (
            <div className="msg_dadoNaoEncontrado">
              <span>Nenhum dado encontrado.</span>
            </div>
          ) : (
            <Tabela
              dados={dadosFormatadosEmprestimo}
              colunas={colunasEmprestimo}
              estiloTabela={estiloTabelaEmprestimo}
              qtdPaginas={calculadorQtdPaginas()}
              clickPaginacao={clickPaginacao}
              acoes={acoes}
              carregandoPagina={carregandoPagina}
            />
          )}
        </div>
      </>
    </div>
  );
}
