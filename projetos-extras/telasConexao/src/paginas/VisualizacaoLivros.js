import "./VisualizacaoLivros.css";
import iconVisu from "../imagem/iconVisu.svg";
import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import RenovarEmpretimo, { hoje } from "../modais/RenovarEmprestimo";
import EfetuarDevolucao from "../modais/DevolucaoLivros";
import formatarDate from "../utils/formataData";
import EmprestarLivro from "../modais/EmprestarLivro";
import EditarLivro from "../modais/EditarLivro";
import { toastError, toastSuccess } from "../toasts/toast";
import {
  buscandoInfoLivro,
  buscarTodosAlunos,
  devolvendoLivros,
  efetuandoEmprestimo,
  emprestimoLivro,
  renovandoEmprestimos,
  buscarGeneros,
  salvandoEditar,
} from "../services/api";
import Tabela from "../tabelas/Tabela";
import iconRenovar from "../imagem/iconRenovar.svg";
import iconDevolver from "../imagem/iconDevolver.svg";
import { ToastContainer } from "react-toastify";
import validaData from "../utils/ValidaData";
import validandoQtdEmprestimos from "../utils/ValidaEmprestimo";

export default function VisualizacaoLivros() {
  const [modalEmprestar, setModalEmprestar] = useState(false);
  const [informacoesLivro, setInformacoesLivro] = useState([]);
  const [nomesAlunos, setNomesAlunos] = useState([]);
  const [generoOpcoes, setGeneroOpcoes] = useState([]);
  const [dataDevolvendo, setDataDevolvendo] = useState(0);
  const [alunoSelecionado, setAlunoSelecionado] = useState(null);
  const [nomeNovoAluno, setNomeNovoAluno] = useState("");
  const [telefoneNovoAluno, setTelefoneNovoAluno] = useState("");
  const [modalEditarLivrosOpen, setModalCadastrarLivrosOpen] = useState(false);
  const [listaDadosEmprestimo, setListaDadosEmprestimo] = useState([]);
  const [dadosFormatadosVisuLivros, setDadosFormatadosVisuLivros] = useState(
    []
  );
  const [qtdEmprestimoPage, setQtdEmprestimoPage] = useState(null);
  const [loadingPagina, setLoadingPagina] = useState(false);
  const [modalRenovar, setModalRenovar] = useState(false);
  const [modalDevolver, setModalDevolver] = useState(false);
  const [infoEmprestimo, setInfoEmprestimo] = useState(null);

  const params = useParams();
  const navigate = useNavigate();

  const colunasEmprestismo = [
    "aluno",
    "emprestimo",
    "status",
    "devolucao",
    "acoes",
  ];

  const acoes = [
    {
      texto: "Renovar",
      icon: iconRenovar,
      func: (e) => acaoRenovar(e),
    },
    {
      texto: "Devolver",
      icon: iconDevolver,
      func: (e) => acaoDevolver(e),
    },
  ];

  useEffect(() => {
    informacaoDadosLivro();
    buscarNomeAlunos();
    carregandoEmprestimosLivro();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    formatandoDadosTabela();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [listaDadosEmprestimo]);

  useEffect(() => {
    carregandoEmprestimosLivro();
    informacaoDadosLivro();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [modalDevolver]);

  useEffect(() => {
    carregandoEmprestimosLivro();
    informacaoDadosLivro();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [modalRenovar]);

  useEffect(() => {
    if (!modalEditarLivrosOpen) {
      informacaoDadosLivro();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [modalEditarLivrosOpen]);

  useEffect(() => {
    carregarGenero();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function informacaoDadosLivro() {
    try {
      const { data } = await buscandoInfoLivro(params.id);
      setInformacoesLivro(data);
    } catch (error) {
      toastError("Erro ao buscar informações do livro");
    }
  }

  async function emprestandoLivro() {
    if (validandoQtdEmprestimos(informacoesLivro.quantidade)) {
      return;
    }
    try {
      let objEmprestar = {
        id_livro: params.id,
        id_aluno: !alunoSelecionado ? null : alunoSelecionado?.id,
        nomeNovoAluno: nomeNovoAluno,
        telefoneNovoAluno: telefoneNovoAluno,
        dataAtual: hoje(),
        dataEntrega: formatarDate(dataDevolvendo),
      };
      await efetuandoEmprestimo(objEmprestar);
      await informacaoDadosLivro();
      await carregandoEmprestimosLivro();
      toastSuccess("Empréstimo realizado.");
    } catch (error) {
      toastError("Erro ao emprestar livro");
    }
  }

  async function buscarNomeAlunos() {
    try {
      const { data } = await buscarTodosAlunos();
      acessandoNomes(data);
    } catch (error) {
      toastError("Erro ao buscar alunos");
    }
  }

  async function editandoLivros(dados) {
    try {
      await salvandoEditar(dados);
      toastSuccess("Livro editado com sucesso!");
      setModalCadastrarLivrosOpen(false);
      informacaoDadosLivro();
    } catch (err) {
      toastError("Erro ao editar livro");
    }
  }

  async function carregandoEmprestimosLivro(page = 1, limit = 10) {
    try {
      setLoadingPagina(true);
      const { data } = await emprestimoLivro(params.id, limit, page);
      setListaDadosEmprestimo(data.emprestimo);
      setQtdEmprestimoPage(data.quantidadeEmprestimo);
    } catch (error) {
      toastError("Erro ao carregar lista de alunos");
    } finally {
      setLoadingPagina(false);
    }
  }

  async function renovarEmprestimoVisuLivros() {
    if (validaData(dataDevolvendo)) {
      setModalRenovar(true);
      return;
    }
    try {
      const objRenovando = {
        id_emprestimo: infoEmprestimo.id,
        dataAtual: hoje(),
        dataEntrega: formatarDate(dataDevolvendo),
      };
      await renovandoEmprestimos(objRenovando);
      setModalRenovar(false);
      toastSuccess("Empréstimo renovado!");
      limpandoCampos();
    } catch (error) {
      toastError("Erro ao efetuar empréstimo!");
    }
  }

  async function devolvendoEmprestimoVisuLivros() {
    if (validaData(dataDevolvendo)) {
      setModalDevolver(true);
      return;
    }
    try {
      const objDevolver = {
        id_emprestimo: infoEmprestimo.id,
        dataEntregue: formatarDate(dataDevolvendo),
      };
      await devolvendoLivros(objDevolver);
      setModalDevolver(false);
      toastSuccess("Devolução realizada.");
      limpandoCampos();
    } catch (error) {
      toastError("Erro ao efetuar devolução");
    }
  }

  async function carregarGenero() {
    try {
      const { data } = await buscarGeneros();
      formataGenero(data);
    } catch (error) {
      toastError("Erro ao carregar gêneros");
    }
  }

  function formatandoDadosTabela() {
    let objRetorno = [];
    listaDadosEmprestimo.map((c) => {
      objRetorno.push({
        id: c.idEmprestimo,
        aluno: c.nome.length > 30 ? c.nome.slice(0, 30) + "..." : c.nome,
        emprestimo: formatarDate(c.dataEmprestimo),
        status: c.status === "EM_DIA" ? "Em dia" : "Em atraso",
        devolucao: formatarDate(c.dataDevolucao),
      });
    });
    setDadosFormatadosVisuLivros(objRetorno);
  }

  function acessandoNomes(nomes) {
    let dadosNomes = [];
    nomes.map((nome) => {
      dadosNomes.push({
        ...nome,
        label: nome.nome,
      });
    });
    setNomesAlunos(dadosNomes);
  }

  function calculadorQtdPaginas() {
    const limiteAlunos = 10;
    const totalPaginasEmprestadas = Math.ceil(qtdEmprestimoPage / limiteAlunos);
    return totalPaginasEmprestadas;
  }

  function clickPaginacao(event, value) {
    carregandoEmprestimosLivro(value);
  }

  function acaoRenovar(e) {
    setModalRenovar(true);
    setInfoEmprestimo(e);
  }

  function acaoDevolver(e) {
    setModalDevolver(true);
    setInfoEmprestimo(e);
  }

  function voltarTela() {
    navigate("/livros");
  }

  function cancelar() {
    setModalEmprestar(false);
    setModalRenovar(false);
    setModalDevolver(false);
    limpandoCampos();
  }

  function limpandoCampos() {
    setAlunoSelecionado("");
    setNomeNovoAluno("");
    setTelefoneNovoAluno("");
    setDataDevolvendo("");
  }

  function formataGenero(generos) {
    let objGeneros = [];
    generos.map((genero) => {
      objGeneros.push({
        ...genero,
        label: genero.nome,
      });
    });
    setGeneroOpcoes(objGeneros);
  }

  return (
    <div className="caixa_visualizarLivro">
      <ToastContainer />
      <EmprestarLivro
        open={modalEmprestar}
        cancelar={cancelar}
        emprestar={emprestandoLivro}
        titulo={informacoesLivro?.titulo}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
        options={nomesAlunos}
        alunoSelecionado={alunoSelecionado}
        setAlunoSelecionado={setAlunoSelecionado}
        nomeNovoAluno={nomeNovoAluno}
        setNomeNovoAluno={setNomeNovoAluno}
        telefoneNovoAluno={telefoneNovoAluno}
        setTelefoneNovoAluno={setTelefoneNovoAluno}
      />

      <EditarLivro
        open={modalEditarLivrosOpen}
        cancelar={() => setModalCadastrarLivrosOpen(false)}
        dadosLivro={informacoesLivro}
        editar={editandoLivros}
        options={generoOpcoes}
        idLivro={params.id}
      />

      <RenovarEmpretimo
        open={modalRenovar}
        cancelar={cancelar}
        renovar={renovarEmprestimoVisuLivros}
        titulo={informacoesLivro?.titulo}
        aluno={infoEmprestimo?.aluno}
        id={infoEmprestimo?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />

      <EfetuarDevolucao
        open={modalDevolver}
        cancelar={cancelar}
        devolver={devolvendoEmprestimoVisuLivros}
        titulo={informacoesLivro?.titulo}
        aluno={infoEmprestimo?.aluno}
        id={infoEmprestimo?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />

      <RenovarEmpretimo
        open={modalRenovar}
        cancelar={cancelar}
        renovar={renovarEmprestimoVisuLivros}
        titulo={informacoesLivro?.titulo}
        aluno={infoEmprestimo?.aluno}
        id={infoEmprestimo?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />

      <EfetuarDevolucao
        open={modalDevolver}
        cancelar={cancelar}
        devolver={devolvendoEmprestimoVisuLivros}
        titulo={informacoesLivro?.titulo}
        aluno={infoEmprestimo?.aluno}
        id={infoEmprestimo?.id}
        dataDevolvendo={dataDevolvendo}
        setDataDevolvendo={setDataDevolvendo}
      />

      <div className="caixa_btn">
        <button onClick={voltarTela}>
          <img src={iconVisu} alt="seta de voltar" />
          Informações do livro
        </button>
        <div className="btn_modais">
          <button
            className="btn_editar"
            onClick={() => setModalCadastrarLivrosOpen(true)}
          >
            Editar
          </button>
          <button onClick={() => setModalEmprestar(true)}>Emprestar</button>
        </div>
      </div>
      <div className="caixa_infoLivros">
        <div className="dados_livro">
          <div className="coluna1">
            <div>
              <h4>ISBN </h4>
              <p>{informacoesLivro.isbn}</p>
            </div>
            <div>
              <h4>Data de publicação </h4>
              <p>{informacoesLivro.data_publicacao}</p>
            </div>
            <div>
              <h4>Acervo </h4>
              <p>{informacoesLivro.quantidade_livros}</p>
            </div>
          </div>
          <div className="coluna2">
            <div>
              <h4>Titulo </h4>
              <p title={informacoesLivro.titulo}>
               {informacoesLivro?.titulo?.length > 20
               ? informacoesLivro.titulo.slice(0, 20) + "..."
               : informacoesLivro?.titulo || "titulo desconhecido"}
              </p>
            </div>
            <div>
              <h4>Gênero </h4>
              <p> {informacoesLivro.genero}</p>
            </div>
            <div>
              <h4>Disponível </h4>
              <p>{informacoesLivro.quantidade}</p>
            </div>
          </div>
          <div className="coluna3">
            <div>
              <h4>Autor </h4>
              <p title={informacoesLivro.autor}>
              {informacoesLivro?.autor?.length > 30
                ? informacoesLivro.autor.slice(0, 30) + "..."
                : informacoesLivro?.autor || "Autor desconhecido"}
              </p>
            </div>
            <div>
              <h4>Editora </h4>
              <p title={informacoesLivro.editora}>
              {informacoesLivro?.editora?.length > 30
                ? informacoesLivro.editora.slice(0, 30) + "..."
                : informacoesLivro?.editora || "editora desconhecido"}
              </p>
            </div>
            <div>
              <h4>Localização </h4>
              <p title={informacoesLivro.localizacao_pratileira}>
               {informacoesLivro?.localizacao_pratileira?.length > 30
               ? informacoesLivro.localizacao_pratileira.slice(0, 30) + "..."
               : informacoesLivro?.localizacao_pratileira || "localizacao_pratileira desconhecido"}
              </p>
            </div>
          </div>
        </div>
        <div className="caixa_sinopse">
          <h4>Sinopse</h4>
          <p> {informacoesLivro.sinopse} </p>
        </div>
      </div>
      <div className="tabela_alunos_emprestimo">
        <Tabela
          dados={dadosFormatadosVisuLivros}
          colunas={colunasEmprestismo}
          acoes={acoes}
          qtdPaginas={calculadorQtdPaginas()}
          clickPaginacao={clickPaginacao}
          carregandoPagina={loadingPagina}
        />
      </div>
    </div>
  );
}
