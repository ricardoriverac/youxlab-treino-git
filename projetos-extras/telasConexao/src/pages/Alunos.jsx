import "./Alunos.css";
import adicionarUser from "../imagem/adicionarUser.svg";
import lupa from "../imagem/lupa.svg";
import Tabela from "../tabelas/Tabela";
import { useEffect, useState } from "react";
import { buscarAlunos, cadastrarAluno, editarAluno } from "../services/api";
import iconVisualizar from "../imagem/iconVisualizar.svg";
import iconEditar from "../imagem/iconEditar.svg";
import { useNavigate } from "react-router-dom";
import { toastError, toastSuccess } from "../toasts/toast";
import CadastrarAluno from "../modais/CadastrarAluno";
import { limparMascara } from "../utils/formataInputTelefoneVazio";
import { formatarTelefone } from "../utils/formatarInputTelefone";
import { ToastContainer } from "react-toastify";

document.body.style.overflow = "hidden";

export default function Alunos() {
  const [dadosAlunos, setDadosAlunos] = useState([]);
  const [dadosFormatadosAlunos, setDadosFormatadosAlunos] = useState(null);
  const [inputFiltro, setInputFiltro] = useState("");
  const [carregandoPaginacao, setCarregandoPaginacao] = useState(true);
  const [paginandoAlunos, setPaginandoAlunos] = useState(0);
  const [openModal, setOpenModal] = useState(false);
  const [editandoAluno, setEditandoAluno] = useState(false);
  const [loadModal, setLoadModal] = useState(false);
  const [alunoEditado, setAlunoEditado] = useState(null);

  const navigate = useNavigate();

  const colunasAlunos = [
    "aluno",
    "telefone",
    "status",
    "num_emprestimo",
    "acoes",
  ];

  const estiloTabelaAlunos = {
    height: "130%",
    width: "100%",
    margin: "0 auto",
    border: "1px solid var(--cor-cinzaMargin)",
    borderRadius: 2,
  };

  useEffect(() => {
    carregarDados();
  }, []);

  useEffect(() => {
    formataDadosAlunos();
  }, [dadosAlunos]);

  useEffect(() => {
    if (inputFiltro === "") {
      carregarDados();
    }
  }, [inputFiltro]);

  async function carregarDados(pagina = 1, limit = 10) {
    try {
      setCarregandoPaginacao(true);
      const objFiltro = {
        limit: limit,
        page: pagina,
        nome: inputFiltro,
      };
      const dados = await buscarAlunos(objFiltro);
      setDadosAlunos(dados.data.alunos || []);
      setPaginandoAlunos(dados.data.quantidadeAlunos || 0);
    } catch (error) {
      toastError("Erro ao carregar dados.");
    } finally {
      setCarregandoPaginacao(false);
    }
  }

  function formataDadosAlunos() {
    const objRetorno = [];
    if (dadosAlunos.length > 0) {
      dadosAlunos?.map((c) =>
        objRetorno.push({
          id: c.idAluno,
          aluno: c.nome.length > 30 ? c.nome.slice(0, 30) + "..." : c.nome,
          telefone: formatarTelefone(c.telefone),
          status: c.status === null || c.status === "ENTREGUE" ? "Sem livros" : c.status === "EM_DIA" ? "Em dia" : "Em atraso",
          num_emprestimo: c.quantidadeEmprestado,
        })
      );
      setDadosFormatadosAlunos(objRetorno);
    } else {
      setDadosFormatadosAlunos([]);
    }
  }

  function calculadorQtdPaginas() {
    const itensPorPagina = 10;
    const totalPaginas = Math.ceil((paginandoAlunos || 0) / itensPorPagina);
    return totalPaginas || 1;
  }

  async function clickPaginacao(event, value) {
    carregarDados(value);
  }

  const VisualizarAlunos = (e) => {
    navigate(`/visualizacaoAlunos/${e.id}`);
  };

  const acoesAlunos = [
    {
      texto: "Editar",
      icon: iconEditar,
      func: Editar,
    },
    {
      texto: "Visualizar",
      icon: iconVisualizar,
      func: VisualizarAlunos,
    },
  ];

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      carregarDados();
    }
  };

  const openModalCadastrarAluno = (editando) => {
    setEditandoAluno(editando);
    setOpenModal(true);
  };

  function Editar(e) {
    setEditandoAluno(true);
    setAlunoEditado({
      id: e.id,
      nome: e.aluno,
      telefone: formatarTelefone(e.telefone),
    });
    setOpenModal(true);
  }

  const cancelarModal = () => {
    setEditandoAluno(false);
    setAlunoEditado(null);
    setOpenModal(false);
  };

  const cadastrarAlunoEvento = async (aluno) => {
    try {
      setLoadModal(true);
      const alunoBody = {
        nome: aluno.nome,
        telefone: limparMascara(aluno.telefone),
      };
      await cadastrarAluno(alunoBody);
      carregarDados();
      toastSuccess("Aluno cadastrado com sucesso!");
      cancelarModal();
    } catch (e) {
      toastError("Preencha com um telefone válido.");
    } finally {
      setLoadModal(false);
    }
  };

  const editarAlunoEvento = async (alunoEditado) => {
    const editarAlunos = {
      idAluno: alunoEditado.idAluno,
      nome: alunoEditado.nome,
      telefone: limparMascara(alunoEditado.telefone),
    };
    try {
      setLoadModal(true);
      await editarAluno(editarAlunos);
      toastSuccess("Aluno editado com sucesso!");
      carregarDados();
      cancelarModal();
    } catch (e) {
      toastError("Erro ao editar aluno.");
    } finally {
      setLoadModal(false);
    }
  };

  return (
    <div className="containerAlunos">
      <ToastContainer />
      <CadastrarAluno
        open={openModal}
        editando={editandoAluno}
        cancelar={cancelarModal}
        cadastrar={cadastrarAlunoEvento}
        editar={editarAlunoEvento}
        alunoEditado={alunoEditado}
        loadModal={loadModal}
      />
      <div className="topoAlunos">
        <h1>Alunos </h1>
        <button
          className="cadastrarAluno"
          onClick={() => openModalCadastrarAluno(false)}
        >
          <img src={adicionarUser} alt="iconAddUser" className="iconAddAluno" />
          Cadastrar
        </button>
      </div>

      <div className="caixaBusca">
        <input
          id="input_alunos"
          type="text"
          placeholder="Buscar"
          className="inputBusca"
          value={inputFiltro}
          onChange={(e) => setInputFiltro(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button className="buttonBuscar">
          <img src={lupa} alt="iconeLupa" onClick={() => carregarDados()} />
        </button>
      </div>

      <div className="tabelaAlunos">
        {dadosAlunos.length === 0 ? (
          <span> Nenhum aluno encontrado.</span>
        ) : (
          <Tabela
            dados={dadosFormatadosAlunos}
            colunas={colunasAlunos}
            estiloTabela={estiloTabelaAlunos}
            qtdPaginas={calculadorQtdPaginas()}
            clickPaginacao={clickPaginacao}
            acoes={acoesAlunos}
            carregandoPaginacao={carregandoPaginacao}
          />
        )}
      </div>
    </div>
  );
}
