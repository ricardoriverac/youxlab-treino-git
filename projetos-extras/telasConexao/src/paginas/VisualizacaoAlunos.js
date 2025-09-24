import "./VisualizacaoAlunos.css";
import { useNavigate, useParams } from "react-router-dom";
import iconVisu from "../imagem/iconVisu.svg";
import { useEffect, useState } from "react";
import {
  buscarAlunosporId,
  editarAluno,
  devolvendoLivros,
  renovandoEmprestimos,
} from "../services/api";
import { toastError, toastSuccess } from "../toasts/toast";
import Tabela from "../tabelas/Tabela";
import formatarDate from "../utils/formataData";
import iconRenovar from "../imagem/iconRenovar.svg";
import iconDevolver from "../imagem/iconDevolver.svg";
import CadastrarAluno from "../modais/CadastrarAluno";
import RenovarEmpretimo, { hoje } from "../modais/RenovarEmprestimo";
import EfetuarDevolucao from "../modais/DevolucaoLivros";
import { formatarTelefone } from "../utils/formatarInputTelefone";
import { ToastContainer } from "react-toastify";
import { limparMascara } from "../utils/formataInputTelefoneVazio";

document.body.style.overflow = "hidden";

export default function VisualizacaoAlunos() {
  const navigate = useNavigate();
  const [infoAlunos, setInfoAlunos] = useState([]);
  const [infoLivros, setInfoLivros] = useState([]);
  const [infoLivrosFormatado, setInfoLivrosFormatado] = useState();
  const [rowSelecionada, setRowSelecionada] = useState(0);
  const [dataDevolvendo, setDataDevolvendo] = useState(0);
  const [openRenovar, setOpenRenovar] = useState(false);
  const [openDevolver, setOpenDevolver] = useState(false);
  const [openModal, setOpenModal] = useState(false);
  const [editandoAluno, setEditandoAluno] = useState(false);
  const [atualizarEmprestimos, setAtualizarEmprestimos] = useState(false);
  const [loadModal, setLoadModal] = useState(false);
  const [alunoEditado, setAlunoEditado] = useState(null);
  const parametrosAluno = useParams();
  const colunas = ["titulo", "emprestimo", "status", "devolucao", "acoes"];

  const estiloTabelaInfo = {
    height: "130%",
    width: "100%",
    margin: "0 auto",
    border: "1px solid var(--cor-cinzaMargin)",
    borderRadius: 2,
  };

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

  const openModalEditarAluno = (editando) => {
    if (editando) {
      setAlunoEditado(infoAlunos);
    }
    setEditandoAluno(editando);
    setOpenModal(true);
  };

  const cancelarModal = () => {
    setEditandoAluno(false);
    setAlunoEditado(null);
    setOpenModal(false);
  };

  const editarAlunoEvento = async (alunoEditado) => {
    try {
      setLoadModal(true);
      const limpandoTelefone = {
        idAluno: alunoEditado.idAluno,
        nome: alunoEditado.nome,
        telefone: limparMascara(alunoEditado.telefone),
      };
      await editarAluno(limpandoTelefone);
      setInfoAlunos(alunoEditado);
      toastSuccess("Aluno editado com sucesso!");
      cancelarModal();
    } catch (e) {
      toastError("Preencha com um telefone válido");
    } finally {
      setLoadModal(false);
    }
  };

  useEffect(() => {
    carregarInfo();
  }, []);

  useEffect(() => {
    formataDados();
  }, [infoLivros]);

  function openModalRenovar(e) {
    setRowSelecionada(e);
    setOpenRenovar(true);
  }

  function closeModalRenovar() {
    setRowSelecionada(null);
    setOpenRenovar(false);
  }

  function openModalDevolver(e) {
    setRowSelecionada(e);
    setOpenDevolver(true);
  }

  function closeModalDevolver() {
    setRowSelecionada(null);
    setOpenDevolver(false);
  }

  async function devolver() {
    await enviandoDevolvendoLivros();
    carregarInfo();
  }

  async function carregarInfo() {
    try {
      const respostaDoBackend = await buscarAlunosporId(parametrosAluno.id);
      setInfoAlunos(respostaDoBackend.data.aluno);
      setInfoLivros(respostaDoBackend.data.livros);
    } catch (error) {
      toastError("Erro ao carregar as informações");
    }
  }

  async function enviandoEmprestimoRenovado() {
    try {
      const objRenovando = {
        id_emprestimo: rowSelecionada.id,
        dataAtual: hoje(),
        dataEntrega: formatarDate(dataDevolvendo),
      };
      await renovandoEmprestimos(objRenovando);
      setOpenRenovar(false);
      toastSuccess("Empréstimo renovado!");
      setAtualizarEmprestimos(!atualizarEmprestimos);
    } catch (error) {
      toastError("Erro ao efetuar empréstimo!");
    }
  }

  async function enviandoDevolvendoLivros() {
    try {
      const objDevolvendo = {
        id_emprestimo: rowSelecionada.id,
        dataEntregue: formatarDate(dataDevolvendo),
      };
      await devolvendoLivros(objDevolvendo);
      setOpenDevolver(false);
      toastSuccess("Devolução efetuada!");
      setAtualizarEmprestimos(!atualizarEmprestimos);
    } catch (error) {
      toastError("Erro ao efetuar devolução!");
    }
  }

  function formataDados() {
    const objRetorno = infoLivros?.map((livro) => ({
      id: livro.idEmprestimo,
      titulo:
        livro.titulo.length > 30
          ? livro.titulo.slice(0, 30) + "..."
          : livro.titulo,
      emprestimo: formatarDate(livro.dataEmprestimo),
      status: livro.status === "EM_DIA" ? "Em dia" : "Em atraso",
      devolucao: formatarDate(livro.dataDevolucao),
      nomeAluno: infoAlunos.nome,
    }));
    setInfoLivrosFormatado(objRetorno);
  }

  const voltarAlunos = () => {
    navigate("/alunos");
  };

  return (
    <div className="containerVisuAlunos">
      <ToastContainer />
      <CadastrarAluno
        open={openModal}
        editando={editandoAluno}
        cancelar={cancelarModal}
        editar={editarAlunoEvento}
        alunoEditado={alunoEditado}
        loadModal={loadModal}
      />
      <RenovarEmpretimo
        open={openRenovar}
        cancelar={() => closeModalRenovar()}
        renovar={() => enviandoEmprestimoRenovado()}
        titulo={rowSelecionada?.titulo}
        aluno={rowSelecionada?.nomeAluno}
        id={rowSelecionada?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />
      <EfetuarDevolucao
        open={openDevolver}
        cancelar={() => closeModalDevolver()}
        devolver={() => devolver()}
        titulo={rowSelecionada?.titulo}
        aluno={rowSelecionada?.nomeAluno}
        id={rowSelecionada?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />
      <div className="topoInfo">
        <button className="btnVoltarAlunos" onClick={voltarAlunos}>
          <img src={iconVisu} alt="iconVisuAlunos" className="iconVisuAlunos" />
          Informações do aluno
        </button>
        <button
          className="btnEditar"
          onClick={() => openModalEditarAluno(true)}
        >
          Editar
        </button>
      </div>
      <div className="containerInformacoesAlunos">
        <div className="paragrafoNome">
          <p className="nome">Nome </p>
          <p>{infoAlunos.nome}</p>
        </div>
        <div className="paragrafoTelefone">
          <p className="telefone">Telefone</p>
          <p>{formatarTelefone(infoAlunos.telefone)}</p>
        </div>
      </div>
      <div className="tabelaLivros">
        {infoLivros.length === 0 ? (
          <span> Nenhum livro encontrado.</span>
        ) : (
          <Tabela
            isPaginado={false}
            dados={infoLivrosFormatado}
            colunas={colunas}
            acoes={acoes}
            estiloTabela={estiloTabelaInfo}
          />
        )}
      </div>
    </div>
  );
}
